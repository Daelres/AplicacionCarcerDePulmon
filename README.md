# **Aplicación de Detección de Cáncer de Pulmón**
Este proyecto consiste en una aplicación desarrollada en Python que utiliza técnicas de aprendizaje automático para predecir la probabilidad de que un paciente tenga cáncer de pulmón, basándose en características clínicas y demográficas. La interfaz de usuario está construida con Streamlit, lo que permite una interacción sencilla y efectiva.

#### Estructura del Proyecto
Cancer_Pulmon.ipynb: Notebook de Jupyter donde se realiza la exploración de datos, preprocesamiento y entrenamiento del modelo de machine learning.

API.py: Script que define una API para interactuar con el modelo entrenado.

Main.py: Archivo principal que ejecuta la aplicación.

StreamLitProject.py: Script que contiene la implementación de la interfaz de usuario utilizando Streamlit.

requirements.txt: Lista de dependencias necesarias para ejecutar el proyecto.

Dockerfile: Archivo para la creación de una imagen Docker del proyecto.

Recursos/: Carpeta que contiene recursos adicionales utilizados en el proyecto.

.idea/: Carpeta generada por el entorno de desarrollo (por ejemplo, PyCharm).

 #### Requisitos
Antes de ejecutar la aplicación, asegúrate de tener instalado:

Python 3.7 o superior

pip (gestor de paquetes de Python)

Instala las dependencias necesarias con:

bash
Copiar código
pip install -r requirements.txt
 Creación del Droplet y configuración
 ##### 1. Crear un Droplet en DigitalOcean
Se muestra el panel de configuración para la creación del droplet.

![Imagen de WhatsApp 2025-05-28 a las 21 06 40_10b16f40](https://github.com/user-attachments/assets/f222652a-3902-4ae7-966a-623de703679f)

##### 2. Seleccionar el sistema operativo y especificaciones del servidor
Configuración de la distribución de Debian y los recursos asignados al droplet.
![Imagen de WhatsApp 2025-05-28 a las 21 06 53_83a98fbc](https://github.com/user-attachments/assets/ef657754-b5fd-4807-b5f6-cdffc2590e56)


##### 3. Confirmación de la creación del droplet y acceso a su IP
Visualización de la IP pública del droplet creada correctamente.
![Imagen de WhatsApp 2025-05-28 a las 21 09 37_5c661aae](https://github.com/user-attachments/assets/8866f29d-d320-4cf0-8bd5-05c4eee64a30)


#### 🔧 Actualización, Configuración y Verificación de Docker
##### 1. Actualizar repositorios del sistema
Se ejecuta sudo apt update para asegurar que los repositorios estén actualizados.
![Imagen de WhatsApp 2025-05-28 a las 21 13 01_d339b571](https://github.com/user-attachments/assets/1958254a-accd-48c0-beb6-158608d884bd)


##### 2. Instalar dependencias necesarias para Docker
Instalación de paquetes como apt-transport-https, ca-certificates, curl, etc.
![Imagen de WhatsApp 2025-05-28 a las 21 15 50_33993e26](https://github.com/user-attachments/assets/14198b3d-0190-44a7-9525-47f884bd8c0c)


##### 3. Añadir la clave GPG oficial de Docker
Autenticación del repositorio oficial para asegurar descargas confiables.
![Imagen de WhatsApp 2025-05-28 a las 21 16 30_e15880e5](https://github.com/user-attachments/assets/ea577cf7-7feb-4019-857f-913a45fcbcc2)


##### 4. Configurar el repositorio de Docker
Se añade el repositorio de Docker a la lista de fuentes del sistema.


##### 5. Instalar el motor de Docker
Comando para instalar Docker Engine tras configurar los repositorios.
![Imagen de WhatsApp 2025-05-28 a las 21 17 35_5b6feed6](https://github.com/user-attachments/assets/e8704dfb-7a42-46e5-995d-d0da26da2cf4)


##### 6. Verificar instalación de Docker
Se comprueba que Docker fue instalado exitosamente usando docker --version.
![Imagen de WhatsApp 2025-05-28 a las 21 18 19_5aca2aa4](https://github.com/user-attachments/assets/16d44928-88f0-45e0-b6ea-cb3ca974eb44)


##### 7. Iniciar y habilitar servicios de Docker
Activación automática de Docker al arrancar el sistema.
![Imagen de WhatsApp 2025-05-28 a las 21 18 47_64014bd4](https://github.com/user-attachments/assets/234f95e0-906a-4730-b2a5-1a40a8028096)


##### 8. Reiniciar el servidor para aplicar cambios
Se reinicia el droplet para asegurar que todos los servicios estén funcionando correctamente.
![Imagen de WhatsApp 2025-05-28 a las 21 20 43_b9a267f9](https://github.com/user-attachments/assets/856e7c18-8102-4c97-ba22-c84561fc7b05)


#### ⚙️ Ejecución de la API y Verificación
##### 1. Clonar el repositorio que contiene la API
Se descarga el proyecto desde GitHub al droplet.
![Imagen de WhatsApp 2025-05-28 a las 21 22 59_8174f847](https://github.com/user-attachments/assets/d57b1a5c-5d4c-4c09-9f64-e88eb4de9ba6)


##### 2. Construir la imagen Docker de la API
Uso de docker build para generar la imagen a partir del Dockerfile.
![Imagen de WhatsApp 2025-05-28 a las 21 25 12_6ebf831c](https://github.com/user-attachments/assets/52effb91-9c24-45b1-8b26-edbc2e2d11c5)


##### 3. Verificar la creación de la imagen
Se confirma que la imagen fue creada correctamente en el sistema.

![Imagen de WhatsApp 2025-05-28 a las 21 26 44_b0e48b90](https://github.com/user-attachments/assets/ccc0e107-337d-47e5-810b-74830da208d6)

##### 4. Ejecutar el contenedor en el puerto 8000
Despliegue de la API en el puerto 8000 del droplet.
![Imagen de WhatsApp 2025-05-28 a las 21 45 38_a3e0e2b1](https://github.com/user-attachments/assets/2367a85e-5e89-498f-812b-7d75353727cd)


##### 5. Verificar que el contenedor se esté ejecutando
Se revisa que el contenedor está activo y corriendo.
![Imagen de WhatsApp 2025-05-28 a las 21 45 57_7e3d3d17](https://github.com/user-attachments/assets/d1d05173-76ba-46a2-ae3c-ba94df6def5b)


##### 6. Abrir el puerto 8000 en el firewall del droplet
Se configura el firewall para permitir tráfico entrante en el puerto 8000.
![Imagen de WhatsApp 2025-05-28 a las 21 31 00_89bd16d0](https://github.com/user-attachments/assets/f2ceba34-f794-4ee0-8abc-218a68ed6900)

##### 7. Hacer etición de pruebas al servidor
   Se ejecutan pruebas para verificar el correcto funcionamiento del servidor y su API.
![Imagen de WhatsApp 2025-05-28 a las 21 47 00_261c4237](https://github.com/user-attachments/assets/c57eedd5-0454-4852-b9f2-a1f6a6b4a700)

##### 8. Consultar en swagger con ip y puerto asignados
    Acceso a Swagger UI mediante la IP y puerto asignados para explorar y probar las rutas de la API.
![Imagen de WhatsApp 2025-05-28 a las 21 47 31_6d470344](https://github.com/user-attachments/assets/70a9184b-15b7-4643-80b7-2342115e6899)

##### 9. Realizar peticion de pruebas
Se envía una solicitud de prueba a uno de los endpoints para comprobar la respuesta del servidor. 
![Imagen de WhatsApp 2025-05-28 a las 21 48 05_3104e65d](https://github.com/user-attachments/assets/00eafa8b-ef3d-4433-8dd4-73ffe4ef5bf4)


# **Link del repositorio de la app realizada en kotlin para movil**

https://github.com/Daelres/CancerDePulmon.git


