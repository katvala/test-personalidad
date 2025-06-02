#!/usr/bin/env python3
"""
Generador de clave secreta para Flask
"""
import secrets
import string

def generate_secret_key(length=32):
    """Genera una clave secreta segura"""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print("🔐 Clave secreta generada para FLASK_SECRET_KEY:")
    print(f"FLASK_SECRET_KEY={secret_key}")
    print("\n💡 Copia esta clave para usar en las variables de entorno del deploy")
