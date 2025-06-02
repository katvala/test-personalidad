# 🧠 Test de Personalidad - Guía de Despliegue

## 🚀 Despliegue en Servicios Gratuitos

### Opción 1: Render (Recomendado)

1. **Conectar Repositorio**:
   - Ve a [render.com](https://render.com)
   - Registrate/inicia sesión con GitHub
   - Conecta tu repositorio

2. **Configurar Web Service**:
   - Selecciona "New Web Service"
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn wsgi:app`
   - Instance Type: Free

3. **Variables de Entorno** (opcionales):
   ```
   FLASK_ENV=production
   FLASK_SECRET_KEY=tu-clave-secreta-segura
   GOOGLE_DRIVE_FOLDER_ID=tu-folder-id (opcional)
   ```

### Opción 2: Railway

1. **Conectar Repositorio**:
   - Ve a [railway.app](https://railway.app)
   - Conecta con GitHub
   - Selecciona "Deploy from GitHub repo"

2. **Configuración Automática**:
   - Railway detectará automáticamente el archivo `railway.json`
   - La aplicación se desplegará automáticamente

### Opción 3: Vercel

1. **Conectar Repositorio**:
   - Ve a [vercel.com](https://vercel.com)
   - Importa tu proyecto desde GitHub

2. **Configurar como Serverless**:
   - Framework Preset: Other
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: `.`

## 🔧 Configuración Post-Despliegue

### Variables de Entorno Requeridas:
- `FLASK_SECRET_KEY`: Clave secreta para sesiones
- `FLASK_ENV`: `production` para entorno de producción

### Variables Opcionales (Google Drive):
- `GOOGLE_DRIVE_FOLDER_ID`: ID del folder de Google Drive
- `GOOGLE_DRIVE_CREDENTIALS`: JSON de credenciales (para Railway/Vercel)

## 📊 Funcionalidades

- ✅ **Sin Google Drive**: La aplicación funciona completamente sin configuración adicional
- ✅ **Con Google Drive**: Backup automático de respuestas en la nube
- ✅ **Generación PDF**: Funciona en todos los entornos
- ✅ **Responsive**: Optimizado para móviles y desktop

## 🧪 Prueba Local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar con Gunicorn (simulando producción)
gunicorn wsgi:app

# Ejecutar en desarrollo
python app.py
```

## 🎯 URLs de Prueba

- **Inicio**: `/`
- **Formulario**: `/form`
- **Resultados**: Se genera automáticamente tras envío
- **PDF**: `/descargar_pdf` (después de completar test)

## 🔒 Seguridad

- Las credenciales de Google Drive son opcionales
- La aplicación funciona sin configuración de base de datos
- Todas las dependencias están especificadas y son seguras
- HTTPS automático en todos los servicios gratuitos

---

**Desarrollado con ❤️ usando Flask, Chart.js y WeasyPrint**
