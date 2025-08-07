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

# -------------------------------
# FUNCIONES PRINCIPALES
# -------------------------------

def hacer_pregunta(p, nombre_nivel):
    respuesta_usuario = None
    if p["tipo"] == "opcion":
        respuesta_usuario = st.radio(p["pregunta"], p["opciones"], key=f"{nombre_nivel}_{p['pregunta']}")
    elif p["tipo"] == "vf":
        respuesta_usuario = st.radio(p["pregunta"], ["V", "F"], key=f"{nombre_nivel}_{p['pregunta']}")
    elif p["tipo"] == "abierta":
        respuesta_usuario = st.text_input(p["pregunta"], key=f"{nombre_nivel}_{p['pregunta']}")
    return respuesta_usuario

def verificar_respuesta(pregunta, respuesta_usuario):
    if pregunta["tipo"] in ["opcion", "vf"]:
        return respuesta_usuario == pregunta["respuesta"]
    elif pregunta["tipo"] == "abierta":
        return any(val in respuesta_usuario.lower() for val in pregunta["respuesta"])
    return False

def examen_nivel(nombre_nivel):
    st.write(f"🧪 Nivel: {nombre_nivel.upper()} (Debes acertar al menos 4 de 5)")

    # Inicializar el estado
    if f'preguntas_{nombre_nivel}' not in st.session_state:
        st.session_state[f'preguntas_{nombre_nivel}'] = random.sample(niveles[nombre_nivel], 5)
        st.session_state[f'respuestas_{nombre_nivel}'] = [None] * 5
        st.session_state[f'actual_{nombre_nivel}'] = 0
        st.session_state[f'finalizado_{nombre_nivel}'] = False

    preguntas = st.session_state[f'preguntas_{nombre_nivel}']
    actual = st.session_state[f'actual_{nombre_nivel}']
    respuestas = st.session_state[f'respuestas_{nombre_nivel}']

    # Barra de progreso
    progreso = int((actual / 5) * 100)
    st.progress(progreso, text=f"{actual}/5 preguntas respondidas")

    # Mostrar pregunta actual
    if actual < 5:
        p = preguntas[actual]
        r_usuario = hacer_pregunta(p, nombre_nivel)
        if st.button("Siguiente pregunta", key=f"btn_siguiente_{nombre_nivel}_{actual}"):
            if r_usuario is not None and r_usuario != "":
                respuestas[actual] = r_usuario
                st.session_state[f'actual_{nombre_nivel}'] += 1
            else:
                st.warning("Por favor responde antes de continuar.")

    # Evaluar si terminó
    if st.session_state[f'actual_{nombre_nivel}'] >= 5:
        if not st.session_state[f'finalizado_{nombre_nivel}']:
            puntaje = 0
            for i, p in enumerate(preguntas):
                if verificar_respuesta(p, respuestas[i]):
                    puntaje += 1
            st.session_state[f'puntaje_{nombre_nivel}'] = puntaje
            st.session_state[f'finalizado_{nombre_nivel}'] = True

        puntaje_final = st.session_state[f'puntaje_{nombre_nivel}']
        st.write(f"📊 Resultado: {puntaje_final}/5")
        for i, p in enumerate(preguntas):
            correcto = verificar_respuesta(p, respuestas[i])
            if correcto:
                st.success(f"✅ Pregunta {i+1}: Correcto")
            else:
                st.error(f"❌ Pregunta {i+1}: Incorrecto")
                st.info(f"ℹ️ Explicación: {p['explicacion']}")
        return puntaje_final

    return -1  # No finalizado


# -------------------------------
# FLUJO PRINCIPAL
# -------------------------------

def main():
    st.title("🎓 EXAMEN ADAPTATIVO: Evaluación Formativa con IA")

    st.header("📘 Bienvenida")
    st.write("""
    Este examen tiene tres niveles: **BÁSICO**, **INTERMEDIO** y **AVANZADO**.
    
    - Comenzarás por el nivel BÁSICO.
    - Debes responder al menos 4 de 5 preguntas correctamente para avanzar.
    - Si no apruebas, recibirás un refuerzo con preguntas y recursos de aprendizaje.
    
    👉 Selecciona un tema y luego presiona uno de los botones para comenzar.
    """)

    tema_seleccionado = st.selectbox("Selecciona un tema:", list(subtemas.keys()))

    if st.button("Nivel BÁSICO"):
        resultado = examen_nivel("básico")
        if resultado >= 0:
            if resultado >= 4:
                st.success("✅ ¡Pasas al nivel INTERMEDIO!")
            else:
                st.warning("🔁 No aprobaste el nivel BÁSICO. Vamos a reforzar.")

    if st.button("Nivel INTERMEDIO"):
        if st.session_state.get('puntaje_básico', 0) < 4:
            st.warning("❗ Debes aprobar el nivel BÁSICO para acceder al nivel INTERMEDIO.")
        else:
            resultado = examen_nivel("intermedio")
            if resultado >= 0:
                if resultado >= 4:
                    st.success("✅ ¡Pasas al nivel AVANZADO!")
                else:
                    st.warning("🔁 No aprobaste el nivel INTERMEDIO. Vamos a reforzar.")

    if st.button("Nivel AVANZADO"):
        if st.session_state.get('puntaje_intermedio', 0) < 4:
            st.warning("❗ Debes aprobar el nivel INTERMEDIO para acceder al nivel AVANZADO.")
        else:
            resultado = examen_nivel("avanzado")
            if resultado >= 0:
                if resultado >= 4:
                    st.success("🏁 ¡Felicidades! Has completado exitosamente todos los niveles.")
                else:
                    st.warning("🔁 No aprobaste el nivel AVANZADO. Vamos a reforzar.")


# -------------------------------
# DATOS (niveles y subtemas)
# -------------------------------

# Incluye aquí las secciones `niveles` y `subtemas` que ya tienes, no es necesario modificarlas para que esto funcione correctamente.

# -------------------------------
# EJECUTAR
# -------------------------------
main()


