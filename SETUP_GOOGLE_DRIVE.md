# Configuración de Google Drive para el Test de Personalidad

## Pasos para configurar Google Drive

### 1. Crear proyecto en Google Cloud Console

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuevo proyecto o selecciona uno existente
3. En el panel de navegación, ve a "APIs y servicios" > "Biblioteca"
4. Busca "Google Drive API" y habilítala

### 2. Crear credenciales de cuenta de servicio

1. Ve a "APIs y servicios" > "Credenciales"
2. Haz clic en "Crear credenciales" > "Cuenta de servicio"
3. Completa el formulario:
   - Nombre: `test-personalidad-service`
   - Descripción: `Cuenta de servicio para subir archivos CSV del test`
4. Haz clic en "Crear y continuar"
5. Omite los pasos opcionales y haz clic en "Listo"

### 3. Generar clave JSON

1. En la página de credenciales, encuentra tu cuenta de servicio
2. Haz clic en el ícono de lápiz (editar)
3. Ve a la pestaña "Claves"
4. Haz clic en "Agregar clave" > "Crear nueva clave"
5. Selecciona "JSON" y haz clic en "Crear"
6. Guarda el archivo descargado como `credentials.json` en la carpeta `config/`

### 4. Crear carpeta en Google Drive

1. Ve a [Google Drive](https://drive.google.com/)
2. Crea una nueva carpeta llamada "Test Personalidad Datos"
3. Haz clic derecho en la carpeta > "Compartir"
4. Agrega la dirección de email de tu cuenta de servicio (está en el archivo credentials.json)
5. Dale permisos de "Editor"
6. Copia el ID de la carpeta desde la URL (la parte después de `/folders/`)

### 5. Configurar variables de entorno

Edita el archivo `.env` con los valores correctos:

```env
# Google Drive Configuration
GOOGLE_CREDENTIALS_PATH=config/credentials.json
GOOGLE_DRIVE_FOLDER_ID=tu_id_de_carpeta_aqui

# Flask Configuration
FLASK_SECRET_KEY=tu_clave_secreta_muy_segura_aqui
```

### 6. Probar la configuración

```bash
# Activar el entorno virtual
source venv/bin/activate

# Ejecutar la aplicación
python app.py
```

## Estructura de archivos

```
test-personalidad/
├── config/
│   └── credentials.json          # Credenciales de Google (NO subir a git)
├── venv/                         # Entorno virtual (NO subir a git)
├── .env                         # Variables de entorno (NO subir a git)
├── .gitignore                   # Configurado para excluir archivos sensibles
├── google_drive.py              # Utilidades de Google Drive
├── app.py                       # Aplicación principal (actualizada)
└── requirements.txt             # Dependencias actualizadas
```

## Seguridad

- ✅ El archivo `credentials.json` está en `.gitignore`
- ✅ El archivo `.env` está en `.gitignore`
- ✅ Los archivos CSV locales están en `.gitignore`
- ✅ Se usa cuenta de servicio (más segura que OAuth)

## Características

- 📤 **Subida automática**: Los CSV se suben automáticamente a Google Drive
- 💾 **Respaldo local**: Se guarda una copia local como respaldo
- 🔒 **Acceso privado**: Solo tú y la cuenta de servicio tienen acceso
- 📊 **Estructura optimizada**: CSV listos para análisis en JASP/SPSS
- 🚀 **Escalable**: Funciona con Google Drive's free tier

## Troubleshooting

### Error de autenticación

- Verifica que el archivo `credentials.json` exista en `config/`
- Revisa que el ID de carpeta sea correcto en `.env`
- Asegúrate de haber compartido la carpeta con la cuenta de servicio

### Error de permisos

- La cuenta de servicio debe tener permisos de "Editor" en la carpeta
- Verifica que la Google Drive API esté habilitada

### Archivos no aparecen

- Los archivos se suben a la carpeta específica configurada
- Revisa la consola para mensajes de éxito/error
