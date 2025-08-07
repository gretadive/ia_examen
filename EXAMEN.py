import random

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
# FUNCIONES DEL EXAMEN
# -------------------------------

def hacer_pregunta(p):
    print("\n📌", p["pregunta"])
    if p["tipo"] == "opcion":
        for op in p["opciones"]:
            print(op)
        r = input("Tu respuesta: ").strip().upper()
        if r == p["respuesta"]:
            print("✅ ¡Correcto!")
            return True
        else:
            print("❌ Incorrecto. Revisa el concepto.")
            print("📘", p["explicacion"])
            return False

    elif p["tipo"] == "vf":
        r = input("Responde V o F: ").strip().upper()
        if r == p["respuesta"]:
            print("✅ ¡Correcto!")
            return True
        else:
            print("❌ Incorrecto. Revisa el concepto.")
            print("📘", p["explicacion"])
            return False

    elif p["tipo"] == "abierta":
        r = input("Tu respuesta: ").strip().lower()
        for val in p["respuesta"]:
            if val in r:
                print("✅ ¡Correcto!")
                return True
        print("❌ Incorrecto. Revisa el concepto.")
        print("📘", p["explicacion"])
        return False


def examen_nivel(nombre_nivel):
    print(f"\n📚 Nivel: {nombre_nivel.upper()} (Debes acertar al menos 4 de 5)")
    preguntas = random.sample(niveles[nombre_nivel], 5)
    puntaje = 0
    for p in preguntas:
        if hacer_pregunta(p):
            puntaje += 1
    print(f"\nResultado: {puntaje}/5")
    return puntaje >= 4


# -------------------------------
# FLUJO ADAPTATIVO
# -------------------------------

print("🎓 EXAMEN ADAPTATIVO: Evaluación Formativa con IA")
print("Comenzarás con el nivel BÁSICO.")
print("Debes aprobar con al menos 80% para avanzar.\n")

if examen_nivel("básico"):
    print("\n🎉 ¡Bien hecho! Pasas al nivel INTERMEDIO.")
    if examen_nivel("intermedio"):
        print("\n🌟 ¡Excelente! Ahora el nivel AVANZADO.")
        if examen_nivel("avanzado"):
            print("\n🏆 ¡Felicidades! Has completado exitosamente los tres niveles.")
        else:
            print("\n🔁 No aprobaste el nivel avanzado. Inténtalo nuevamente luego.")
    else:
        print("\n🔁 No aprobaste el nivel intermedio. Intenta reforzar tus conocimientos.")
else:
    print("\n🔁 No aprobaste el nivel básico. Refuerza tus conceptos antes de continuar.")
