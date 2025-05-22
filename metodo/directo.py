import streamlit as st
import cv2
from PIL import Image
import time

# Simula captura continua de cámara
def camera_stream():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("No se pudo acceder a la cámara.")
        return

    # Crea contenedor para mostrar imagen
    img_placeholder = st.empty()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                st.warning("No se pudo capturar imagen.")
                break

            # Convertir BGR a RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)

            # Mostrar en pantalla
            img_placeholder.image(img, caption="Cámara en vivo", use_container_width=True)

            # Esperar 0.5 segundos
            time.sleep(0.1)

    except KeyboardInterrupt:
        st.write("Captura interrumpida.")
    finally:
        cap.release()

# Título
st.title("🔴 Inferencia en tiempo real - Simulación de cámara")

# Botón para iniciar
if st.button("Iniciar cámara"):
    camera_stream()