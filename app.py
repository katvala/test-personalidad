from flask import Flask, render_template, request
import csv
from utils import interpretar_respuestas, interpretar_textos, LISTA_CaMiR, LISTA_SD3, OPCIONES_RESPUESTA

app = Flask(__name__)

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
    import os
    os.makedirs("data", exist_ok=True)
    
    # 7) Guardar en CSV con datos demográficos en las primeras columnas
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    csv_path = "data/respuestas.csv"
    file_exists = os.path.exists(csv_path) and os.path.getsize(csv_path) > 0
    
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Preparar headers en un orden más lógico para JASP
        if not file_exists:
            # 1. Datos demográficos
            demographic_headers = ["timestamp", "edad", "sexo", "carrera"]
            
            # 2. Puntuaciones calculadas (variables principales para análisis)
            score_headers = [
                "ApSeg_Total", "ApAns_Total", "ApEvi_Total", "ApDes_Total",  # Apego
                "Maq_Total", "Nar_Total", "Psi_Total",  # Triada
                "ApegoDominante", "TriadaDominante"  # Dominantes
            ]
            
            # 3. Respuestas individuales (variables de respaldo)
            # Generar nombres descriptivos para las preguntas
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
            writer.writerow(headers)
        
        # Preparar fila de datos con el nuevo orden
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
        apego_questions = sorted([k for k in respuestas.keys() if k.startswith(('seg_', 'ans_', 'evit_', 'desorg_'))])
        triada_questions = sorted([k for k in respuestas.keys() if k.startswith(('maq_', 'nar_', 'psi_'))])
        response_data = [int(respuestas.get(q, 0)) for q in (apego_questions + triada_questions)]
        
        row_data = demographic_data + score_data + response_data
        
        writer.writerow(row_data)
    
    # 8) Renderizar el template con ambos diccionarios
    return render_template(
        "result.html",
        interpretacion=resultado_numerico,
        interpretacion_texto=resultado_textual
    )

if __name__ == "__main__":
    app.run(debug=True)