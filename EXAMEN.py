import streamlit as st
import unicodedata
import io

# =====================
# DATOS DEL EXAMEN
# =====================
niveles = {
    "básico": [
        {"pregunta": "¿Cuál es una ventaja de la evaluación formativa con IA?",
         "tipo": "opcion_multiple",
         "opciones": ["Castigar errores", "Promover la memorización", "Dar retroalimentación inmediata", "Eliminar al docente"],
         "respuesta": "Dar retroalimentación inmediata",
         "explicacion": "La IA permite dar retroalimentación inmediata, lo cual es clave en la evaluación formativa."},
        {"pregunta": "¿Qué permite la evaluación formativa?",
         "tipo": "opcion_multiple",
         "opciones": ["Evaluar solo al final", "Ayudar al aprendizaje durante el proceso", "Hacer exámenes sorpresa", "Reprobar al estudiante"],
         "respuesta": "Ayudar al aprendizaje durante el proceso",
         "explicacion": "La evaluación formativa guía y apoya el aprendizaje mientras ocurre."}
    ],
    "intermedio": [
        {"pregunta": "¿Qué ventaja tiene usar IA en la personalización del aprendizaje?",
         "tipo": "opcion_multiple",
         "opciones": ["Aumentar el castigo", "Adaptar el contenido", "Eliminar el trabajo docente", "Generar exámenes aleatorios"],
         "respuesta": "Adaptar el contenido",
         "explicacion": "La IA puede adaptar el contenido a las necesidades del estudiante."},
        {"pregunta": "¿Qué significa personalizar el aprendizaje?",
         "tipo": "abierta",
         "respuesta": ["adaptar", "necesidades", "estudiante"],
         "explicacion": "Significa adaptar el contenido y ritmo a las necesidades del estudiante."}
    ]
}

subtemas = {
    "retroalimentación": {
        "refuerzo": [
            {"pregunta": "¿Qué significa retroalimentación efectiva?",
             "tipo": "abierta",
             "respuesta": ["mejorar", "progreso", "guía"],
             "explicacion": "La retroalimentación efectiva ayuda a mejorar y guiar el progreso del estudiante."}
        ],
        "recursos": {
            "pdf": "https://ejemplo.com/retroalimentacion.pdf",
            "video": "https://youtu.be/abcd1234"
        }
    },
    "personalización": {
        "refuerzo": [
            {"pregunta": "¿Qué busca la personalización del aprendizaje?",
             "tipo": "abierta",
             "respuesta": ["adaptar", "necesidades", "estudiante"],
             "explicacion": "Busca adaptar el aprendizaje a las necesidades de cada estudiante."}
        ],
        "recursos": {
            "pdf": "https://ejemplo.com/personalizacion.pdf",
            "video": "https://youtu.be/wxyz5678"
        }
    }
}

# =====================
# FUNCIONES
# =====================
def normalizar_texto(texto):
    return unicodedata.normalize('NFD', texto.lower()).encode('ascii', 'ignore').decode('utf-8')

def evaluar_respuesta(pregunta, respuesta_usuario):
    correcta = False
    if pregunta["tipo"] in ["opcion_multiple", "vf"]:
        correcta = normalizar_texto(respuesta_usuario) == normalizar_texto(pregunta["respuesta"])
    elif pregunta["tipo"] == "abierta":
        for palabra in pregunta["respuesta"]:
            if palabra.lower() in normalizar_texto(respuesta_usuario):
                correcta = True
                break
    return correcta

def generar_txt(historial):
    buffer = io.StringIO()
    for bloque in historial:
        buffer.write(f"{bloque['titulo']}\nNota: {bloque['nota']}%\n\n")
        for idx, p in enumerate(bloque["preguntas"], 1):
            buffer.write(f"{idx}) {p['pregunta']}\n")
            buffer.write(f"Tu respuesta: {p['respuesta_usuario']}\n")
            buffer.write(f"Respuesta correcta: {p['respuesta_correcta']}\n")
            buffer.write(f"Explicación: {p['explicacion']}\n\n")
        buffer.write("-" * 40 + "\n")
    return buffer.getvalue()

def avanzar_fase():
    niveles_lista = list(niveles.keys())
    idx = niveles_lista.index(st.session_state.nivel)
    if idx + 1 < len(niveles_lista):
        st.session_state.nivel = niveles_lista[idx + 1]
        st.session_state.fase = "examen"
    else:
        st.session_state.fase = "final"

# =====================
# INICIALIZACIÓN
# =====================
if "fase" not in st.session_state:
    st.session_state.fase = "inicio"
if "tema" not in st.session_state:
    st.session_state.tema = None
if "nivel" not in st.session_state:
    st.session_state.nivel = "básico"
if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0
if "respuestas" not in st.session_state:
    st.session_state.respuestas = []
if "historial" not in st.session_state:
    st.session_state.historial = []
if "refuerzo" not in st.session_state:
    st.session_state.refuerzo = False

# =====================
# FLUJO
# =====================
st.title("Examen Adaptativo con IA")

if st.session_state.fase == "inicio":
    st.subheader("Seleccione un tema para el refuerzo")
    st.session_state.tema = st.selectbox("Tema:", list(subtemas.keys()))
    if st.button("Iniciar examen"):
        st.session_state.fase = "examen"

elif st.session_state.fase in ["examen", "refuerzo"]:
    preguntas = subtemas[st.session_state.tema]["refuerzo"] if st.session_state.refuerzo else niveles[st.session_state.nivel]
    total_preguntas = len(preguntas)

    progreso = (st.session_state.pregunta_actual + 1) / total_preguntas
    st.progress(progreso)

    pregunta = preguntas[st.session_state.pregunta_actual]
    st.write(f"**Pregunta {st.session_state.pregunta_actual + 1} de {total_preguntas}**")
    st.write(pregunta["pregunta"])

    if pregunta["tipo"] == "opcion_multiple":
        respuesta = st.radio("Selecciona una opción:", pregunta["opciones"], key=f"preg_{st.session_state.pregunta_actual}")
    else:
        respuesta = st.text_input("Escribe tu respuesta:", key=f"preg_{st.session_state.pregunta_actual}")

    if st.button("Siguiente" if st.session_state.pregunta_actual < total_preguntas - 1 else "Terminar bloque"):
        st.session_state.respuestas.append(respuesta)
        if st.session_state.pregunta_actual < total_preguntas - 1:
            st.session_state.pregunta_actual += 1
        else:
            # Evaluar bloque
            correctas = 0
            detalles = []
            for i, preg in enumerate(preguntas):
                es_correcta = evaluar_respuesta(preg, st.session_state.respuestas[i])
                if es_correcta:
                    correctas += 1
                detalles.append({
                    "pregunta": preg["pregunta"],
                    "respuesta_usuario": st.session_state.respuestas[i],
                    "respuesta_correcta": preg["respuesta"],
                    "explicacion": preg["explicacion"]
                })
            nota = round((correctas / total_preguntas) * 100, 2)
            st.session_state.historial.append({"titulo": f"{'Refuerzo' if st.session_state.refuerzo else 'Examen ' + st.session_state.nivel}", "nota": nota, "preguntas": detalles})

            # Reset estado preguntas
            st.session_state.pregunta_actual = 0
            st.session_state.respuestas = []

            if st.session_state.refuerzo:
                st.session_state.refuerzo = False
                st.session_state.fase = "examen"  # repetir mismo nivel
            else:
                if nota >= 80:
                    avanzar_fase()
                else:
                    st.session_state.refuerzo = True
                    st.session_state.fase = "refuerzo"

elif st.session_state.fase == "final":
    st.success("¡Has completado todos los niveles!")
    for bloque in st.session_state.historial:
        st.write(f"{bloque['titulo']}: {bloque['nota']}%")
    txt_data = generar_txt(st.session_state.historial)
    st.download_button("Descargar resultados", txt_data, file_name="resultados.txt")
