# app.py
import streamlit as st
import unicodedata
import datetime

# -------------------------------
# Datos: niveles y subtemas (los que dictaste)
# -------------------------------
niveles = {
    "básico": [
        {"tipo":"opcion","pregunta":"¿Cuál es una ventaja de la evaluación formativa con IA?","opciones":["A. Castigar errores","B. Promover la memorización","C. Dar retroalimentación inmediata","D. Eliminar al docente"],"respuesta":"C","explicacion":"La IA permite dar retroalimentación inmediata, lo cual es clave en la evaluación formativa."},
        {"tipo":"opcion","pregunta":"¿Qué permite la evaluación formativa?","opciones":["A. Evaluar solo al final","B. Ayudar al aprendizaje durante el proceso","C. Hacer exámenes sorpresa","D. Reprobar al estudiante"],"respuesta":"B","explicacion":"La evaluación formativa busca mejorar el aprendizaje en tiempo real."},
        {"tipo":"vf","pregunta":"La evaluación formativa se usa únicamente al final del curso. (V/F)","respuesta":"F","explicacion":"Se utiliza durante el proceso para mejorar el aprendizaje."},
        {"tipo":"abierta","pregunta":"Menciona una característica de la evaluación formativa.","respuesta":["retroalimentacion","proceso","mejora","seguimiento"],"explicacion":"Busca identificar ideas clave como retroalimentación, seguimiento, etc."},
        {"tipo":"abierta","pregunta":"¿Qué rol cumple el estudiante en la evaluación formativa?","respuesta":["activo","participativo","protagonista"],"explicacion":"El estudiante cumple un rol activo y participativo."}
    ],
    "intermedio": [
        {"tipo":"opcion","pregunta":"¿Cómo puede usarse la IA para personalizar la enseñanza?","opciones":["A. Haciendo exámenes aleatorios","B. Detectando el estilo de aprendizaje del estudiante","C. Asignando tareas iguales para todos","D. Usando robots"],"respuesta":"B","explicacion":"La IA puede detectar estilos de aprendizaje y adaptar el contenido."},
        {"tipo":"opcion","pregunta":"¿Qué ventaja ofrece la analítica de aprendizaje con IA?","opciones":["A. Aumenta la carga docente","B. Predice el rendimiento estudiantil","C. Crea exámenes más difíciles","D. Reduce la retroalimentación"],"respuesta":"B","explicacion":"La analítica puede predecir el rendimiento y detectar dificultades."},
        {"tipo":"vf","pregunta":"La IA no puede detectar patrones de aprendizaje. (V/F)","respuesta":"F","explicacion":"La IA sí puede detectar patrones para personalizar la enseñanza."},
        {"tipo":"abierta","pregunta":"¿Qué herramienta con IA conoces que apoye la evaluación formativa?","respuesta":["chatgpt","quizziz","kahoot","duolingo"],"explicacion":"Existen muchas herramientas con IA que brindan retroalimentación."},
        {"tipo":"abierta","pregunta":"Menciona un beneficio de usar IA en la educación.","respuesta":["personalizacion","retroalimentacion","deteccion temprana","seguimiento"],"explicacion":"La IA permite retroalimentación inmediata y personalización del aprendizaje."}
    ],
    "avanzado": [
        {"tipo":"opcion","pregunta":"¿Cuál de los siguientes no es un riesgo ético de la IA en educación?","opciones":["A. Sesgos algorítmicos","B. Violación de privacidad","C. Retroalimentación","D. Desigualdad en el acceso"],"respuesta":"C","explicacion":"La retroalimentación no es un riesgo, es una ventaja."},
        {"tipo":"opcion","pregunta":"¿Cómo puede la IA ayudar a estudiantes con necesidades especiales?","opciones":["A. Estandarizando actividades","B. Personalizando los contenidos","C. Usando textos largos","D. Aumentando el número de pruebas"],"respuesta":"B","explicacion":"La IA permite adaptar materiales a cada necesidad."},
        {"tipo":"vf","pregunta":"La IA puede generar retroalimentación automática según el desempeño. (V/F)","respuesta":"V","explicacion":"Es una de sus funciones clave en evaluación formativa."},
        {"tipo":"abierta","pregunta":"Menciona un dilema ético del uso de IA en la educación.","respuesta":["sesgo","privacidad","acceso desigual","transparencia"],"explicacion":"Se busca reconocer riesgos como el sesgo o la privacidad."},
        {"tipo":"abierta","pregunta":"¿Qué acciones puede tomar un docente al usar IA en la evaluación?","respuesta":["supervisar","verificar","validar","ajustar"],"explicacion":"Debe supervisar y validar lo que genera la IA."}
    ]
}

subtemas = {
    "retroalimentación": {
        "texto":"La retroalimentación es un proceso esencial en la educación que permite a los estudiantes conocer su desempeño y áreas de mejora. La retroalimentación efectiva debe ser específica, oportuna y constructiva, ayudando a los estudiantes a entender sus errores y cómo corregirlos. En el contexto de la IA, esta puede proporcionar retroalimentación instantánea, lo que permite a los estudiantes ajustar su aprendizaje en tiempo real.",
        "preguntas":[
            {"tipo":"opcion","pregunta":"¿Qué caracteriza a una retroalimentación efectiva?","opciones":["A. Ser vaga","B. Ser específica y constructiva","C. Ser solo positiva","D. No ser oportuna"],"respuesta":"B. Ser específica y constructiva","explicacion":"La retroalimentación efectiva debe ser específica y constructiva."},
            {"tipo":"vf","pregunta":"La retroalimentación instantánea no es útil para el aprendizaje. (V/F)","respuesta":"F","explicacion":"La retroalimentación instantánea es muy útil para el aprendizaje."},
            {"tipo":"abierta","pregunta":"Menciona un tipo de retroalimentación.","respuesta":["inmediata","constructiva","especifica"],"explicacion":"Existen diferentes tipos de retroalimentación, como la inmediata y constructiva."},
            {"tipo":"abierta","pregunta":"¿Por qué es importante la retroalimentación en el aprendizaje?","respuesta":["mejora","ajuste","correccion"],"explicacion":"La retroalimentación es importante porque permite mejorar y ajustar el aprendizaje."}
        ],
        "recursos":{"video":{"titulo":"Optimización de Retroalimentación Educativa con IA","url":"https://www.youtube.com/watch?v=ejemplo1"},"pdf":{"titulo":"Guía Completa de Retroalimentación Formativa","url":"https://example.com/retroalimentacion.pdf"}}
    },
    "personalización del aprendizaje": {
        "texto":"La personalización del aprendizaje se refiere a adaptar la enseñanza a las necesidades y estilos de aprendizaje de cada estudiante. Con la ayuda de la IA, es posible analizar datos de rendimiento y preferencias de los estudiantes para ofrecer contenido y actividades que se ajusten a sus características individuales. Esto no solo mejora la motivación, sino que también optimiza el proceso de aprendizaje.",
        "preguntas":[
            {"tipo":"opcion","pregunta":"¿Qué permite la personalización del aprendizaje?","opciones":["A. Un enfoque único para todos","B. Adaptar la enseñanza a cada estudiante","C. Ignorar las necesidades individuales","D. Aumentar la carga de trabajo"],"respuesta":"B","explicacion":"La personalización permite adaptar la enseñanza a las necesidades de cada estudiante."},
            {"tipo":"vf","pregunta":"La personalización del aprendizaje no mejora la motivación. (V/F)","respuesta":"F","explicacion":"La personalización del aprendizaje puede mejorar la motivación de los estudiantes."},
            {"tipo":"abierta","pregunta":"Menciona una herramienta que permita la personalización del aprendizaje.","respuesta":["plataformas de aprendizaje","ia","software educativo"],"explicacion":"Existen herramientas y plataformas que permiten personalizar el aprendizaje."},
            {"tipo":"abierta","pregunta":"¿Por qué es importante personalizar el aprendizaje?","respuesta":["necesidades","eficacia","motivacion"],"explicacion":"Es importante para atender las necesidades individuales y mejorar la eficacia del aprendizaje."}
        ],
        "recursos":{"video":{"titulo":"Personalizando el Aprendizaje con Inteligencia Artificial","url":"https://www.youtube.com/watch?v=ejemplo2"},"pdf":{"titulo":"Manual de Aprendizaje Adaptativo","url":"https://example.com/personalizacion.pdf"}}
    }
}

# -------------------------------
# Parámetros
# -------------------------------
PORC_MIN = 0.8  # 80%

# -------------------------------
# Utilidades
# -------------------------------
def normaliza(texto):
    if texto is None:
        return ""
    texto = texto.lower()
    texto = ''.join(ch for ch in unicodedata.normalize('NFD', texto) if unicodedata.category(ch) != 'Mn')  # quita tildes
    return texto

def eval_pregunta(preg, respuesta_usuario):
    """Devuelve True/False + texto-respuesta-correcta para registro"""
    tipo = preg.get("tipo")
    correct = False
    correcta_text = ""
    if tipo == "opcion":
        # respuesta en niveles es una letra "C" o similar
        correcta = preg.get("respuesta")
        correcta_text = correcta
        # permitir que el usuario haya seleccionado texto completo (ej: "C. Dar ...") o solo letra
        if respuesta_usuario is None:
            return False, correcta_text
        elegido = respuesta_usuario.strip()
        # si el usuario devolvió "C. ...", extraer primera letra
        elegido_letra = elegido[0].upper() if elegido != "" else ""
        if elegido_letra == str(correcta).strip().upper():
            correct = True
    elif tipo == "vf":
        correcta = preg.get("respuesta").strip().upper()
        correcta_text = correcta
        if respuesta_usuario is None:
            return False, correcta_text
        elegido = respuesta_usuario.strip().upper()
        # permitir respuestas 'V'/'F' o 'Verdadero'/'Falso'
        elegido = "V" if elegido.startswith("V") else ("F" if elegido.startswith("F") else elegido)
        if elegido == correcta:
            correct = True
    elif tipo == "abierta":
        # respuesta_usuario texto -> verificamos si contiene alguna palabra clave
        keywords = preg.get("respuesta", [])
        correcta_text = ", ".join(keywords)
        usr = normaliza(respuesta_usuario)
        for kw in keywords:
            if normaliza(kw) in usr:
                correct = True
                break
    else:
        correct = False
    return correct, correcta_text

def iniciar_session_keys():
    # inicializa session_state si no existe
    if "tema" not in st.session_state:
        st.session_state["tema"] = None
    if "nivel_actual" not in st.session_state:
        st.session_state["nivel_actual"] = None
    if "aprobado_básico" not in st.session_state:
        st.session_state["aprobado_básico"] = False
    if "aprobado_intermedio" not in st.session_state:
        st.session_state["aprobado_intermedio"] = False
    if "historial" not in st.session_state:
        st.session_state["historial"] = []  # registros de exámenes
    if "respuestas_temp" not in st.session_state:
        st.session_state["respuestas_temp"] = {}  # respuestas por examen actual
    if "puntos_temp" not in st.session_state:
        st.session_state["puntos_temp"] = []  # lista boolean de correctas en examen actual

# -------------------------------
# Interfaz
# -------------------------------
st.set_page_config(page_title="Examen Adaptativo - Evaluación Formativa con IA", layout="centered")
st.title("Examen Adaptativo — Evaluación Formativa con IA")

iniciar_session_keys()

col1, col2 = st.columns([2,1])
with col1:
    st.header("1) Elige un tema para el refuerzo")
    tema_elegido = st.selectbox("Tema (será usado en caso de refuerzo):", ["retroalimentación","personalización del aprendizaje"])
    if st.button("Confirmar tema"):
        st.session_state["tema"] = tema_elegido
        st.success(f"Tema seleccionado: {tema_elegido}")

with col2:
    st.write("")  # espacio
    st.markdown("**Progreso de la ruta**")
    st.write(f"- Aprobado Básico: {'✅' if st.session_state['aprobado_básico'] else '❌'}")
    st.write(f"- Aprobado Intermedio: {'✅' if st.session_state['aprobado_intermedio'] else '❌'}")

st.markdown("---")
st.header("2) Elige el nivel del examen")
cols = st.columns(3)
with cols[0]:
    if st.button("Iniciar BÁSICO"):
        st.session_state["nivel_actual"] = "básico"
        st.session_state["respuestas_temp"] = {}
        st.session_state["puntos_temp"] = []
with cols[1]:
    if st.session_state["aprobado_básico"]:
        if st.button("Iniciar INTERMEDIO"):
            st.session_state["nivel_actual"] = "intermedio"
            st.session_state["respuestas_temp"] = {}
            st.session_state["puntos_temp"] = []
    else:
        if st.button("Iniciar INTERMEDIO"):
            st.warning("Debes aprobar el nivel BÁSICO primero.")
with cols[2]:
    if st.session_state["aprobado_intermedio"]:
        if st.button("Iniciar AVANZADO"):
            st.session_state["nivel_actual"] = "avanzado"
            st.session_state["respuestas_temp"] = {}
            st.session_state["puntos_temp"] = []
    else:
        if st.button("Iniciar AVANZADO"):
            st.warning("Debes aprobar el nivel INTERMEDIO primero.")

# -------------------------------
# Mostrar examen según nivel_actual
# -------------------------------
nivel = st.session_state.get("nivel_actual")
if nivel:
    st.markdown(f"### Examen: {nivel.upper()}")
    preguntas = niveles[nivel]
    total = len(preguntas)
    # track index: cuántas respondidas (guardamos respuestas en session_state['respuestas_temp'])
    respuestas = st.session_state.get("respuestas_temp", {})
    # Mostrar preguntas una por una o todas
    st.info("Responde todas las preguntas y luego presiona 'Terminar examen'.")

    for i, preg in enumerate(preguntas):
        st.write(f"**{i+1}) {preg['pregunta']}**")
        key = f"{nivel}_q_{i}"
        if preg["tipo"] == "opcion":
            elegido = st.radio("", preg["opciones"], key=key)
            respuestas[str(i)] = elegido
        elif preg["tipo"] == "vf":
            elegido = st.radio("", ["V","F"], key=key)
            respuestas[str(i)] = elegido
        elif preg["tipo"] == "abierta":
            elegido = st.text_input("Escribe tu respuesta aquí:", key=key)
            respuestas[str(i)] = elegido
        # mostrar progreso parcial por pregunta respondida
        responded_count = sum(1 for v in respuestas.values() if v is not None and v != "")
        progreso = responded_count / total
        st.progress(progreso)
        st.write("---")

    st.session_state["respuestas_temp"] = respuestas

    if st.button("Terminar examen"):
        # evaluar
        correctos = 0
        detalles = []
        for i, preg in enumerate(preguntas):
            usr = respuestas.get(str(i), "")
            es_correcto, correcta_text = eval_pregunta(preg, usr)
            detalles.append({
                "n": i+1,
                "pregunta": preg["pregunta"],
                "tu_respuesta": usr,
                "correcta": correcta_text,
                "explicacion": preg.get("explicacion",""),
                "es_correcto": es_correcto
            })
            if es_correcto:
                correctos += 1
        nota = correctos / total
        aprobado = nota >= PORC_MIN

        # guardar en historial
        registro = {
            "fecha": str(datetime.datetime.now()),
            "tipo_examen": "nivel",
            "nivel": nivel,
            "tema": st.session_state.get("tema"),
            "nota": nota,
            "correctos": correctos,
            "total": total,
            "detalles": detalles
        }
        st.session_state["historial"].append(registro)

        # marcar aprobaciones en ruta
        if nivel == "básico" and aprobado:
            st.session_state["aprobado_básico"] = True
        if nivel == "intermedio" and aprobado:
            st.session_state["aprobado_intermedio"] = True

        # mostrar resultado
        st.success(f"Tu nota: {round(nota*100,1)}%  ({correctos}/{total})")
        if aprobado:
            st.balloons()
            st.write("¡Has aprobado este nivel!")
            # botón para ir al siguiente nivel (si existe)
            if nivel == "básico":
                if st.button("Ir a INTERMEDIO"):
                    st.session_state["nivel_actual"] = "intermedio"
                    st.session_state["respuestas_temp"] = {}
                    st.session_state["puntos_temp"] = []
                    st.experimental_rerun()
            elif nivel == "intermedio":
                if st.button("Ir a AVANZADO"):
                    st.session_state["nivel_actual"] = "avanzado"
                    st.session_state["respuestas_temp"] = {}
                    st.session_state["puntos_temp"] = []
                    st.experimental_rerun()
        else:
            st.error("No alcanzaste el porcentaje mínimo. Tienes estas opciones:")
            colr1, colr2 = st.columns(2)
            with colr1:
                if st.button("Realizar REFUERZO del tema seleccionado"):
                    # iniciar refuerzo
                    st.session_state["nivel_actual"] = "refuerzo"
                    st.session_state["respuestas_temp"] = {}
                    st.session_state["puntos_temp"] = []
                    st.experimental_rerun()
            with colr2:
                if st.button("Ver RECURSOS del tema"):
                    st.session_state["ver_recursos"] = True
                    st.experimental_rerun()

# -------------------------------
# Refuerzo
# -------------------------------
if st.session_state.get("nivel_actual") == "refuerzo":
    tema = st.session_state.get("tema")
    if tema is None:
        st.warning("Primero selecciona un tema para refuerzo en el paso 1.")
    else:
        st.markdown(f"### Refuerzo: {tema}")
        preguntas_ref = subtemas[tema]["preguntas"]
        total = len(preguntas_ref)
        respuestas = st.session_state.get("respuestas_temp", {})
        for i, preg in enumerate(preguntas_ref):
            st.write(f"**{i+1}) {preg['pregunta']}**")
            key = f"ref_{i}"
            if preg["tipo"] == "opcion":
                elegido = st.radio("", preg["opciones"], key=key)
                respuestas[str(i)] = elegido
            elif preg["tipo"] == "vf":
                elegido = st.radio("", ["V","F"], key=key)
                respuestas[str(i)] = elegido
            elif preg["tipo"] == "abierta":
                elegido = st.text_input("Escribe tu respuesta aquí:", key=key)
                respuestas[str(i)] = elegido
            responded_count = sum(1 for v in respuestas.values() if v is not None and v != "")
            progreso = responded_count / total
            st.progress(progreso)
            st.write("---")
        st.session_state["respuestas_temp"] = respuestas

        if st.button("Terminar refuerzo"):
            correctos = 0
            detalles = []
            for i, preg in enumerate(preguntas_ref):
                usr = respuestas.get(str(i), "")
                es_correcto, correcta_text = eval_pregunta(preg, usr)
                detalles.append({
                    "n": i+1,
                    "pregunta": preg["pregunta"],
                    "tu_respuesta": usr,
                    "correcta": correcta_text,
                    "explicacion": preg.get("explicacion",""),
                    "es_correcto": es_correcto
                })
                if es_correcto:
                    correctos += 1
            nota = correctos / total
            aprobado = nota >= PORC_MIN

            registro = {
                "fecha": str(datetime.datetime.now()),
                "tipo_examen": "refuerzo",
                "nivel": "refuerzo",
                "tema": tema,
                "nota": nota,
                "correctos": correctos,
                "total": total,
                "detalles": detalles
            }
            st.session_state["historial"].append(registro)

            st.success(f"Tu nota en refuerzo: {round(nota*100,1)}%  ({correctos}/{total})")
            if aprobado:
                st.balloons()
                st.write("Has aprobado el refuerzo. Ahora puedes pasar al siguiente nivel.")
                if st.button("Siguiente nivel"):
                    # si venías de básico, ir a intermedio; si venías de intermedio, ir a avanzado
                    # para simplicidad, detectamos en historial últimos examen de 'nivel' no aprobado
                    # asumimos si no aprobó básico le permitirá ir a intermedio tras refuerzo
                    if not st.session_state["aprobado_básico"]:
                        st.session_state["aprobado_básico"] = True
                        st.session_state["nivel_actual"] = "intermedio"
                        st.session_state["respuestas_temp"] = {}
                        st.experimental_rerun()
                    elif not st.session_state["aprobado_intermedio"]:
                        st.session_state["aprobado_intermedio"] = True
                        st.session_state["nivel_actual"] = "avanzado"
                        st.session_state["respuestas_temp"] = {}
                        st.experimental_rerun()
            else:
                st.error("No aprobaste el refuerzo. Revisa los recursos disponibles.")
                if st.button("Ver recursos"):
                    st.session_state["ver_recursos"] = True
                    st.experimental_rerun()

# -------------------------------
# Recursos
# -------------------------------
if st.session_state.get("ver_recursos"):
    tema = st.session_state.get("tema")
    if tema:
        st.markdown(f"### Recursos — {tema}")
        rec = subtemas[tema]["recursos"]
        if "video" in rec:
            st.write(f"**Video:** [{rec['video']['titulo']}]({rec['video']['url']})")
        if "pdf" in rec:
            st.write(f"**PDF:** [{rec['pdf']['titulo']}]({rec['pdf']['url']})")
    else:
        st.warning("No hay tema seleccionado.")

# -------------------------------
# Mostrar historial y descarga .txt
# -------------------------------
st.markdown("---")
st.header("Historial y descargas")
hist = st.session_state.get("historial", [])
if len(hist) == 0:
    st.write("Aún no se han realizado exámenes.")
else:
    for i, reg in enumerate(reversed(hist), start=1):
        st.write(f"**{i}. {reg['tipo_examen'].upper()} - {reg.get('nivel','')} - {reg.get('tema','')}**  — {reg['fecha']}")
        st.write(f"Nota: {round(reg['nota']*100,1)}%  ({reg['correctos']}/{reg['total']})")
        if st.checkbox(f"Ver detalles {i}", key=f"det_{i}"):
            for d in reg["detalles"]:
                st.write(f"{d['n']}) {d['pregunta']}")
                st.write(f"- Tu respuesta: {d['tu_respuesta']}")
                st.write(f"- Respuesta correcta (o palabras clave): {d['correcta']}")
                st.write(f"- Explicación: {d['explicacion']}")
                st.write(f"- Correcto: {'Sí' if d['es_correcto'] else 'No'}")
                st.write("")

    # preparar texto para descarga
    def genera_txt(historial):
        lines = []
        for reg in historial:
            lines.append("========================================")
            lines.append(f"FECHA: {reg['fecha']}")
            lines.append(f"TIPO: {reg['tipo_examen']}")
            if reg.get("nivel"):
                lines.append(f"NIVEL: {reg['nivel']}")
            lines.append(f"TEMA (refuerzo si aplica): {reg.get('tema')}")
            lines.append(f"NOTA: {round(reg['nota']*100,1)}% ({reg['correctos']}/{reg['total']})")
            lines.append("")
            for d in reg["detalles"]:
                lines.append(f"{d['n']}) {d['pregunta']}")
                lines.append(f"Tu respuesta: {d['tu_respuesta']}")
                lines.append(f"Respuesta correcta / keywords: {d['correcta']}")
                lines.append(f"Explicación: {d['explicacion']}")
                lines.append(f"Correcto: {'Sí' if d['es_correcto'] else 'No'}")
                lines.append("")
            lines.append("\n")
        return "\n".join(lines)

    contenido = genera_txt(hist)
    nombre = f"resultados_examen_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    st.download_button("Descargar resultados (.txt)", data=contenido, file_name=nombre, mime="text/plain")

st.markdown("---")
st.caption("Hecho con ♥ — Si quieres, puedo adaptar diseño, mensajes o formato del .txt.")
