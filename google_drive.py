"""
Utilidades para Google Drive
"""
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload
from io import BytesIO
import csv
from dotenv import load_dotenv
import json

load_dotenv()

class GoogleDriveManager:
    def __init__(self):
        # Usar GOOGLE_CREDENTIALS_JSON (Render) o GOOGLE_CREDENTIALS_PATH (local)
        self.credentials_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
        self.credentials_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
        self.folder_id = os.getenv("GOOGLE_DRIVE_FOLDER_ID")
        self.service = None
        self._authenticate()
    
    def _authenticate(self):
        """Autenticar con Google Drive usando cuenta de servicio"""
        try:
            if self.credentials_json:
                creds_dict = json.loads(self.credentials_json)
                creds = service_account.Credentials.from_service_account_info(
                    creds_dict,
                    scopes=['https://www.googleapis.com/auth/drive.file']
                )
            elif self.credentials_path:
                creds = service_account.Credentials.from_service_account_file(
                    self.credentials_path,
                    scopes=['https://www.googleapis.com/auth/drive.file']
                )
            else:
                raise ValueError("No se encontró GOOGLE_CREDENTIALS_JSON ni GOOGLE_CREDENTIALS_PATH")
            self.service = build('drive', 'v3', credentials=creds)
            print("✅ Autenticación con Google Drive exitosa")
        except Exception as e:
            print(f"❌ Error en autenticación con Google Drive: {e}")
            self.service = None
    
    def upload_csv(self, csv_data, filename):
        """
        Sube datos CSV a Google Drive
        
        Args:
            csv_data: Lista de listas con los datos del CSV
            filename: Nombre del archivo a crear
            
        Returns:
            str: ID del archivo subido o None si hay error
        """
        if not self.service:
            print("❌ No hay conexión con Google Drive")
            return None
            
        try:
            # Crear CSV en memoria
            csv_buffer = BytesIO()
            csv_content = ""
            
            # Convertir datos a string CSV
            for row in csv_data:
                csv_content += ",".join([f'"{str(cell)}"' for cell in row]) + "\n"
            
            csv_buffer.write(csv_content.encode('utf-8'))
            csv_buffer.seek(0)
            
            # Metadata del archivo
            file_metadata = {
                'name': filename,
                'parents': [self.folder_id] if self.folder_id else []
            }
            
            # Media del archivo
            media = MediaIoBaseUpload(
                csv_buffer,
                mimetype='text/csv',
                resumable=True
            )
            
            # Subir archivo
            file = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id,name,webViewLink'
            ).execute()
            
            print(f"✅ Archivo '{filename}' subido exitosamente")
            print(f"📄 ID: {file.get('id')}")
            print(f"🔗 Link: {file.get('webViewLink')}")
            
            return file.get('id')
            
        except HttpError as error:
            print(f"❌ Error HTTP al subir archivo: {error}")
            return None
        except Exception as error:
            print(f"❌ Error general al subir archivo: {error}")
            return None
    
    def check_connection(self):
        """Verificar si la conexión con Google Drive funciona"""
        if not self.service:
            return False
            
        try:
            # Intentar listar archivos como prueba
            results = self.service.files().list(pageSize=1).execute()
            print("✅ Conexión con Google Drive verificada")
            return True
        except Exception as e:
            print(f"❌ Error en conexión con Google Drive: {e}")
            return False
