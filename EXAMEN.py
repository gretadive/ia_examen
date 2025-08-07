import random
import streamlit as st

# -------------------------------
# PREGUNTAS POR NIVEL Y TIPO
# -------------------------------

niveles = {
    "básico": [
        {
            "tipo": "opcion",
            "pregunta": "¿Cuál es una ventaja de la evaluación formativa con IA?",
            "opciones": ["A. Castigar errores", "B. Promover la memorización", "C. Dar retroalimentación inmediata", "D. Eliminar al docente"],
            "respuesta": "C",
            "explicacion": "La IA permite dar retroalimentación inmediata, lo cual es clave en la evaluación formativa."
        },
        {
            "tipo": "opcion",
            "pregunta": "¿Qué permite la evaluación formativa?",
            "opciones": ["A. Evaluar solo al final", "B. Ayudar al aprendizaje durante el proceso", "C. Hacer exámenes sorpresa", "D. Reprobar al estudiante"],
            "respuesta": "B",
            "explicacion": "La evaluación formativa busca mejorar el aprendizaje en tiempo real."
        },
        {
            "tipo": "vf",
            "pregunta": "La evaluación formativa se usa únicamente al final del curso. (V/F)",
            "respuesta": "F",
            "explicacion": "Se utiliza durante el proceso para mejorar el aprendizaje."
        },
        {
            "tipo": "abierta",
            "pregunta": "Menciona una característica de la evaluación formativa.",
            "respuesta": ["retroalimentación", "proceso", "mejora", "seguimiento"],
            "explicacion": "Busca identificar ideas clave como retroalimentación, seguimiento, etc."
        },
        {
            "tipo": "abierta",
            "pregunta": "¿Qué rol cumple el estudiante en la evaluación formativa?",
            "respuesta": ["activo", "participativo", "protagonista"],
            "explicacion": "El estudiante cumple un rol activo y participativo."
        }
    ],
    "intermedio": [
        {
            "tipo": "opcion",
            "pregunta": "¿Cómo puede usarse la IA para personalizar la enseñanza?",
            "opciones": ["A. Haciendo exámenes aleatorios", "B. Detectando el estilo de aprendizaje del estudiante", "C. Asignando tareas iguales para todos", "D. Usando robots"],
            "respuesta": "B",
            "explicacion": "La IA puede detectar estilos de aprendizaje y adaptar el contenido."
        },
        {
            "tipo": "opcion",
            "pregunta": "¿Qué ventaja ofrece la analítica de aprendizaje con IA?",
            "opciones": ["A. Aumenta la carga docente", "B. Predice el rendimiento estudiantil", "C. Crea exámenes más difíciles", "D. Reduce la retroalimentación"],
            "respuesta": "B",
            "explicacion": "La analítica puede predecir el rendimiento y detectar dificultades."
        },
        {
            "tipo": "vf",
            "pregunta": "La IA no puede detectar patrones de aprendizaje. (V/F)",
            "respuesta": "F",
            "explicacion": "La IA sí puede detectar patrones para personalizar la enseñanza."
        },
        {
            "tipo": "abierta",
            "pregunta": "¿Qué herramienta con IA conoces que apoye la evaluación formativa?",
            "respuesta": ["chatgpt", "quizziz", "kahoot", "duolingo"],
            "explicacion": "Existen muchas herramientas con IA que brindan retroalimentación."
        },
        {
            "tipo": "abierta",
            "pregunta": "Menciona un beneficio de usar IA en la educación.",
            "respuesta": ["personalización", "retroalimentación", "detección temprana", "seguimiento"],
            "explicacion": "La IA permite retroalimentación inmediata y personalización del aprendizaje."
        }
    ],
    "avanzado": [
        {
            "tipo": "opcion",
            "pregunta": "¿Cuál de los siguientes no es un riesgo ético de la IA en educación?",
            "opciones": ["A. Sesgos algorítmicos", "B. Violación de privacidad", "C. Retroalimentación", "D. Desigualdad en el acceso"],
            "respuesta": "C",
            "explicacion": "La retroalimentación no es un riesgo, es una ventaja."
        },
        {
            "tipo": "opcion",
            "pregunta": "¿Cómo puede la IA ayudar a estudiantes con necesidades especiales?",
            "opciones": ["A. Estandarizando actividades", "B. Personalizando los contenidos", "C. Usando textos largos", "D. Aumentando el número de pruebas"],
            "respuesta": "B",
            "explicacion": "La IA permite adaptar materiales a cada necesidad."
        },
        {
            "tipo": "vf",
            "pregunta": "La IA puede generar retroalimentación automática según el desempeño. (V/F)",
            "respuesta": "V",
            "explicacion": "Es una de sus funciones clave en evaluación formativa."
        },
        {
            "tipo": "abierta",
            "pregunta": "Menciona un dilema ético del uso de IA en la educación.",
            "respuesta": ["sesgo", "privacidad", "acceso desigual", "transparencia"],
            "explicacion": "Se busca reconocer riesgos como el sesgo o la privacidad."
        },
        {
            "tipo": "abierta",
            "pregunta": "¿Qué acciones puede tomar un docente al usar IA en la evaluación?",
            "respuesta": ["supervisar", "verificar", "validar", "ajustar"],
            "explicacion": "Debe supervisar y validar lo que genera la IA."
        }
    ]
}

# -------------------------------
# SUBTEMAS Y PREGUNTAS DE REFUERZO
# -------------------------------

subtemas = {
    "retroalimentación": {
        "texto": "La retroalimentación es un proceso esencial en la educación que permite a los estudiantes conocer su desempeño y áreas de mejora. La retroalimentación efectiva debe ser específica, oportuna y constructiva, ayudando a los estudiantes a entender sus errores y cómo corregirlos. En el contexto de la IA, esta puede proporcionar retroalimentación instantánea, lo que permite a los estudiantes ajustar su aprendizaje en tiempo real.",
        "preguntas": [
            {
                "tipo": "opcion",
                "pregunta": "¿Qué caracteriza a una retroalimentación efectiva?",
                "opciones": ["A. Ser vaga", "B. Ser específica y constructiva", "C. Ser solo positiva", "D. No ser oportuna"],
                "respuesta": "B",
                "explicacion": "La retroalimentación efectiva debe ser específica y constructiva."
            },
            {
                "tipo": "vf",
                "pregunta": "La retroalimentación instantánea no es útil para el aprendizaje. (V/F)",
                "respuesta": "F",
                "explicacion": "La retroalimentación instantánea es muy útil para el aprendizaje."
            },
            {
                "tipo": "abierta",
                "pregunta": "Menciona un tipo de retroalimentación.",
                "respuesta": ["inmediata", "constructiva", "específica"],
                "explicacion": "Existen diferentes tipos de retroalimentación, como la inmediata y constructiva."
            },
            {
                "tipo": "abierta",
                "pregunta": "¿Por qué es importante la retroalimentación en el aprendizaje?",
                "respuesta": ["mejora", "ajuste", "corrección"],
                "explicacion": "La retroalimentación es importante porque permite mejorar y ajustar el aprendizaje."
            }
        ],
        "recursos": {
            "video": {
                "titulo": "Optimización de Retroalimentación Educativa con IA",
                "url": "https://www.youtube.com/watch?v=ejemplo1"
            },
            "pdf": {
                "titulo": "Guía Completa de Retroalimentación Formativa",
                "url": "https://example.com/retroalimentacion.pdf"
            }
        }
    },
    "personalización del aprendizaje": {
        "texto": "La personalización del aprendizaje se refiere a adaptar la enseñanza a las necesidades y estilos de aprendizaje de cada estudiante. Con la ayuda de la IA, es posible analizar datos de rendimiento y preferencias de los estudiantes para ofrecer contenido y actividades que se ajusten a sus características individuales. Esto no solo mejora la motivación, sino que también optimiza el proceso de aprendizaje.",
        "preguntas": [
            {
                "tipo": "opcion",
                "pregunta": "¿Qué permite la personalización del aprendizaje?",
                "opciones": ["A. Un enfoque único para todos", "B. Adaptar la enseñanza a cada estudiante", "C. Ignorar las necesidades individuales", "D. Aumentar la carga de trabajo"],
                "respuesta": "B",
                "explicacion": "La personalización permite adaptar la enseñanza a las necesidades de cada estudiante."
            },
            {
                "tipo": "vf",
                "pregunta": "La personalización del aprendizaje no mejora la motivación. (V/F)",
                "respuesta": "F",
                "explicacion": "La personalización del aprendizaje puede mejorar la motivación de los estudiantes."
            },
            {
                "tipo": "abierta",
                "pregunta": "Menciona una herramienta que permita la personalización del aprendizaje.",
                "respuesta": ["plataformas de aprendizaje", "IA", "software educativo"],
                "explicacion": "Existen herramientas y plataformas que permiten personalizar el aprendizaje."
            },
            {
                "tipo": "abierta",
                "pregunta": "¿Por qué es importante personalizar el aprendizaje?",
                "respuesta": ["necesidades", "eficacia", "motivación"],
                "explicacion": "Es importante para atender las necesidades individuales y mejorar la eficacia del aprendizaje."
            }
        ],
        "recursos": {
            "video": {
                "titulo": "Personalizando el Aprendizaje con Inteligencia Artificial",
                "url": "https://www.youtube.com/watch?v=ejemplo2"
            },
            "pdf": {
                "titulo": "Manual de Aprendizaje Adaptativo",
                "url": "https://example.com/personalizacion.pdf"
            }
        }
    }
}

# -----------------------------------
# FUNCIONES PARA CADA NIVEL DE EXAMEN
# -----------------------------------

def iniciar_examen(nivel):
    st.session_state[f'iniciado_{nivel}'] = True
    if f'preguntas_{nivel}' not in st.session_state:
        st.session_state[f'preguntas_{nivel}'] = random.sample(niveles[nivel], 5)
        st.session_state[f'respuestas_{nivel}'] = [None] * 5
        st.session_state[f'actual_{nivel}'] = 0
        st.session_state[f'finalizado_{nivel}'] = False

def examen_nivel(nivel):
    preguntas = st.session_state[f'preguntas_{nivel}']
    actual = st.session_state[f'actual_{nivel}']
    respuestas = st.session_state[f'respuestas_{nivel}']

    progreso = int((actual / 5) * 100)
    st.progress(progreso, text=f"{actual}/5 preguntas respondidas")

    if actual < 5:
        p = preguntas[actual]

        # Mostrar pregunta y guardar la respuesta directamente en session_state
        if p["tipo"] == "opcion":
            st.session_state[f"{nivel}_respuesta_{actual}"] = st.radio(
                p["pregunta"],
                p["opciones"],
                index=p["opciones"].index(respuestas[actual]) if respuestas[actual] else 0,
                key=f"{nivel}_{actual}"
            )
        elif p["tipo"] == "vf":
            st.session_state[f"{nivel}_respuesta_{actual}"] = st.radio(
                p["pregunta"],
                ["V", "F"],
                index=["V", "F"].index(respuestas[actual]) if respuestas[actual] else 0,
                key=f"{nivel}_{actual}"
            )
        elif p["tipo"] == "abierta":
            st.session_state[f"{nivel}_respuesta_{actual}"] = st.text_input(
                p["pregunta"],
                value=respuestas[actual] if respuestas[actual] else "",
                key=f"{nivel}_{actual}"
            )

        if st.button("Siguiente pregunta", key=f"siguiente_{nivel}_{actual}"):
            respuesta_usuario = st.session_state.get(f"{nivel}_respuesta_{actual}")
            if respuesta_usuario is not None and respuesta_usuario != "":
                respuestas[actual] = respuesta_usuario
                st.session_state[f'actual_{nivel}'] += 1
            else:
                st.warning("Por favor responde antes de continuar.")

    if st.session_state[f'actual_{nivel}'] >= 5 and not st.session_state[f'finalizado_{nivel}']:
        puntaje = 0
        for i, p in enumerate(preguntas):
            if p["tipo"] in ["opcion", "vf"]:
                if respuestas[i] == p["respuesta"]:
                    puntaje += 1
            elif p["tipo"] == "abierta":
                if any(val in respuestas[i].lower() for val in p["respuesta"]):
                    puntaje += 1

        st.session_state[f'puntaje_{nivel}'] = puntaje
        st.session_state[f'finalizado_{nivel}'] = True

    if st.session_state[f'finalizado_{nivel}']:
        puntaje = st.session_state[f'puntaje_{nivel}']
        st.write(f"📊 Resultado final del nivel {nivel.upper()}: {puntaje}/5")
        for i, p in enumerate(preguntas):
            correcto = False
            if p["tipo"] in ["opcion", "vf"]:
                correcto = respuestas[i] == p["respuesta"]
            elif p["tipo"] == "abierta":
                correcto = any(val in respuestas[i].lower() for val in p["respuesta"])

            if correcto:
                st.success(f"✅ Pregunta {i+1}: Correcta")
            else:
                st.error(f"❌ Pregunta {i+1}: Incorrecta")
                st.info(f"ℹ️ Explicación: {p['explicacion']}")

        # Mostrar botones de refuerzo y recursos si no se aprueba
        if puntaje < 4:
            st.warning("❗ No aprobaste el nivel. Aquí tienes más opciones:")
            if st.button("Reforzamos"):
                realizar_refuerzo(st.session_state['tema_seleccionado'])
            if st.button("Recursos"):
                mostrar_recursos(st.session_state['tema_seleccionado'])
        else:
            if st.button("Siguiente Nivel INTERMEDIO"):
                iniciar_examen("intermedio")

        return puntaje

    return -1  # aún no termina

def realizar_refuerzo(tema):
    subtema = "retroalimentación" if tema == "retroalimentación" else "personalización del aprendizaje"
    st.write(f"🔁 Vamos a reforzar el tema: **{subtema.upper()}**")
    st.write(subtemas[subtema]["texto"])
    
    # Seleccionar preguntas del subtema
    preguntas_refuerzo = random.sample(subtemas[subtema]["preguntas"], len(subtemas[subtema]["preguntas"]))
    st.session_state['actual_refuerzo'] = 0
    st.session_state['respuestas_refuerzo'] = [None] * len(preguntas_refuerzo)
    st.session_state['finalizado_refuerzo'] = False

    while st.session_state['actual_refuerzo'] < len(preguntas_refuerzo):
        p = preguntas_refuerzo[st.session_state['actual_refuerzo']]
        
        # Asegurarse de que la clave sea única
        key_prefix = f"refuerzo_{st.session_state['actual_refuerzo']}"
        
        if p["tipo"] == "opcion":
            st.session_state[f"refuerzo_respuesta_{st.session_state['actual_refuerzo']}"] = st.radio(
                p["pregunta"],
                p["opciones"],
                key=f"{key_prefix}_radio"  # Usar una clave única
            )
        elif p["tipo"] == "vf":
            st.session_state[f"refuerzo_respuesta_{st.session_state['actual_refuerzo']}"] = st.radio(
                p["pregunta"],
                ["V", "F"],
                key=f"{key_prefix}_vf"  # Usar una clave única
            )
        elif p["tipo"] == "abierta":
            st.session_state[f"refuerzo_respuesta_{st.session_state['actual_refuerzo']}"] = st.text_input(
                p["pregunta"],
                key=f"{key_prefix}_text"  # Usar una clave única
            )

        if st.button("Siguiente pregunta", key=f"siguiente_refuerzo_{st.session_state['actual_refuerzo']}"):
            respuesta_usuario = st.session_state.get(f"refuerzo_respuesta_{st.session_state['actual_refuerzo']}")
            if respuesta_usuario is not None and respuesta_usuario != "":
                st.session_state['respuestas_refuerzo'][st.session_state['actual_refuerzo']] = respuesta_usuario
                st.session_state['actual_refuerzo'] += 1
            else:
                st.warning("Por favor responde antes de continuar.")

    # Calcular puntaje de refuerzo
    puntaje_refuerzo = 0
    for i, p in enumerate(preguntas_refuerzo):
        if p["tipo"] in ["opcion", "vf"]:
            if st.session_state['respuestas_refuerzo'][i] == p["respuesta"]:
                puntaje_refuerzo += 1
        elif p["tipo"] == "abierta":
            if any(val in st.session_state['respuestas_refuerzo'][i].lower() for val in p["respuesta"]):
                puntaje_refuerzo += 1

    st.write(f"📊 Resultado final del refuerzo: {puntaje_refuerzo}/{len(preguntas_refuerzo)}")
    for i, p in enumerate(preguntas_refuerzo):
        correcto = False
        if p["tipo"] in ["opcion", "vf"]:
            correcto = st.session_state['respuestas_refuerzo'][i] == p["respuesta"]
        elif p["tipo"] == "abierta":
            correcto = any(val in st.session_state['respuestas_refuerzo'][i].lower() for val in p["respuesta"])

        if correcto:
            st.success(f"✅ Pregunta {i+1}: Correcta")
        else:
            st.error(f"❌ Pregunta {i+1}: Incorrecta")
            st.info(f"ℹ️ Explicación: {p['explicacion']}")

    # Mostrar recursos si no se aprueba el refuerzo
    if puntaje_refuerzo < 3:
        st.warning("❗ No aprobaste el refuerzo. Aquí tienes más recursos:")
        mostrar_recursos(tema)

def mostrar_recursos(tema):
    if tema == "retroalimentación":
        st.write("📹 Video: [Optimización de Retroalimentación Educativa con IA](https://www.youtube.com/watch?v=ejemplo1)")
        st.write("📄 PDF: [Guía Completa de Retroalimentación Formativa](https://example.com/retroalimentacion.pdf)")
    elif tema == "personalización del aprendizaje":
        st.write("📹 Video: [Personalizando el Aprendizaje con Inteligencia Artificial](https://www.youtube.com/watch?v=ejemplo2)")
        st.write("📄 PDF: [Manual de Aprendizaje Adaptativo](https://example.com/personalizacion.pdf)")

# -----------------------------------
# FLUJO PRINCIPAL
# -----------------------------------

def main():
    st.title("🎓 EXAMEN ADAPTATIVO: Evaluación Formativa con IA")

    st.write("""
    Este examen tiene tres niveles: **BÁSICO**, **INTERMEDIO** y **AVANZADO**.

    👉 Debes responder correctamente al menos 4 de 5 preguntas para avanzar.
    """)

    # Inicializar estados generales una sola vez
    for nivel in ["básico", "intermedio", "avanzado"]:
        st.session_state.setdefault(f'iniciado_{nivel}', False)

    # Selección de tema
    tema_seleccionado = st.selectbox("Selecciona un tema:", ["retroalimentación", "personalización del aprendizaje"])
    st.session_state['tema_seleccionado'] = tema_seleccionado  # Guardar el tema seleccionado

    # Botones de inicio
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Iniciar Nivel BÁSICO"):
            iniciar_examen("básico")
    with col2:
        if st.button("Iniciar Nivel INTERMEDIO"):
            if st.session_state.get('puntaje_básico', 0) >= 4:
                iniciar_examen("intermedio")
            else:
                st.warning("Debes aprobar el nivel BÁSICO primero.")
    with col3:
        if st.button("Iniciar Nivel AVANZADO"):
            if st.session_state.get('puntaje_intermedio', 0) >= 4:
                iniciar_examen("avanzado")
            else:
                st.warning("Debes aprobar el nivel INTERMEDIO primero.")

    # Mostrar exámenes si se han iniciado
    if st.session_state['iniciado_básico']:
        examen_nivel("básico")
    elif st.session_state['iniciado_intermedio']:
        examen_nivel("intermedio")
    elif st.session_state['iniciado_avanzado']:
        examen_nivel("avanzado")

# -------------------------------
# EJECUTAR APP
# -------------------------------
main()











