# -*- coding: utf-8 -*-

OPCIONES_RESPUESTA = [
    (1, "Totalmente en desacuerdo"),
    (2, "En desacuerdo"),
    (3, "Neutral"),
    (4, "De acuerdo"),
    (5, "Totalmente de acuerdo")
]

# 1) LISTAS DE PREGUNTAS CaMir-R y SD3-F
LISTA_CaMiR = [
    # 1° bloque
    ("seg_1",    "Puedo contar con mis seres queridos para encontrar consuelo."),
    ("ans_1",    "Siempre estoy preocupado(a) por la pena que puedo causar a mis seres queridos al dejarlos."),
    ("evit_1",   "Detesto el sentimiento de depender de los demás."),
    ("desorg_1", "Las amenazas de separación, traslado o ruptura de lazos familiares son parte de mis recuerdos infantiles."),

    # 2° bloque
    ("seg_2",    "Cuando era niño(a), sabía que encontraría consuelo en mis seres queridos."),
    ("ans_2",    "No puedo concentrarme sabiendo que uno de mis seres queridos tiene problemas."),
    ("evit_2",   "Solo cuento conmigo mismo para resolver mis problemas."),
    ("desorg_2", "Mis padres eran incapaces de tener autoridad cuando era necesario."),

    # 3° bloque
    ("seg_3",    "Mis seres queridos siempre me han dado lo mejor de sí mismos."),
    ("ans_3",    "Siento que nunca superaría la muerte de uno de mis seres queridos."),
    ("evit_3",   "En mi niñez, era difícil tomar decisiones en familia."),
    ("desorg_3", "Las relaciones con mis seres queridos durante mi niñez fueron, en general, positivas."),

    # 4° bloque
    ("seg_4",    "Cuando era niño(a), recibí suficiente cariño de mis seres queridos como para no buscarlo en otra parte."),
    ("ans_4",    "Cuando me alejo de mis seres queridos, no me siento bien conmigo mismo."),
    ("evit_4",   "Mis padres no se dieron cuenta de que yo necesitaba tener vida propia."),
    ("desorg_4", "En mi niñez, tuve que enfrentarme a la violencia de un ser querido."),

    # 5° bloque
    ("seg_5",    "Siento confianza en mis seres queridos."),
    ("ans_5",    "La idea de una separación momentánea con un ser querido me deja una sensación de inquietud."),
    ("evit_5",   "Mis padres me dieron demasiada libertad para hacer todo lo que yo quería."),
    ("desorg_5", "Cuando era niño(a), a menudo mis seres queridos se mostraban impacientes e irritables."),

    # 6° bloque
    ("seg_6",    "Mis seres queridos disfrutaban compartir su tiempo conmigo."),
    ("ans_6",    "Me siento preocupado(a), sin razón, por la salud de mis seres queridos."),
    ("evit_6",   "Mis padres o cuidadores solían dejarme hacer lo que yo quería, sin muchas reglas o límites."),
    ("desorg_6", "De adolescente, nadie de mi entorno comprendía del todo mis preocupaciones."),

    # Bloque final de evitativo + desorganizado (items 7, 8 y 9)
    ("evit_7",   "He comprendido que nunca somos lo suficientemente buenos para los padres."),
    ("desorg_7", "Cuando era niño(a), había peleas insoportables en casa."),

    ("evit_8",   "Mis padres no podían evitar controlarlo todo: apariencia, notas, amigos."),
    ("desorg_8", "Se preocuparon tanto por mi salud y mi seguridad que me sentía aprisionado(a)."),

    ("evit_9",   "Es importante que el niño aprenda a obedecer."),
    ("desorg_9", "Mis padres no se dieron cuenta de que yo necesitaba tener vida propia."),
]

LISTA_SD3 = [
    ("maq_1", "Me gusta usar trampas para conseguir lo que quiero."),
    ("nar_1", "Sin mí, las reuniones tienden a ser aburridas."),
    ("psi_1", "Me gusta vengarme de las autoridades."),
    ("maq_2", "Cueste lo que cueste, debes tener a la gente importante de tu lado."),
    ("nar_2", "Sé que soy especial porque todo el mundo me lo dice una y otra vez."),
    ("psi_2", "Evito situaciones peligrosas."),
    ("maq_3", "Evito el conflicto directo con otros porque me pueden ser de utilidad en el futuro."),
    ("nar_3", "Se me ha comparado con gente famosa."),
    ("psi_3", "La venganza tiene que ser rápida y desagradable."),
    ("maq_4", "Es importante saber cosas de la gente que puedas usar en su contra en el futuro."),
    ("nar_4", "Me siento seguro/a en mis habilidades sociales."),
    ("psi_4", "La gente dice a menudo que estoy fuera de control."),
    ("maq_5", "Debes esperar el momento oportuno para vengarte de la gente."),
    ("nar_5", "Me encanta que la gente me admire."),
    ("psi_5", "Es cierto que puedo ser cruel con los demás."),
    ("maq_6", "Asegúrate de que tus planes te beneficien solo a ti y no a los demás."),
    ("nar_6", "Me considero muy atractivo/a."),
    ("psi_6", "La gente que se mete conmigo siempre lo lamenta."),
    ("maq_7", "La mayoría de la gente puede ser manipulada."),
    ("nar_7", "Mis padres me criaron para creer que soy especial."),
    ("psi_7", "Disfruto teniendo relaciones sexuales con personas que apenas conozco."),
    ("maq_8", "La gente me ve como un líder natural."),
    ("nar_8", "La gente dice que tengo cualidades únicas."),
    ("psi_8", "Diría lo que sea para conseguir lo que quiero."),
    ("maq_9", "Me gusta conocer gente importante."),
    ("nar_9", "Cuando hablo, suelo ser el centro de atención."),
    ("psi_9", "Me siento insensible ante el sufrimiento ajeno."),
]

def interpretar_respuestas(respuestas):
    """
    - 'respuestas' es un dict con pares { "seg_1": "4", "seg_2": "2", ..., "psi_9": "5" }
    - Calcula promedio de cada dimensión, añade 'Estilo de Apego Dominante' y 'Triada Dominante'.
    - Asegura que los valores sean correctamente formateados para análisis.
    """
    def promedio(prefijos):
        vals = []
        for clave, valor in respuestas.items():
            for p in prefijos:
                if clave.startswith(p):
                    try:
                        vals.append(int(valor))
                    except:
                        pass
        return round(sum(vals) / len(vals), 2) if vals else 0

    resultado = {
        "Maquiavelismo": promedio(["maq_"]),
        "Narcisismo": promedio(["nar_"]),
        "Psicopatía": promedio(["psi_"]),
        "Apego Seguro": promedio(["seg_"]),
        "Apego Ansioso": promedio(["ans_"]),
        "Apego Evitativo": promedio(["evit_"]),
        "Apego Desorganizado": promedio(["desorg_"]),
    }

    # Estilo de apego dominante
    estilos_apego = {
        k: resultado[k]
        for k in ["Apego Seguro", "Apego Ansioso", "Apego Evitativo", "Apego Desorganizado"]
    }
    resultado["Estilo de Apego Dominante"] = max(estilos_apego, key=lambda k: estilos_apego[k])

    # Rasgo oscuro dominante
    rasgos_oscuros = {
        k: resultado[k] for k in ["Maquiavelismo", "Narcisismo", "Psicopatía"]
    }
    resultado["Triada Dominante"] = max(rasgos_oscuros, key=lambda k: rasgos_oscuros[k])

    return resultado

def interpretar_textos(resultado):
    """
    Recibe el dict con valores numéricos (incluye dominantes) y devuelve
    un dict con interpretaciones detalladas para cada rasgo, más los dominantes y mensaje final.
    También incluye una descripción general de la personalidad.
    """
    textos = {}
    umbral_alto = 3.5
    umbral_moderado = 2.5
    
    # TRIADA OSCURA - Clasificar por niveles con lógica personalizada
    for rasgo in ["Maquiavelismo", "Narcisismo", "Psicopatía"]:
        valor = resultado.get(rasgo, 0)

        # Valores altos
        if valor > umbral_alto:
            if rasgo == "Maquiavelismo":
                textos["Maquiavelismo Elevado"] = (
                    "Tienes un nivel elevado de maquiavelismo: podrías tender a manipular a otros estratégicamente "
                    "y usar tácticas para obtener lo que quieres. Reflexiona si estas actitudes benefician a largo "
                    "plazo o socavan la confianza en tus relaciones. Sugerencia: practica empatía activa antes de actuar "
                    "y busca formas de negociación donde ambas partes ganen."
                )
            elif rasgo == "Narcisismo":
                textos["Narcisismo Elevado"] = (
                    "Tienes un nivel elevado de narcisismo: tiendes a buscar admiración y puedes centrarte mucho en tus "
                    "propias necesidades y logros. Valoras ser reconocido y destacar entre los demás. Sugerencia: equilibra "
                    "tu autoestima reconociendo y valorando genuinamente los logros ajenos, y practica la escucha activa."
                )
            elif rasgo == "Psicopatía":
                textos["Psicopatía Elevada"] = (
                    "Tienes un nivel elevado de rasgos de psicopatía: podrías mostrar cierta frialdad emocional, impulsividad "
                    "o dificultad para considerar las consecuencias de tus acciones. Sugerencia: trabaja en identificar y "
                    "gestionar tus emociones con técnicas como meditación, respiración consciente o terapia psicológica."
                )
        # Valores intermedios (personalización, sin clasificaciones explícitas)
        elif valor > umbral_moderado:
            if 2.5 < valor < 3.5:
                if rasgo == "Maquiavelismo":
                    textos["Maquiavelismo"] = (
                        "Tu puntuación en maquiavelismo se encuentra en un rango intermedio. Esto sugiere que, aunque puedes "
                        "ser capaz de pensar estratégicamente o proteger tus intereses en situaciones sociales, no sueles recurrir "
                        "habitualmente a la manipulación. Mantener esta conciencia puede ayudarte a establecer relaciones basadas en la confianza."
                    )
                elif rasgo == "Narcisismo":
                    textos["Narcisismo"] = (
                        "Tu puntuación en narcisismo es intermedia. Puedes tener confianza en ti mismo y disfrutar del reconocimiento, "
                        "pero sin que esto domine tus relaciones. Este equilibrio puede ser útil para alcanzar metas y mantener relaciones saludables."
                    )
                elif rasgo == "Psicopatía":
                    textos["Psicopatía"] = (
                        "Tu puntuación en psicopatía es intermedia. Puedes mostrar cierta capacidad para tomar decisiones objetivas "
                        "y actuar con firmeza, pero sin perder de vista las consecuencias emocionales para ti y para los demás."
                    )
            else:
                # Para valores moderados fuera de 2.5-3.5, mantener el texto general sin clasificaciones
                if rasgo == "Maquiavelismo":
                    textos["Maquiavelismo"] = (
                        "Muestras algunos rasgos de maquiavelismo: puedes usar estrategias para influir en otros en ciertas situaciones, "
                        "pero generalmente mantienes tus valores y la ética en tus interacciones."
                    )
                elif rasgo == "Narcisismo":
                    textos["Narcisismo"] = (
                        "Presentas algunos rasgos de narcisismo: valoras el reconocimiento y tienes confianza en ti mismo, "
                        "lo que puede ser positivo para conseguir metas, siempre que no desatiendas las necesidades de los demás."
                    )
                elif rasgo == "Psicopatía":
                    textos["Psicopatía"] = (
                        "Muestras algunos rasgos asociados a psicopatía: ocasionalmente puedes actuar por impulso "
                        "o mostrar cierta frialdad en situaciones específicas. Es importante que desarrolles conciencia "
                        "sobre cómo tus acciones afectan a otros y practiques la empatía activamente."
                    )
        # Valores bajos
        else:
            if rasgo == "Maquiavelismo":
                textos["Maquiavelismo Bajo"] = (
                    "Presentas un nivel bajo de maquiavelismo: tiendes a ser directo y honesto en tus interacciones, "
                    "priorizando la transparencia sobre la manipulación estratégica. Esto favorece relaciones basadas "
                    "en la confianza y autenticidad."
                )
            elif rasgo == "Narcisismo":
                textos["Narcisismo Bajo"] = (
                    "Muestras un nivel bajo de narcisismo: no buscas constantemente admiración y puedes priorizar las "
                    "necesidades de otros sobre el reconocimiento personal. Esto facilita relaciones más equilibradas, "
                    "aunque a veces podrías beneficiarte de afirmar más tus propias necesidades."
                )
            elif rasgo == "Psicopatía":
                textos["Psicopatía Baja"] = (
                    "Presentas un nivel bajo de rasgos de psicopatía: generalmente consideras las consecuencias de tus "
                    "acciones y muestras empatía hacia los demás. Tiendes a ser reflexivo antes de actuar y consideras "
                    "el impacto emocional de tus decisiones en otras personas."
                )
    
    # ESTILOS DE APEGO - Clasificar por niveles
    # Apego seguro siempre se reporta
    valor_apego_seguro = resultado.get("Apego Seguro", 0)
    if valor_apego_seguro > umbral_alto:
        textos["Apego Seguro Elevado"] = (
            "Muestras un nivel elevado de apego seguro: te sientes cómodo tanto con la intimidad emocional como con "
            "la autonomía. Confías en los demás y sabes que estarán ahí cuando los necesitas, lo que te permite "
            "formar relaciones saludables y estables. Este es un patrón muy positivo que favorece tu bienestar."
        )
    elif valor_apego_seguro > umbral_moderado:
        textos["Apego Seguro"] = (
            "Tu puntuación en apego seguro es intermedia. Generalmente confías en los demás y te sientes cómodo "
            "en las relaciones cercanas, aunque ocasionalmente puedes experimentar inseguridades. Tu estilo de vinculación "
            "te permite mantener relaciones mayormente saludables."
        )
    
    # Estilos de apego inseguros
    for estilo in ["Apego Ansioso", "Apego Evitativo", "Apego Desorganizado"]:
        valor = resultado.get(estilo, 0)
        # Valores altos
        if valor > umbral_alto:
            if estilo == "Apego Ansioso":
                textos["Apego Ansioso Elevado"] = (
                    "Presentas un nivel elevado de apego ansioso: puedes temer perder a tus seres queridos o necesitar "
                    "validación constante en tus relaciones. Esto puede generar preocupación excesiva y búsqueda de "
                    "confirmación. Sugerencia: practica técnicas de autorregulación emocional como mindfulness y "
                    "comunica tus inseguridades de forma asertiva en lugar de indirecta."
                )
            elif estilo == "Apego Evitativo":
                textos["Apego Evitativo Elevado"] = (
                    "Muestras un nivel elevado de apego evitativo: tiendes a evitar la cercanía emocional, valoras mucho "
                    "tu independencia y puedes tener dificultades para confiar plenamente en otros. Sugerencia: intenta "
                    "compartir gradualmente tus sentimientos con personas de confianza y practica la vulnerabilidad en "
                    "situaciones seguras."
                )
            elif estilo == "Apego Desorganizado":
                textos["Apego Desorganizado Elevado"] = (
                    "Presentas un nivel elevado de apego desorganizado: puedes alternar entre buscar cercanía y rechazarla, "
                    "generando confusión en tus relaciones. Esto puede derivarse de experiencias contradictorias en el pasado. "
                    "Sugerencia: llevar un diario emocional y buscar apoyo profesional puede ayudarte a reconocer patrones y "
                    "estabilizar tus vínculos."
                )
        # Valores intermedios (personalización, sin clasificaciones explícitas)
        elif valor > umbral_moderado:
            if 2.5 < valor < 3.5:
                if estilo == "Apego Ansioso":
                    textos["Apego Ansioso"] = (
                        "Tu puntuación en apego ansioso es intermedia. En ciertas situaciones puedes preocuparte por el estado "
                        "de tus relaciones o buscar confirmación de que los demás te valoran. Esto puede ser natural en momentos "
                        "de estrés, aunque generalmente mantienes un equilibrio."
                    )
                elif estilo == "Apego Evitativo":
                    textos["Apego Evitativo"] = (
                        "Tu puntuación en apego evitativo es intermedia. Valoras tu independencia y a veces prefieres mantener "
                        "cierta distancia emocional, aunque puedes formar vínculos cuando te sientes seguro. Encontrar un balance "
                        "entre autonomía y conexión podría beneficiarte."
                    )
                elif estilo == "Apego Desorganizado":
                    textos["Apego Desorganizado"] = (
                        "Tu puntuación en apego desorganizado es intermedia. En ocasiones puedes sentirte confundido sobre cómo "
                        "acercarte a los demás o enviar señales contradictorias en tus relaciones. Reflexionar sobre tus patrones "
                        "de comunicación podría ayudarte a establecer vínculos más claros."
                    )
            else:
                if estilo == "Apego Ansioso":
                    textos["Apego Ansioso"] = (
                        "Muestras algunos rasgos de apego ansioso: en ciertas situaciones puedes preocuparte por el estado "
                        "de tus relaciones o buscar confirmación de que los demás te valoran. Esto puede ser natural en momentos "
                        "de estrés, aunque generalmente mantienes un equilibrio."
                    )
                elif estilo == "Apego Evitativo":
                    textos["Apego Evitativo"] = (
                        "Presentas algunos rasgos de apego evitativo: valoras tu independencia y a veces prefieres mantener "
                        "cierta distancia emocional, aunque puedes formar vínculos cuando te sientes seguro. Encontrar un balance "
                        "entre autonomía y conexión podría beneficiarte."
                    )
                elif estilo == "Apego Desorganizado":
                    textos["Apego Desorganizado"] = (
                        "Muestras algunos rasgos de apego desorganizado: en ocasiones puedes sentirte confundido sobre cómo "
                        "acercarte a los demás o enviar señales contradictorias en tus relaciones. Reflexionar sobre tus patrones "
                        "de comunicación podría ayudarte a establecer vínculos más claros."
                    )
    
    # Si tiene un perfil equilibrado (ninguno alto)
    tiene_altos = any(resultado.get(rasgo, 0) > umbral_alto for rasgo in 
                     ["Maquiavelismo", "Narcisismo", "Psicopatía", 
                      "Apego Ansioso", "Apego Evitativo", "Apego Desorganizado"])
    if not tiene_altos:
        textos["Perfil Equilibrado"] = (
            "¡Felicidades! Tu perfil muestra niveles equilibrados en todas las dimensiones evaluadas. "
            "Esto sugiere que tienes buenas habilidades de autorregulación emocional y relacional, lo que "
            "contribuye positivamente a tu bienestar psicológico y social."
        )

    # Combinaciones de estilos de apego mixtos
    alto_apegos = [k for k in ["Apego Ansioso", "Apego Evitativo", "Apego Desorganizado"] if resultado.get(k, 0) > umbral_alto]
    if "Apego Ansioso" in alto_apegos and "Apego Evitativo" in alto_apegos:
        textos["Apego Mixto (Ansioso + Evitativo)"] = (
            "Tu perfil sugiere una combinación de apego ansioso y evitativo. Esto puede reflejar una tensión interna entre "
            "el deseo profundo de cercanía y la necesidad de protegerte emocionalmente. Es posible que temas el rechazo, "
            "pero al mismo tiempo mantengas una distancia emocional para evitar el dolor. Explorar estas dinámicas puede ayudarte "
            "a construir relaciones más estables y satisfactorias."
        )
    if "Apego Ansioso" in alto_apegos and "Apego Desorganizado" in alto_apegos:
        textos["Apego Mixto (Ansioso + Desorganizado)"] = (
            "Tu perfil revela una combinación de apego ansioso y desorganizado, lo que puede manifestarse en relaciones inestables, "
            "con preocupación por el abandono y comportamientos contradictorios. Reconocer estos patrones es el primer paso para trabajar "
            "hacia vínculos más seguros y satisfactorios."
        )
    if "Apego Evitativo" in alto_apegos and "Apego Desorganizado" in alto_apegos:
        textos["Apego Mixto (Evitativo + Desorganizado)"] = (
            "Tu perfil muestra una mezcla de apego evitativo y desorganizado. Puedes tender a evitar la cercanía y, al mismo tiempo, "
            "experimentar confusión o ambivalencia en tus relaciones. Es útil explorar estos patrones para entender mejor tus necesidades emocionales."
        )
    
    # Descripción general de personalidad
    est_dom = resultado.get("Estilo de Apego Dominante", "")
    triada_dom = resultado.get("Triada Dominante", "")
    
    # Crear descripción personalizada
    descripcion_personalidad = []
    
    # Describir estilo de apego
    if est_dom == "Apego Seguro":
        descripcion_personalidad.append(
            "Tu estilo de apego dominante es seguro, lo que significa que generalmente te sientes cómodo tanto con "
            "la intimidad como con la autonomía en tus relaciones. Tiendes a confiar en los demás y a tener una "
            "visión positiva de ti mismo."
        )
    elif est_dom == "Apego Ansioso":
        descripcion_personalidad.append(
            "Tu estilo de apego dominante es ansioso, lo que puede manifestarse como preocupación por la disponibilidad "
            "de los demás y búsqueda de proximidad y seguridad en tus relaciones. Tiendes a valorar mucho la cercanía emocional."
        )
    elif est_dom == "Apego Evitativo":
        descripcion_personalidad.append(
            "Tu estilo de apego dominante es evitativo, lo que significa que tiendes a valorar tu independencia y "
            "autosuficiencia. Podrías sentirte incómodo con demasiada cercanía emocional y preferir mantener cierta distancia."
        )
    elif est_dom == "Apego Desorganizado":
        descripcion_personalidad.append(
            "Tu estilo de apego dominante es desorganizado, lo que puede reflejarse en patrones inconsistentes en tus "
            "relaciones. A veces puedes buscar cercanía mientras que otras podrías rechazarla, generando cierta ambivalencia."
        )
    
    # Describir triada oscura
    if triada_dom == "Maquiavelismo":
        descripcion_personalidad.append(
            "En cuanto a rasgos de personalidad, destacas en maquiavelismo, lo que sugiere que tienes capacidad para "
            "el pensamiento estratégico y pragmático. Podrías ser hábil para comprender las dinámicas sociales y utilizarlas "
            "a tu favor cuando lo consideras necesario."
        )
    elif triada_dom == "Narcisismo":
        descripcion_personalidad.append(
            "En cuanto a rasgos de personalidad, destacas en narcisismo, lo que puede reflejarse en una buena autoestima, "
            "confianza en tus habilidades y cierta inclinación a buscar reconocimiento por tus logros. Esto puede ser positivo "
            "para alcanzar metas cuando se mantiene en equilibrio."
        )
    elif triada_dom == "Psicopatía":
        descripcion_personalidad.append(
            "En cuanto a rasgos de personalidad, destacas en rasgos asociados a psicopatía, lo que podría manifestarse como "
            "una tendencia a la acción directa, menor preocupación por las convenciones sociales o cierta frialdad al tomar "
            "decisiones. Esto puede ser útil en situaciones que requieren tomar decisiones difíciles."
        )
    
    # Añadir conclusión equilibrada
    descripcion_personalidad.append(
        "Recuerda que estos rasgos existen en un continuo y cada persona tiene una combinación única. Lo importante es "
        "reconocer tus patrones para potenciar tus fortalezas y trabajar en áreas de mejora, buscando relaciones más "
        "satisfactorias y un mayor bienestar personal."
    )
    
    textos["Descripción de tu Personalidad"] = " ".join(descripcion_personalidad)
    
    # Resumen de puntuaciones en formato texto
    puntuaciones_texto = []
    puntuaciones_texto.append("ESTILOS DE APEGO:")
    puntuaciones_texto.append(f"- Apego Seguro: {resultado.get('Apego Seguro', 0)}/5")
    puntuaciones_texto.append(f"- Apego Ansioso: {resultado.get('Apego Ansioso', 0)}/5")
    puntuaciones_texto.append(f"- Apego Evitativo: {resultado.get('Apego Evitativo', 0)}/5")
    puntuaciones_texto.append(f"- Apego Desorganizado: {resultado.get('Apego Desorganizado', 0)}/5")
    puntuaciones_texto.append("\nTRIADA OSCURA:")
    puntuaciones_texto.append(f"- Maquiavelismo: {resultado.get('Maquiavelismo', 0)}/5")
    puntuaciones_texto.append(f"- Narcisismo: {resultado.get('Narcisismo', 0)}/5")
    puntuaciones_texto.append(f"- Psicopatía: {resultado.get('Psicopatía', 0)}/5")
    
    textos["Tus Puntuaciones"] = "\n".join(puntuaciones_texto)
    
    # Siempre incluir Estilo de Apego Dominante
    if est_dom:
        textos["Estilo de Apego Dominante"] = f"Tu estilo de apego dominante es: {est_dom}."

    # Siempre incluir Triada Dominante
    if triada_dom:
        textos["Triada Oscura Dominante"] = f"Tu rasgo oscuro dominante es: {triada_dom}."

        # Interpretación combinada para mezclas específicas
        combinacion = (est_dom, triada_dom)

        if combinacion == ("Apego Evitativo", "Psicopatía"):
            textos["Interpretación Combinada"] = (
                "Tu combinación de apego evitativo con altos rasgos de psicopatía puede reflejar una tendencia a evitar la cercanía emocional, "
                "mientras mantienes una actitud pragmática o incluso fría en tus relaciones. Puedes sentirte más cómodo resolviendo las cosas por tu cuenta "
                "y priorizando la lógica sobre la emoción. Es recomendable explorar formas seguras de conectar con otros sin sentir que pierdes autonomía."
            )
        elif combinacion == ("Apego Ansioso", "Maquiavelismo"):
            textos["Interpretación Combinada"] = (
                "Tu estilo de apego ansioso combinado con maquiavelismo sugiere que puedes experimentar ansiedad en tus vínculos, acompañada de un enfoque estratégico "
                "para asegurar la cercanía o el control en las relaciones. Es importante que examines si tus intentos de conexión se ven influenciados por el temor a ser rechazado "
                "y por la necesidad de tener el control. Trabaja en cultivar relaciones basadas en la confianza mutua, no en el miedo o la manipulación."
            )
        elif combinacion == ("Apego Seguro", "Maquiavelismo"):
            textos["Interpretación Combinada"] = (
                "Aunque tienes una base segura en tus relaciones, el maquiavelismo indica que puedes utilizar estrategias sociales para obtener resultados. "
                "Esto puede ser una ventaja si sabes cuándo actuar con autenticidad y cuándo es útil aplicar un enfoque más racional. Asegúrate de mantener un equilibrio ético."
            )
        elif combinacion == ("Apego Desorganizado", "Psicopatía"):
            textos["Interpretación Combinada"] = (
                "Esta combinación puede reflejar conflictos internos intensos: por un lado, dificultades para estabilizar relaciones (apego desorganizado), "
                "y por otro, una actitud distante o incluso hostil hacia los demás. Considera buscar apoyo emocional o terapéutico para reconocer tus patrones relacionales y su impacto."
            )

    # Mensaje de apoyo final
    textos["Mensaje de Apoyo"] = (
        "Si estos resultados te generan preocupación o dificultan tu bienestar, "
        "te recomendamos visitar la Oficina de Bienestar Estudiantil (OBE) para recibir orientación profesional. "
        "Recuerda que estos resultados son un punto de partida para la autorreflexión y el crecimiento personal."
    )

    return textos
