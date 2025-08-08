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
            "respuesta": "C. Dar retroalimentación inmediata",
            "explicacion": "La IA permite dar retroalimentación inmediata, lo cual es clave en la evaluación formativa."
        },
        {
            "tipo": "opcion",
            "pregunta": "¿Qué permite la evaluación formativa?",
            "opciones": ["A. Evaluar solo al final", "B. Ayudar al aprendizaje durante el proceso", "C. Hacer exámenes sorpresa", "D. Reprobar al estudiante"],
            "respuesta": "B. Ayudar al aprendizaje durante el proceso",
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
            "respuesta": "B. Detectando el estilo de aprendizaje del estudiante",
            "explicacion": "La IA puede detectar estilos de aprendizaje y adaptar el contenido."
        },
        {
            "tipo": "opcion",
            "pregunta": "¿Qué ventaja ofrece la analítica de aprendizaje con IA?",
            "opciones": ["A. Aumenta la carga docente", "B. Predice el rendimiento estudiantil", "C. Crea exámenes más difíciles", "D. Reduce la retroalimentación"],
            "respuesta": "B. Predice el rendimiento estudiantil",
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
            "respuesta": "C. Retroalimentación",
            "explicacion": "La retroalimentación no es un riesgo, es una ventaja."
        },
        {
            "tipo": "opcion",
            "pregunta": "¿Cómo puede la IA ayudar a estudiantes con necesidades especiales?",
            "opciones": ["A. Estandarizando actividades", "B. Personalizando los contenidos", "C. Usando textos largos", "D. Aumentando el número de pruebas"],
            "respuesta": "B. Personalizando los contenidos",
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
                "respuesta": "B. Ser específica y constructiva",
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
                "url": "https://us02web.zoom.us/rec/share/Pma546yfdz1OYxpEo3xpt0W_mUw69j_wVDEj7TBynAeS6Tdn9_psfMv2o-6hhasN.NTNu-3Zho_wZ0A_N"
            },
            "pdf": {
                "titulo": "Guía Completa de Retroalimentación Formativa",
                "url": "https://classroom.google.com/c/NzY0ODQwMTMxNzE5/m/Nzg3NzU3NTQxMjM3/details"
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
                "url": "https://us02web.zoom.us/rec/share/AwNC5JTqq_aMxTKYjv8IIHZnNBA6aYtp4fG5Y1vqg8Q_3Li4nkmntfZIxvIvtINd.xATS_XsFmTLeIwK3"
            },
            "pdf": {
                "titulo": "Manual de Aprendizaje Adaptativo",
                "url": "https://docs.google.com/document/d/1ngN7NvlMA13VhDFFT_ZiNrzRi8XwxKXFoStYoExED7o/edit?tab=t.0"
            }
        }
    }
}

# --------------------------
# FUNCIONES AUXILIARES
# --------------------------
def iniciar_examen(nivel):
    st.session_state[f'iniciado_{nivel}'] = True
    for otro in ["básico", "intermedio", "avanzado"]:
        if otro != nivel:
            st.session_state[f'iniciado_{otro}'] = False
    st.session_state[f'preguntas_{nivel}'] = random.sample(niveles[nivel], 5)
    st.session_state[f'respuestas_{nivel}'] = [None] * 5
    st.session_state[f'actual_{nivel}'] = 0
    st.session_state[f'finalizado_{nivel}'] = False
    st.session_state["mostrar"] = None

def limpiar_y_redirigir(nivel, accion):
    st.session_state[f'iniciado_{nivel}'] = False
    st.session_state[f'finalizado_{nivel}'] = False
    st.session_state[f'actual_{nivel}'] = 0
    st.session_state[f'puntaje_{nivel}'] = 0
    st.session_state[f'respuestas_{nivel}'] = [None] * 5
    st.session_state["mostrar"] = accion
    st.session_state["nivel_refuerzo"] = nivel
    st.rerun()

def examen_nivel(nivel):
    preguntas = st.session_state[f'preguntas_{nivel}']
    actual = st.session_state[f'actual_{nivel}']
    respuestas = st.session_state[f'respuestas_{nivel}']

    st.progress(int((actual / 5) * 100), text=f"{actual}/5 preguntas respondidas")

    if actual < 5:
        p = preguntas[actual]
        key = f"{nivel}_{actual}"

        if p["tipo"] == "opcion":
            st.session_state[f"{nivel}_respuesta_{actual}"] = st.radio(
                p["pregunta"], p["opciones"],
                index=p["opciones"].index(respuestas[actual]) if respuestas[actual] else 0,
                key=key
            )
        elif p["tipo"] == "vf":
            st.session_state[f"{nivel}_respuesta_{actual}"] = st.radio(
                p["pregunta"], ["V", "F"],
                index=["V", "F"].index(respuestas[actual]) if respuestas[actual] else 0,
                key=key
            )
        elif p["tipo"] == "abierta":
            st.session_state[f"{nivel}_respuesta_{actual}"] = st.text_input(
                p["pregunta"], value=respuestas[actual] if respuestas[actual] else "", key=key
            )

        if st.button("Siguiente pregunta", key=f"siguiente_{nivel}_{actual}"):
            respuesta_usuario = st.session_state.get(f"{nivel}_respuesta_{actual}")
            if respuesta_usuario:
                respuestas[actual] = respuesta_usuario
                st.session_state[f'actual_{nivel}'] += 1
                st.rerun()
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
        st.subheader(f"📊 Resultado final del nivel {nivel.upper()}: {puntaje}/5")
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

        if puntaje < 4:
            st.warning("❗ No aprobaste el nivel. Aquí tienes más opciones:")
            if st.button("🔁 Reforzamos"):
                limpiar_y_redirigir(nivel, "refuerzo")
            if st.button("📚 Ver Recursos"):
                limpiar_y_redirigir(nivel, "recursos")
        else:
            if nivel == "básico":
                if st.button("▶️ Continuar a INTERMEDIO"):
                    iniciar_examen("intermedio")
            elif nivel == "intermedio":
                if st.button("▶️ Continuar a AVANZADO"):
                    iniciar_examen("avanzado")


def realizar_refuerzo(tema):
    subtema = tema
    preguntas_refuerzo = subtemas[subtema]["preguntas"]

    st.subheader(f"🔁 Refuerzo del tema: {subtema.upper()}")
    st.write(subtemas[subtema]["texto"])

    if 'respuestas_refuerzo' not in st.session_state:
        st.session_state['respuestas_refuerzo'] = [None] * len(preguntas_refuerzo)

    with st.form(key='refuerzo_form'):
        for i, p in enumerate(preguntas_refuerzo):
            key = f"ref_refuerzo_{i}_{subtema}"
            if p["tipo"] == "opcion":
                st.session_state['respuestas_refuerzo'][i] = st.radio(
                    p["pregunta"],
                    p["opciones"],
                    index=p["opciones"].index(st.session_state['respuestas_refuerzo'][i])
                    if st.session_state['respuestas_refuerzo'][i] else 0,
                    key=key
                )
            elif p["tipo"] == "vf":
                st.session_state['respuestas_refuerzo'][i] = st.radio(
                    p["pregunta"],
                    ["V", "F"],
                    index=["V", "F"].index(st.session_state['respuestas_refuerzo'][i])
                    if st.session_state['respuestas_refuerzo'][i] else 0,
                    key=key
                )
            elif p["tipo"] == "abierta":
                st.session_state['respuestas_refuerzo'][i] = st.text_input(
                    p["pregunta"],
                    value=st.session_state['respuestas_refuerzo'][i]
                    if st.session_state['respuestas_refuerzo'][i] else "",
                    key=key
                )

        submit_button = st.form_submit_button("Enviar Respuestas")

    if submit_button:
        puntaje = 0
        for i, p in enumerate(preguntas_refuerzo):
            r = st.session_state['respuestas_refuerzo'][i]
            if p["tipo"] in ["opcion", "vf"]:
                if str(r).strip().upper() == str(p["respuesta"]).strip().upper():
                    puntaje += 1
            elif p["tipo"] == "abierta":
                if any(val in str(r).lower() for val in p["respuesta"]):
                    puntaje += 1

        total_preg = len(preguntas_refuerzo)
        st.subheader(f"📊 Resultado del Refuerzo: {puntaje}/{total_preg}")

        for i, p in enumerate(preguntas_refuerzo):
            r = st.session_state['respuestas_refuerzo'][i]
            correcto = False
            if p["tipo"] in ["opcion", "vf"]:
                correcto = str(r).strip().upper() == str(p["respuesta"]).strip().upper()
            elif p["tipo"] == "abierta":
                correcto = any(val in str(r).lower() for val in p["respuesta"])

            if correcto:
                st.success(f"✅ Pregunta {i+1}: Correcta")
            else:
                st.error(f"❌ Pregunta {i+1}: Incorrecta")
                st.info(f"ℹ️ Explicación: {p['explicacion']}")

        # Mover el botón FUERA del formulario
        if puntaje >= 3:
            st.success("🎉 ¡Has aprobado el refuerzo!")
            st.session_state['refuerzo_aprobado'] = True
            if st.button("▶️ Continuar al nivel INTERMEDIO"):
                iniciar_examen("intermedio")  # Esto activa iniciado_intermedio=True
                st.session_state["mostrar"] = None  # Quita la pantalla de refuerzo
                st.session_state['refuerzo_aprobado'] = False  # Limpia bandera para futuros intentos
                st.experimental_rerun()
        else:
            st.warning("❌ No aprobaste el refuerzo.")
            if st.button("🔁 Reiniciar refuerzo"):
                st.session_state['respuestas_refuerzo'] = [None] * len(preguntas_refuerzo)
                st.experimental_rerun()  # Reiniciar para volver a mostrar el refuerzo

def mostrar_recursos(tema):
    recursos = subtemas[tema]["recursos"]
    st.subheader(f"📚 Recursos para el tema: {tema.upper()}")
    
    # Mostrar video como enlace de texto si está disponible
    if "video" in recursos:
        st.write("VER VIDEO")
        st.markdown(f"[{recursos['video']['titulo']}]({recursos['video']['url']})")  # Enlace de Zoom
        
    
    # Mostrar PDF si está disponible
    if "pdf" in recursos:
        st.write("VER LECTURA")
        st.markdown(f"[{recursos['pdf']['titulo']}]({recursos['pdf']['url']})")
       

# En el flujo principal, asegúrate de que el examen del nivel intermedio se muestre correctamente
def main():
    st.session_state.setdefault("mostrar", None)
    st.session_state.setdefault("refuerzo_aprobado", False)  # Inicializar el estado de aprobación del refuerzo

    if st.session_state["mostrar"] == "refuerzo":
        tema = st.session_state.get('tema_seleccionado', 'retroalimentación')
        realizar_refuerzo(tema)
        return  # Mover el return aquí para que no interrumpa el flujo

    if st.session_state["mostrar"] == "recursos":
        tema = st.session_state.get('tema_seleccionado', 'retroalimentación')
        mostrar_recursos(tema)
        return

    # Solo se muestra si no está en refuerzo ni recursos
    st.title("🎓 EXAMEN ADAPTATIVO: Evaluación Formativa con IA")
    st.markdown("Este examen tiene tres niveles: **BÁSICO**, **INTERMEDIO** y **AVANZADO**. Debes aprobar con 4/5 para avanzar.")

    for nivel in ["básico", "intermedio", "avanzado"]:
        st.session_state.setdefault(f'iniciado_{nivel}', False)

    tema = st.selectbox("Selecciona un tema:", list(subtemas.keys()))
    st.session_state['tema_seleccionado'] = tema

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔴 Iniciar BÁSICO"):
            iniciar_examen("básico")
    with col2:
        if st.button("🔴 Iniciar INTERMEDIO"):
            if st.session_state.get("puntaje_básico", 0) >= 4 or st.session_state['refuerzo_aprobado']:
                iniciar_examen("intermedio")
                st.session_state['refuerzo_aprobado'] = False  # Reiniciar el estado de aprobación
            else:
                st.warning("Debes aprobar el nivel BÁSICO primero.")
    with col3:
        if st.button("🔴 Iniciar AVANZADO"):
            if st.session_state.get("puntaje_intermedio", 0) >= 4:
                iniciar_examen("avanzado")
            else:
                st.warning("Debes aprobar el nivel INTERMEDIO primero.")

    if st.session_state["iniciado_básico"]:
        examen_nivel("básico")
    elif st.session_state["iniciado_intermedio"]:
        examen_nivel("intermedio")
    elif st.session_state["iniciado_avanzado"]:
        examen_nivel("avanzado")

# -------------------------------
# EJECUTAR APP
# -------------------------------
main()





























