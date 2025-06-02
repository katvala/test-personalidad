from flask import Flask, render_template, request, send_file, make_response, session
import csv
import os
import datetime
from dotenv import load_dotenv
from utils import interpretar_respuestas, interpretar_textos, LISTA_CaMiR, LISTA_SD3, OPCIONES_RESPUESTA
from google_drive import GoogleDriveManager
from weasyprint import HTML, CSS
from jinja2 import Template

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-key-change-in-production')

# Inicializar Google Drive Manager
print("🔧 Configurando Google Drive...")
drive_manager = None
try:
    drive_manager = GoogleDriveManager()
    if drive_manager.is_available():
        print("✅ Google Drive Manager inicializado y disponible")
        success, message = drive_manager.test_connection()
        if success:
            print("✅ Conexión con Google Drive verificada")
        else:
            print(f"⚠️ Problema con Google Drive: {message}")
    else:
        print("📁 Google Drive no configurado, usando solo almacenamiento local")
        drive_manager = None
except Exception as e:
    print(f"❌ Error al inicializar Google Drive: {e}")
    print("📁 La aplicación funcionará solo con guardado local")
    drive_manager = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html",
                           preguntas_apego=LISTA_CaMiR,
                           preguntas_sd3=LISTA_SD3,
                           opciones_respuesta=OPCIONES_RESPUESTA)

@app.route("/submit", methods=["POST"])
def submit():
    # 1) Separar datos demográficos de respuestas psicológicas
    edad = request.form.get("edad")
    sexo = request.form.get("sexo")
    carrera = request.form.get("carrera")
    
    # 2) Recoger solo las respuestas de las escalas psicológicas
    respuestas = {}
    for clave, valor in request.form.items():
        if clave not in ["edad", "sexo", "carrera"]:  # Excluir datos demográficos
            respuestas[clave] = valor
    
    # 3) Validar que todas las respuestas psicológicas sean números válidos del 1 al 5
    for clave, valor in respuestas.items():
        try:
            valor_int = int(valor)
            if valor_int < 1 or valor_int > 5:
                return "Error: Respuesta inválida", 400
        except ValueError:
            return "Error: Respuesta inválida", 400
    
    # 4) Cálculo numérico de promedios incluyendo dominantes
    resultado_numerico = interpretar_respuestas(respuestas)
    
    # 5) Cálculo textual (solo altos + dominantes + apoyo)
    resultado_textual = interpretar_textos(resultado_numerico)
    
    # 6) Crear directorio data si no existe
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)
    
    # 7) Preparar datos para CSV y Google Drive
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Preparar headers en un orden más lógico para JASP
    demographic_headers = ["timestamp", "edad", "sexo", "carrera"]
    
    # Puntuaciones calculadas (variables principales para análisis)
    score_headers = [
        "ApSeg_Total", "ApAns_Total", "ApEvi_Total", "ApDes_Total",  # Apego
        "Maq_Total", "Nar_Total", "Psi_Total",  # Triada
        "ApegoDominante", "TriadaDominante"  # Dominantes
    ]
    
    # Respuestas individuales (variables de respaldo)
    apego_labels = {
        'seg_': 'ApSeg_P', 'ans_': 'ApAns_P', 
        'evit_': 'ApEvi_P', 'desorg_': 'ApDes_P'
    }
    triada_labels = {
        'maq_': 'Maq_P', 'nar_': 'Nar_P', 'psi_': 'Psi_P'
    }
    
    def rename_question(q):
        for prefix, label in {**apego_labels, **triada_labels}.items():
            if q.startswith(prefix):
                num = q.split('_')[1]
                return f"{label}{num}"
        return q
    
    # Ordenar y renombrar las preguntas por escala
    apego_questions = sorted([k for k in respuestas.keys() if k.startswith(('seg_', 'ans_', 'evit_', 'desorg_'))])
    triada_questions = sorted([k for k in respuestas.keys() if k.startswith(('maq_', 'nar_', 'psi_'))])
    response_headers = [rename_question(q) for q in (apego_questions + triada_questions)]
    
    headers = demographic_headers + score_headers + response_headers
    
    # Preparar fila de datos
    demographic_data = [timestamp, edad, sexo, carrera]
    
    # Puntuaciones calculadas en el orden específico
    score_data = [
        round(float(resultado_numerico.get("Apego Seguro", 0)), 2),
        round(float(resultado_numerico.get("Apego Ansioso", 0)), 2),
        round(float(resultado_numerico.get("Apego Evitativo", 0)), 2),
        round(float(resultado_numerico.get("Apego Desorganizado", 0)), 2),
        round(float(resultado_numerico.get("Maquiavelismo", 0)), 2),
        round(float(resultado_numerico.get("Narcisismo", 0)), 2),
        round(float(resultado_numerico.get("Psicopatía", 0)), 2),
        resultado_numerico.get("Estilo de Apego Dominante", ""),
        resultado_numerico.get("Triada Dominante", "")
    ]
    
    # Respuestas individuales en el mismo orden que los headers
    response_data = [int(respuestas.get(q, 0)) for q in (apego_questions + triada_questions)]
    
    row_data = demographic_data + score_data + response_data
    
    # 8) Subir a Google Drive (con manejo robusto de errores)
    csv_data = [headers, row_data]
    filename = f"respuestas_{timestamp.replace(' ', '_').replace(':', '-')}.csv"
    
    print(f"💾 Procesando guardado de datos...")
    print(f"📊 Filename: {filename}")
    print(f"📈 Headers: {len(headers)} columnas")
    print(f"📋 Data: {len(row_data)} valores")
    
    # Intentar Google Drive primero
    google_drive_success = False
    try:
        if drive_manager and drive_manager.is_available():
            print("☁️ Intentando subir a Google Drive...")
            file_id = drive_manager.upload_csv(csv_data, filename)
            
            if file_id:
                print(f"✅ Archivo subido a Google Drive con ID: {file_id}")
                google_drive_success = True
            else:
                print("❌ Falló la subida a Google Drive")
        else:
            print("⚠️ Google Drive no está disponible")
            if drive_manager is None:
                print("   - Google Drive Manager no inicializado")
            elif not drive_manager.is_available():
                print("   - Credenciales o configuración faltante")
    except Exception as e:
        print(f"❌ Error inesperado con Google Drive: {e}")
        import traceback
        print(f"   Traceback: {traceback.format_exc()}")
    
    # Resultado del intento de Google Drive
    if google_drive_success:
        print("✅ Backup en Google Drive completado")
    else:
        print("⚠️ Google Drive no disponible, guardando solo localmente")
    
    # 9) Guardar localmente como respaldo (independientemente de Google Drive)
    print("💾 Guardando respaldo local...")
    
    csv_path = os.path.join(data_dir, "respuestas.csv")
    print(f"📂 Ruta CSV: {csv_path}")
    
    file_exists = os.path.exists(csv_path) and os.path.getsize(csv_path) > 0
    print(f"📄 Archivo existe: {file_exists}")
    
    try:
        with open(csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            
            if not file_exists:
                writer.writerow(headers)
                print("📋 Headers escritos")
            
            writer.writerow(row_data)
            print("📊 Datos escritos")
        
        # Verificar que se guardó correctamente
        if os.path.exists(csv_path):
            file_size = os.path.getsize(csv_path)
            print(f"✅ Guardado local exitoso - Tamaño: {file_size} bytes")
        else:
            print("❌ Error: archivo no se creó")
            
    except Exception as e:
        print(f"❌ Error al guardar localmente: {e}")
        import traceback
        print(f"   Traceback: {traceback.format_exc()}")
    
    # Resumen de guardado
    print("📊 RESUMEN DE GUARDADO:")
    print(f"   ☁️ Google Drive: {'✅ Exitoso' if google_drive_success else '❌ Falló'}")
    print(f"   💾 Local: {'✅ Guardado' if os.path.exists(csv_path) else '❌ Falló'}")
    
    # En producción, mostrar advertencia sobre almacenamiento efímero
    if os.getenv('RENDER') or os.getenv('RAILWAY_ENVIRONMENT'):
        print("⚠️ NOTA: En producción el almacenamiento local es efímero")
        print("   Los archivos locales se perderán al reiniciar el servicio")
        if not google_drive_success:
            print("   ❗ IMPORTANTE: Configura Google Drive para persistencia")
    
    # 8) Preparar datos para el gráfico radar
    chart_labels = []
    chart_values = []
    
    for categoria, puntuacion in resultado_numerico.items():
        # Filtrar categorías que no sean dominantes y que sean numéricas
        if categoria not in ['Estilo de Apego Dominante', 'Triada Dominante'] and isinstance(puntuacion, (int, float)):
            chart_labels.append(categoria)
            chart_values.append(float(puntuacion))
    
    chart_data = {
        'labels': chart_labels,
        'values': chart_values
    }
    
    # 9) Ensure all numeric values are properly converted to floats for template comparisons
    puntuaciones_numericas = {}
    puntuaciones_categoricas = {}
    
    for key, value in resultado_numerico.items():
        if key in ['Estilo de Apego Dominante', 'Triada Dominante']:
            # These are categorical, store separately
            puntuaciones_categoricas[key] = value
        else:
            # These should be numeric, convert to float
            try:
                puntuaciones_numericas[key] = float(value)
            except (ValueError, TypeError):
                puntuaciones_numericas[key] = 0.0  # Default to 0 if conversion fails
    
    # 10) Renderizar el template con ambos diccionarios
    # Guardar resultados en la sesión para el PDF
    session['interpretacion'] = resultado_numerico
    session['interpretacion_texto'] = resultado_textual
    session['puntuaciones'] = puntuaciones_numericas
    session['dominantes'] = puntuaciones_categoricas
    session['chartData'] = chart_data

    return render_template(
        "result.html",
        interpretacion=resultado_numerico,
        interpretacion_texto=resultado_textual,
        chartData=chart_data,
        puntuaciones=puntuaciones_numericas,
        dominantes=puntuaciones_categoricas
    )

@app.route("/descargar_pdf")
def descargar_pdf():
    """Generar y descargar resultados en PDF"""
    # Obtener la última interpretación de la sesión
    current_datetime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    
    resultado_html = render_template(
        "result_pdf.html",
        interpretacion=session.get('interpretacion', {}),
        interpretacion_texto=session.get('interpretacion_texto', {}),
        puntuaciones=session.get('puntuaciones', {}),
        dominantes=session.get('dominantes', {}),
        fecha_generacion=current_datetime
    )
    
    # Generar PDF desde HTML
    pdf = HTML(string=resultado_html).write_pdf()
    
    # Crear respuesta con el PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=resultados_test_personalidad.pdf'
    
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    debug = os.environ.get("FLASK_ENV") != "production"
    app.run(host="0.0.0.0", port=port, debug=debug)