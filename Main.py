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
Utiliza los controles deslizantes de la pestaña **Datos de Entrada** para ingresar la edad (entre 30 y 90 años) y la cantidad de cigarrillos consumidos por día (entre 0 y 40). 
Luego, presiona el botón **Predecir** para determinar si existe probabilidad de cáncer de pulmón. 
La predicción se mostrará en la pestaña **Resultado**.
""")

# Creación de pestañas para entrada y resultado
tab1, tab2 = st.tabs(["Datos de Entrada", "Resultado"])

with tab1:
    st.header("Ingreso de Datos")
    # Captura de datos mediante sliders
    edad = st.slider("Edad", min_value=30, max_value=90, step=1, value=30)
    cigarrillos = st.slider("Cigarrillos por día", min_value=0, max_value=40, step=1, value=0)

    # Se crea un DataFrame con los datos ingresados
    datos_entrada = pd.DataFrame({
        "edad": [edad],
        "cigarrillos": [cigarrillos]
    })

    if st.button("Predecir"):
        try:
            # Cargar el modelo de persistencia de datos (por ejemplo, un preprocesador)
            preprocesador = joblib.load("Recursos\Modelos\data_lung_cancer.pkl")
            datos_procesados = preprocesador.transform(datos_entrada)

            # Cargar el modelo predictivo
            modelo = joblib.load("Recursos\Modelos\decision_tree_model.pkl")
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
        st.info("Aún no se ha realizado ninguna predicción. Por favor ingresa los datos en la pestaña **Datos de Entrada** y presiona **Predecir**.")
