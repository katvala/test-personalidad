#!/usr/bin/env python3
"""
Script de verificación para deployment
"""
import os
import sys

def check_deployment():
    """Verifica que todos los archivos necesarios estén presentes"""
    print("🔍 Verificando archivos para deployment...")
    
    required_files = [
        'app.py',
        'wsgi.py', 
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        'utils.py',
        'templates/index.html',
        'templates/form.html',
        'templates/result.html',
        'templates/result_pdf.html'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            print(f"✅ {file}")
    
    if missing_files:
        print(f"\n❌ Archivos faltantes: {missing_files}")
        return False
    
    print("\n📦 Verificando dependencias...")
    try:
        import flask
        print(f"✅ Flask {flask.__version__}")
    except ImportError:
        print("❌ Flask no encontrado")
        return False
    
    try:
        import weasyprint
        print(f"✅ WeasyPrint disponible")
    except ImportError:
        print("⚠️ WeasyPrint no encontrado (se instalará en deployment)")
    
    try:
        import gunicorn
        print(f"✅ Gunicorn disponible")
    except ImportError:
        print("❌ Gunicorn no encontrado")
        return False
    
    print("\n🔧 Verificando configuración...")
    
    # Check environment variables
    secret_key = os.getenv('FLASK_SECRET_KEY')
    if secret_key:
        print("✅ FLASK_SECRET_KEY configurada")
    else:
        print("⚠️ FLASK_SECRET_KEY no configurada (usar en deployment)")
    
    print("\n🎯 URLs de deployment sugeridas:")
    print("- Render: https://render.com")
    print("- Railway: https://railway.app") 
    print("- Vercel: https://vercel.com")
    
    print("\n✅ Listo para deployment!")
    return True

if __name__ == "__main__":
    success = check_deployment()
    sys.exit(0 if success else 1)
