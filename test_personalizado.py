#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de prueba para la nueva función generate_personalized_result
"""

from utils import generate_personalized_result
import json

# Datos de prueba simulando respuestas de usuario
# Simulamos un perfil ansioso-evitativo (combinación)
respuestas_test_combinacion = {
    # Apego Ansioso alto
    'ans_1': '4',  # Preocupado por causar pena
    'ans_2': '5',  # No se concentra si seres queridos tienen problemas
    'ans_3': '4',  # No superaría muerte de ser querido
    'ans_4': '4',  # No se siente bien alejándose
    'ans_5': '4',  # Separación momentánea da inquietud
    'ans_6': '4',  # Preocupado sin razón por salud
    
    # Apego Evitativo alto también
    'evit_1': '4',  # Detesta depender de otros
    'evit_2': '4',  # Solo cuenta consigo mismo
    'evit_3': '3',  # Difícil tomar decisiones en familia
    'evit_4': '4',  # Padres no notaron necesidad de vida propia
    'evit_5': '3',  # Padres dieron demasiada libertad
    'evit_6': '3',  # Padres dejaban hacer lo que quería
    'evit_7': '4',  # Nunca somos suficientemente buenos
    'evit_8': '3',  # Padres controlaban todo
    'evit_9': '3',  # Es importante que niño aprenda a obedecer
    
    # Apego Seguro bajo
    'seg_1': '2',
    'seg_2': '2', 
    'seg_3': '2',
    'seg_4': '2',
    'seg_5': '2',
    'seg_6': '2',
    
    # Apego Desorganizado moderado
    'desorg_1': '3',
    'desorg_2': '3',
    'desorg_3': '3',
    'desorg_4': '2',
    'desorg_5': '3',
    'desorg_6': '3',
    'desorg_7': '3',
    'desorg_8': '2',
    'desorg_9': '3',
    
    # Triada Oscura baja-moderada
    'maq_1': '2', 'maq_2': '2', 'maq_3': '2', 'maq_4': '2', 'maq_5': '2', 
    'maq_6': '2', 'maq_7': '2', 'maq_8': '2', 'maq_9': '2',
    
    'nar_1': '3', 'nar_2': '2', 'nar_3': '2', 'nar_4': '3', 'nar_5': '3',
    'nar_6': '2', 'nar_7': '2', 'nar_8': '2', 'nar_9': '3',
    
    'psi_1': '2', 'psi_2': '2', 'psi_3': '1', 'psi_4': '2', 'psi_5': '1',
    'psi_6': '2', 'psi_7': '2', 'psi_8': '2', 'psi_9': '1'
}

def test_nueva_funcion():
    print("🧪 Probando nueva función generate_personalized_result")
    print("=" * 60)
    
    try:
        resultado = generate_personalized_result(respuestas_test_combinacion)
        
        print("✅ Función executada exitosamente!")
        print("\n📊 RESULTADO PERSONALIZADO:")
        print("=" * 40)
        
        for clave, valor in resultado.items():
            if clave == "Tus Puntuaciones":
                print(f"\n🔢 {clave}:")
                for categoria, puntuaciones in valor.items():
                    print(f"  📈 {categoria}:")
                    for nombre, punt in puntuaciones.items():
                        print(f"    • {nombre}: {punt}/5")
            else:
                print(f"\n📝 {clave}:")
                if isinstance(valor, str):
                    # Limitar longitud para legibilidad
                    texto = valor[:200] + "..." if len(valor) > 200 else valor
                    print(f"   {texto}")
                else:
                    print(f"   {valor}")
        
        print("\n" + "=" * 60)
        print("✅ Prueba completada exitosamente!")
        
        # Verificar que se detectó combinación
        estilo_apego = resultado.get('Estilo de Apego', '')
        if 'Ansioso-Evitativo' in estilo_apego or ('Ansioso' in estilo_apego and 'Evitativo' in estilo_apego):
            print("🎯 ¡Combinación detectada correctamente!")
        else:
            print(f"⚠️  Estilo detectado: {estilo_apego}")
            
    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    test_nueva_funcion()
