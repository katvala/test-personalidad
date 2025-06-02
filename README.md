# Test de Personalidad - Sistema de Evaluación Psicológica

Sistema web para administrar tests de personalidad basados en escalas de apego (CaMiR) y triada oscura (SD3), con almacenamiento seguro en Google Drive.

## 🚀 Características

- **Evaluación Dual**: Escalas de apego (CaMiR) y triada oscura (SD3)
- **Almacenamiento Seguro**: Subida automática a Google Drive privado
- **Respaldo Local**: Copia de seguridad en el servidor
- **Análisis Optimizado**: CSV estructurado para JASP/SPSS
- **Interfaz Intuitiva**: Diseño responsivo y fácil de usar

## 📋 Requisitos

- Python 3.8+
- Cuenta de Google Cloud Platform
- Google Drive API habilitada

## ⚙️ Instalación Rápida

```bash
# 1. Clonar/descargar el proyecto
cd test-personalidad

# 2. Ejecutar script de configuración
./run.sh
```

El script `run.sh` se encarga automáticamente de:

- Crear el entorno virtual
- Instalar dependencias
- Configurar archivos necesarios
- Iniciar la aplicación

## 🔧 Configuración Manual

### 1. Entorno Virtual

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Google Drive

1. **Sigue la guía detallada**: [SETUP_GOOGLE_DRIVE.md](SETUP_GOOGLE_DRIVE.md)
2. **Coloca las credenciales**: `config/credentials.json`
3. **Configura variables**: Edita `.env` con tus valores

### 3. Verificar Configuración

```bash
# Probar conexión con Google Drive
python test_config.py
```

## 🏃‍♂️ Uso

### Iniciar Aplicación

```bash
# Método 1: Script automatizado (recomendado)
./run.sh

# Método 2: Manual
source venv/bin/activate
python app.py
```

### Acceso

1. Abre tu navegador en: `http://localhost:5000`
2. Completa el formulario de evaluación
3. Los resultados se guardan automáticamente en Google Drive

## 📊 Estructura de Datos

### Archivo CSV Generado

```
timestamp,edad,sexo,carrera,ApSeg_Total,ApAns_Total,ApEvi_Total,ApDes_Total,Maq_Total,Nar_Total,Psi_Total,ApegoDominante,TriadaDominante,ApSeg_P1,ApSeg_P2,...
```

**Variables Principales:**

- `ApSeg_Total`, `ApAns_Total`, `ApEvi_Total`, `ApDes_Total`: Puntuaciones de apego
- `Maq_Total`, `Nar_Total`, `Psi_Total`: Puntuaciones de triada oscura
- `ApegoDominante`, `TriadaDominante`: Estilos dominantes

**Variables de Respaldo:**

- `ApSeg_P1`, `ApSeg_P2`, etc.: Respuestas individuales por ítem

## 🔒 Seguridad

### Archivos Protegidos (no se suben a git)

- `config/credentials.json`: Credenciales de Google
- `.env`: Variables de entorno
- `data/respuestas.csv`: Datos locales sensibles

### Acceso a Datos

- Solo tu cuenta y la cuenta de servicio tienen acceso
- Archivos almacenados en carpeta privada de Google Drive
- URLs de archivos no son públicas

## 📁 Estructura del Proyecto

```
test-personalidad/
├── 📄 app.py                    # Aplicación Flask principal
├── 📄 google_drive.py           # Utilidades de Google Drive
├── 📄 utils.py                  # Funciones de cálculo psicológico
├── 📄 requirements.txt          # Dependencias Python
├── 📄 .env                      # Variables de entorno (crear)
├── 📄 run.sh                    # Script de ejecución
├── 📄 test_config.py            # Script de prueba
├── 📁 config/
│   └── 📄 credentials.json      # Credenciales Google (obtener)
├── 📁 data/                     # Respaldos locales
├── 📁 templates/                # Plantillas HTML
│   ├── 📄 index.html
│   ├── 📄 form.html
│   └── 📄 result.html
└── 📁 static/
    └── 📄 style.css            # Estilos CSS
```

## 🛠️ Solución de Problemas

### Error de Importación

```bash
# Asegúrate de estar en el entorno virtual
source venv/bin/activate
pip install -r requirements.txt
```

### Error de Google Drive

```bash
# Ejecutar diagnóstico
python test_config.py
```

### Puerto en Uso

```bash
# Cambiar puerto en app.py (línea final)
app.run(debug=True, port=5001)
```

## 🔬 Para Investigadores

### Análisis de Datos

Los archivos CSV están optimizados para:

- **JASP**: Importación directa con variables etiquetadas
- **SPSS**: Formato compatible con sintaxis estándar
- **R**: Estructura tidy para análisis estadístico

### Variables Calculadas

**Apego (CaMiR)**:

- Seguro, Ansioso, Evitativo, Desorganizado
- Promedio de ítems por escala

**Triada Oscura (SD3)**:

- Maquiavelismo, Narcisismo, Psicopatía
- Promedio de ítems por escala

## 📞 Soporte

Para problemas técnicos:

1. Consulta [SETUP_GOOGLE_DRIVE.md](SETUP_GOOGLE_DRIVE.md)
2. Ejecuta `python test_config.py` para diagnóstico
3. Revisa los logs en la consola

## 📄 Licencia

[Ver LICENSE](LICENSE)

---

**Desarrollado para investigación en psicología** 🧠✨
