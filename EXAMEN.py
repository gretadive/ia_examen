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

def hacer_pregunta(p):
    if p["tipo"] == "opcion":
        r = st.radio(p["pregunta"], p["opciones"])
        if r == p["respuesta"]:
            st.success("¡Correcto!")
            return True
        else:
            st.error("Incorrecto. Revisa el concepto.")
            st.info(p["explicacion"])
            return False

    elif p["tipo"] == "vf":
        r = st.radio(p["pregunta"], ["V", "F"])
        if r == p["respuesta"]:
            st.success("¡Correcto!")
            return True
        else:
            st.error("Incorrecto. Revisa el concepto.")
            st.info(p["explicacion"])
            return False

    elif p["tipo"] == "abierta":
        r = st.text_input(p["pregunta"])
        if any(val in r.lower() for val in p["respuesta"]):
            st.success("¡Correcto!")
            return True
        else:
            st.error("Incorrecto. Revisa el concepto.")
            st.info(p["explicacion"])
            return False

def examen_nivel(nombre_nivel):
    st.write(f"🧪 Nivel: {nombre_nivel.upper()} (Debes acertar al menos 4 de 5)")
    preguntas = random.sample(niveles[nombre_nivel], 5)
    puntaje = 0
    for p in preguntas:
        if hacer_pregunta(p):
            puntaje += 1
    st.write(f"📊 Resultado: {puntaje}/5")
    return puntaje

def reforzar_conceptos():
    st.write("🔁 Vamos a reforzar juntos este tema.")
    subtema_seleccionado = random.choice(list(subtemas.keys()))
    st.write(f"📚 Tema de refuerzo: {subtema_seleccionado.upper()}")
    st.write(subtemas[subtema_seleccionado]["texto"])

    preguntas_refuerzo = random.sample(subtemas[subtema_seleccionado]["preguntas"], 4)
    puntaje_refuerzo = 0

    for p in preguntas_refuerzo:
        if hacer_pregunta(p):
            puntaje_refuerzo += 1

    st.write(f"📊 Puntaje de refuerzo: {puntaje_refuerzo}/4")

    if puntaje_refuerzo >= 3:
        st.success("🎉 ¡Refuerzo exitoso! Puedes continuar.")
        return True
    else:
        st.error("❗ Necesitas más práctica. Te recomendamos estos recursos:")
        st.write(f"📹 Video: {subtemas[subtema_seleccionado]['recursos']['video']['titulo']}")
        st.write(f"[Ver Video]({subtemas[subtema_seleccionado]['recursos']['video']['url']})")
        st.write(f"📄 PDF: {subtemas[subtema_seleccionado]['recursos']['pdf']['titulo']}")
        st.write(f"[Ver PDF]({subtemas[subtema_seleccionado]['recursos']['pdf']['url']})")
        return False

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

    # Selección de tema
    tema_seleccionado = st.selectbox("Selecciona un tema:", ["retroalimentación", "personalización del aprendizaje"])

    # Botones para niveles
    if st.button("Nivel BÁSICO"):
        st.write("📘 Comenzarás con el nivel BÁSICO.")
        if examen_nivel("básico") >= 4:
            st.success("✅ ¡Pasas al nivel INTERMEDIO!")
        else:
            st.warning("🔁 No aprobaste el nivel BÁSICO. Vamos a reforzar.")
            if not reforzar_conceptos():
                st.info("📌 Revisa los recursos y vuelve a intentarlo más tarde.")
                return

    if st.button("Nivel INTERMEDIO"):
        st.write("📘 Intentando acceder al nivel INTERMEDIO.")
        if examen_nivel("básico") < 4:
            st.warning("❗ Debes aprobar el nivel BÁSICO para acceder al nivel INTERMEDIO.")
        else:
            if examen_nivel("intermedio") >= 4:
                st.success("✅ ¡Pasas al nivel AVANZADO!")
            else:
                st.warning("🔁 No aprobaste el nivel INTERMEDIO. Vamos a reforzar.")
                if not reforzar_conceptos():
                    st.info("📌 Revisa los recursos y vuelve a intentarlo más tarde.")
                    return

    if st.button("Nivel AVANZADO"):
        st.write("📘 Intentando acceder al nivel AVANZADO.")
        if examen_nivel("intermedio") < 4:
            st.warning("❗ Debes aprobar el nivel INTERMEDIO para acceder al nivel AVANZADO.")
        else:
            if examen_nivel("avanzado") >= 4:
                st.success("🏁 ¡Felicidades! Has completado exitosamente todos los niveles.")
            else:
                st.warning("🔁 No aprobaste el nivel AVANZADO. Vamos a reforzar.")
                if reforzar_conceptos():
                    st.success("🎯 ¡Listo! Has completado el examen adaptativo.")
                else:
                    st.info("📌 Revisa los recursos y vuelve a intentarlo más tarde.")

# Ejecutar siempre el flujo principal
main()
