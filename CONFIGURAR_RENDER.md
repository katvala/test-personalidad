# 🔧 Configuración de Google Drive para Render

## Problema Identificado
En Render (y otros servicios cloud), el archivo `config/credentials.json` no está disponible porque:
1. Los archivos locales no se suben al servidor
2. Las credenciales no deben estar en el repositorio por seguridad

## Solución: Variables de Entorno

### Opción 1: Subir JSON completo (Recomendado)

1. **Obtén tu archivo de credenciales**:
   ```bash
   cat config/credentials.json
   ```

2. **Copia todo el contenido JSON**

3. **En Render Dashboard**:
   - Ve a tu servicio
   - Settings → Environment
   - Agrega nueva variable:
     ```
     Nombre: GOOGLE_DRIVE_CREDENTIALS
     Valor: {todo-el-json-de-credenciales}
     ```

### Opción 2: Credenciales individuales

Si prefieres no subir el JSON completo, puedes usar variables individuales:

```bash
GOOGLE_CLIENT_EMAIL=tu-email@proyecto.iam.gserviceaccount.com
GOOGLE_PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\ntu-clave-privata\n-----END PRIVATE KEY-----
GOOGLE_DRIVE_FOLDER_ID=1TQAskPqud8VAhpJggCeAnNTE9WRXubRg
```

### Verificar Configuración

Después de configurar las variables, revisa los logs de Render:
- Settings → Logs
- Busca mensajes como:
  ```
  ✅ Google Drive Manager inicializado
  ✅ Conexión con Google Drive verificada
  ```

### Variables Requeridas

```
GOOGLE_DRIVE_FOLDER_ID=1TQAskPqud8VAhpJggCeAnNTE9WRXubRg
GOOGLE_DRIVE_CREDENTIALS={el-json-completo}
FLASK_SECRET_KEY=tu-clave-secreta
```

## Alternativa: Funcionar sin Google Drive

Si no quieres configurar Google Drive, la aplicación funciona perfectamente sin él:
- Los datos se procesan normalmente
- Los PDFs se generan
- Solo no hay backup en la nube (lo cual está bien para testing)

## Logs de Diagnóstico

La aplicación ahora incluye logs detallados que te dirán exactamente qué está pasando:

```
🔧 Configurando Google Drive...
📁 Google Drive no configurado, usando solo almacenamiento local
💾 Procesando guardado de datos...
📊 RESUMEN DE GUARDADO:
   ☁️ Google Drive: ❌ Falló
   💾 Local: ✅ Guardado
⚠️ NOTA: En producción el almacenamiento local es efímero
```
