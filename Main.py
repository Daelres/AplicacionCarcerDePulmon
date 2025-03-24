import streamlit as st
import pandas as pd
import joblib

# Configuración de la página
st.set_page_config(page_title="Asistente de Detección de Cáncer de Pulmón", layout="centered")

# Título, autor e instrucciones
st.title("Asistente de Detección de Cáncer de Pulmón")
st.markdown("#### Autor: Daniel Restrepo - David Chia")
st.write("""
Bienvenido a la aplicación de detección de cáncer de pulmón.

Por favor, llena todos los campos en la pestaña **Datos de Entrada**:
- **Género (m/f)**  
- **Edad (30 a 90)**  
- **Resto de variables (selecciona 2 para 'Sí' y 1 para 'No')**  

Luego, presiona el botón **Predecir** para determinar si existe probabilidad de cáncer de pulmón.
La predicción se mostrará en la pestaña **Resultado**.
""")

# Creación de pestañas para entrada y resultado
tab1, tab2 = st.tabs(["Datos de Entrada", "Resultado"])

with tab1:
    st.header("Ingreso de Datos")

    # 1. Género
    gender = st.radio("Seleccione su género:", options=["m", "f"], index=0)

    # 2. Edad
    age = st.slider("Edad", min_value=30, max_value=90, step=1, value=30)

    st.write("Responde con **2** para 'Sí' y **1** para 'No' en las siguientes preguntas:")

    # 3. SMOKING
    smoking = st.radio("¿Fuma habitualmente? (SMOKING)", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 4. YELLOW_FINGERS
    yellow_fingers = st.radio("¿Dedos amarillos? (YELLOW_FINGERS)", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 5. ANXIETY
    anxiety = st.radio("¿Ansiedad? (ANXIETY)", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 6. PEER_PRESSURE
    peer_pressure = st.radio("¿Presión social? (PEER_PRESSURE)", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 7. CHRONIC DISEASE
    chronic_disease = st.radio("¿Padece enfermedad crónica? (CHRONIC DISEASE)", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 8. FATIGUE  (notar espacio al final)
    fatigue = st.radio("¿Fatiga? (FATIGUE )", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 9. ALLERGY  (notar espacio al final)
    allergy = st.radio("¿Alergia? (ALLERGY )", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 10. WHEEZING
    wheezing = st.radio("¿Sibilancias? (WHEEZING)", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 11. ALCOHOL CONSUMING
    alcohol_consuming = st.radio("¿Consume alcohol? (ALCOHOL CONSUMING)", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 12. COUGHING
    coughing = st.radio("¿Tos? (COUGHING)", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 13. SHORTNESS OF BREATH
    shortness_of_breath = st.radio("¿Falta de aliento? (SHORTNESS OF BREATH)", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 14. SWALLOWING DIFFICULTY
    swallowing_difficulty = st.radio("¿Dificultad para tragar? (SWALLOWING DIFFICULTY)", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # 15. CHEST PAIN
    chest_pain = st.radio("¿Dolor en el pecho? (CHEST PAIN)", options=[1, 2], format_func=lambda x: "No" if x == 1 else "Sí", index=0)

    # Se crea un DataFrame con los datos ingresados
    datos_entrada = pd.DataFrame({
        'GENDER': [gender],
        'AGE': [age],
        'SMOKING': [smoking],
        'YELLOW_FINGERS': [yellow_fingers],
        'ANXIETY': [anxiety],
        'PEER_PRESSURE': [peer_pressure],
        'CHRONIC DISEASE': [chronic_disease],
        'FATIGUE ': [fatigue],
        'ALLERGY ': [allergy],
        'WHEEZING': [wheezing],
        'ALCOHOL CONSUMING': [alcohol_consuming],
        'COUGHING': [coughing],
        'SHORTNESS OF BREATH': [shortness_of_breath],
        'SWALLOWING DIFFICULTY': [swallowing_difficulty],
        'CHEST PAIN': [chest_pain]
    })

    if st.button("Predecir"):
        try:
            # Cargar el preprocesador (data_lung_cancer.pkl) 
            preprocesador = joblib.load("Recursos/Modelos/data_lung_cancer.pkl")
            datos_procesados = preprocesador.transform(datos_entrada)

            # Cargar el modelo predictivo (decision_tree_model.pkl)
            modelo = joblib.load("Recursos/Modelos/decision_tree_model.pkl")
            prediccion = modelo.predict(datos_procesados)

            # Almacenar la predicción en el estado de la sesión para compartirla entre pestañas
            st.session_state["prediccion"] = int(prediccion[0])
            st.success("¡Predicción realizada exitosamente!")
        except Exception as e:
            st.error(f"Error al cargar el modelo o realizar la predicción: {e}")

with tab2:
    st.header("Resultado de la Predicción")
    if "prediccion" in st.session_state:
        resultado = st.session_state["prediccion"]
        if resultado == 0:
            st.write("El paciente **NO** presenta indicios de cáncer de pulmón.")
            st.image("https://source.unsplash.com/640x480/?healthy,lungs", caption="Pulmones saludables")
        else:
            st.write("El paciente **PRESENTA** indicios de cáncer de pulmón. Se recomienda consultar a un especialista.")
            st.image("https://source.unsplash.com/640x480/?lung,cancer", caption="Posible cáncer de pulmón detectado")
    else:
        st.info("Aún no se ha realizado ninguna predicción. Ingresa los datos en la pestaña **Datos de Entrada** y presiona **Predecir**.")
