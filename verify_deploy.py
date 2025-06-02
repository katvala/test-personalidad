#!/usr/bin/env python3
import os
import secrets

print("🔍 Verificando archivos para deployment...")
files = ['app.py', 'wsgi.py', 'requirements.txt', 'Procfile']
for f in files:
    print(f"✅ {f}" if os.path.exists(f) else f"❌ {f}")

print("\n🎯 Clave secreta para FLASK_SECRET_KEY:")
print(f"FLASK_SECRET_KEY={secrets.token_urlsafe(32)}")
print("\n✅ Listo para deployment!")
