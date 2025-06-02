"""
Google Drive Manager mejorado para producción
"""
import os
import json
import base64
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload
from io import BytesIO
import csv
from dotenv import load_dotenv

load_dotenv()

class GoogleDriveManager:
    def __init__(self):
        self.folder_id = os.getenv("GOOGLE_DRIVE_FOLDER_ID")
        self.service = None
        print(f"🔍 Inicializando Google Drive Manager...")
        print(f"📁 Folder ID: {self.folder_id}")
        self._authenticate()
    
    def _authenticate(self):
        """Autenticar con Google Drive usando diferentes métodos"""
        try:
            # Método 1: Archivo local (desarrollo)
            credentials_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
            if credentials_path and os.path.exists(credentials_path):
                print(f"🔑 Usando credenciales desde archivo: {credentials_path}")
                creds = service_account.Credentials.from_service_account_file(
                    credentials_path, 
                    scopes=['https://www.googleapis.com/auth/drive.file']
                )
                self.service = build('drive', 'v3', credentials=creds)
                print("✅ Autenticación exitosa (archivo local)")
                return
            
            # Método 2: Variable de entorno con JSON (producción)
            credentials_json = os.getenv("GOOGLE_DRIVE_CREDENTIALS")
            if credentials_json:
                print("🔑 Usando credenciales desde variable de entorno")
                try:
                    # Si está en base64, decodificar
                    if not credentials_json.startswith('{'):
                        credentials_json = base64.b64decode(credentials_json).decode('utf-8')
                    
                    credentials_info = json.loads(credentials_json)
                    creds = service_account.Credentials.from_service_account_info(
                        credentials_info,
                        scopes=['https://www.googleapis.com/auth/drive.file']
                    )
                    self.service = build('drive', 'v3', credentials=creds)
                    print("✅ Autenticación exitosa (variable de entorno)")
                    return
                except Exception as e:
                    print(f"❌ Error al procesar credenciales de variable de entorno: {e}")
            
            # Método 3: Credenciales individuales (alternativa)
            client_email = os.getenv("GOOGLE_CLIENT_EMAIL")
            private_key = os.getenv("GOOGLE_PRIVATE_KEY")
            
            if client_email and private_key:
                print("🔑 Usando credenciales individuales")
                credentials_info = {
                    "type": "service_account",
                    "client_email": client_email,
                    "private_key": private_key.replace('\\n', '\n'),
                    "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID", ""),
                    "client_id": os.getenv("GOOGLE_CLIENT_ID", ""),
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                }
                
                creds = service_account.Credentials.from_service_account_info(
                    credentials_info,
                    scopes=['https://www.googleapis.com/auth/drive.file']
                )
                self.service = build('drive', 'v3', credentials=creds)
                print("✅ Autenticación exitosa (credenciales individuales)")
                return
            
            # No se pudo autenticar
            print("⚠️ No se encontraron credenciales válidas para Google Drive")
            print("📁 La aplicación funcionará sin backup en Google Drive")
            self.service = None
            
        except Exception as e:
            print(f"❌ Error durante autenticación con Google Drive: {e}")
            self.service = None
    
    def is_available(self):
        """Verificar si Google Drive está disponible"""
        return self.service is not None and self.folder_id is not None
    
    def upload_csv(self, csv_data, filename):
        """
        Subir archivo CSV a Google Drive
        
        Args:
            csv_data: Lista de listas con los datos del CSV
            filename: Nombre del archivo
            
        Returns:
            str: ID del archivo subido o None si falló
        """
        if not self.is_available():
            print("⚠️ Google Drive no está disponible")
            return None
        
        try:
            print(f"📤 Intentando subir {filename} a Google Drive...")
            
            # Crear contenido CSV en memoria
            csv_buffer = BytesIO()
            csv_writer = csv.writer(csv_buffer.read().decode().splitlines().__iter__())
            
            # Alternativa más simple
            csv_content = ""
            for row in csv_data:
                csv_content += ",".join([f'"{str(cell)}"' for cell in row]) + "\n"
            
            csv_buffer = BytesIO(csv_content.encode('utf-8'))
            
            # Metadatos del archivo
            file_metadata = {
                'name': filename,
                'parents': [self.folder_id] if self.folder_id else []
            }
            
            # Upload del archivo
            media = MediaIoBaseUpload(
                csv_buffer,
                mimetype='text/csv',
                resumable=True
            )
            
            file = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id,webViewLink'
            ).execute()
            
            file_id = file.get('id')
            file_link = file.get('webViewLink')
            
            print(f"✅ Archivo '{filename}' subido exitosamente")
            print(f"📄 ID: {file_id}")
            print(f"🔗 Link: {file_link}")
            
            return file_id
            
        except HttpError as e:
            print(f"❌ Error HTTP al subir a Google Drive: {e}")
            return None
        except Exception as e:
            print(f"❌ Error inesperado al subir a Google Drive: {e}")
            return None
    
    def test_connection(self):
        """Probar la conexión con Google Drive"""
        if not self.is_available():
            return False, "Google Drive no está configurado"
        
        try:
            # Intentar listar archivos en la carpeta
            results = self.service.files().list(
                q=f"'{self.folder_id}' in parents" if self.folder_id else None,
                pageSize=1,
                fields="files(id, name)"
            ).execute()
            
            print(f"✅ Conexión exitosa con Google Drive")
            if self.folder_id:
                print(f"📁 Carpeta accesible: {self.folder_id}")
            
            return True, "Conexión exitosa"
            
        except Exception as e:
            print(f"❌ Error al probar conexión: {e}")
            return False, str(e)
