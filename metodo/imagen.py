import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import time

dibujo_hecho = False
json_subido = False  # ✅ NUEVO

informee="Persona 1 le faltan gafas y guantes"

# --- CONTENEDOR SUPERIOR ---
with st.container():
    col1, space, col2 = st.columns([1.5, 0.1, 0.8])

    with col1:
        st.header("Inferencia en imágenes")
        with st.expander("Cómo utilizar este método"):
            st.write('''
                1. Ajusta los parámetros
                2. Selecciona la imagen a analizar
                3. La comparación de imágenes se mostrará a continuación. Puede descargarla haciendo clic en el botón de descarga.
            ''')
        uploaded_file = st.file_uploader(" ", label_visibility="collapsed", type=["jpg", "jpeg", "png"])
        image = None
        if uploaded_file is not None:
            image = Image.open(uploaded_file)

    with space:
        st.markdown(
            '''
            <div style="display: flex; justify-content: center;">
                <div class="divider-vertical-line"></div>
            </div>
            <style>
                .divider-vertical-line {
                    border-left: 1px solid rgba(49, 51, 63, 0.2);
                    height: 375px;
                }
            </style>
            ''',
            unsafe_allow_html=True
        )

    with col2:
        st.subheader("Parámetros")

        st.markdown("Detección en zonas:")
        options = ["Activa", "Inactiva"]
        selection = st.pills(" ", options, selection_mode="single", label_visibility="collapsed")
        st.session_state.selection = selection  # Guardar en estado

        st.markdown("Clases detectadas:")
        coll1, coll2 = st.columns(2)
        with coll1:
            gafas = st.checkbox("Gafas")
            guantes = st.checkbox("Guantes")
        with coll2:
            chaleco = st.checkbox("Chaleco")
            casco = st.checkbox("Casco")

        st.markdown("Confianza:")
        confianza = st.slider("Confianza:", 0, 50, 100, label_visibility="collapsed")

# --- NUEVO CONTENEDOR: SOLO SI SELECCIÓN ES ACTIVA ---
if 'selection' in st.session_state and st.session_state.selection == "Activa" and uploaded_file is not None:
    st.divider()
    with st.container():
        st.subheader("Determina las zonas de detección a continuación:")

        col_canvas1, spaceee, col_canvas2 = st.columns([0.8,0.1, 1.5])

        with col_canvas2:
            st.write("Sube un json con las coordenadas de la zona...")
            uploaded_json = st.file_uploader(" ", label_visibility="collapsed", type=["json"], key="json")
            if uploaded_json is not None:
                json_subido = True  # ✅ CAMBIO

        with spaceee:
            st.markdown(
                '''
                <div style="display: flex; justify-content: center;">
                    <div class="divider-vertical-line"></div>
                </div>
                <style>
                    .divider-vertical-line {
                        border-left: 1px solid rgba(49, 51, 63, 0.2);
                        height: 300px;
                    }
                </style>
                ''',
                unsafe_allow_html=True
            )

        with col_canvas1:
            st.write("...o dibújala sobre la imagen.")
            resized_image = image.resize((300, 300), resample=Image.Resampling.LANCZOS)
            canvas_result = st_canvas(
                fill_color="rgba(255, 255, 0, 0.2)",  # Zona amarilla translúcida
                stroke_width=2,
                stroke_color="#FFFF00",
                background_image=resized_image,
                update_streamlit=True,
                height=220,
                width=220,
                drawing_mode="polygon",
                key="canvas_mini",
                display_toolbar=False
            )
            if canvas_result.json_data is not None and len(canvas_result.json_data["objects"]) > 0:
                dibujo_hecho = True  # ✅ CAMBIO

# --- CONTENEDOR DE RESULTADOS (con condiciones actualizadas) ---
mostrar_resultados = False  # ✅ NUEVO

if uploaded_file is not None:
    if st.session_state.selection == "Inactiva":
        mostrar_resultados = True
    elif st.session_state.selection == "Activa" and (json_subido or dibujo_hecho):
        mostrar_resultados = True

if mostrar_resultados:
    st.divider()
    with st.container():
        st.subheader("Resultados de la inferencia")
        
        
        col1, col2 = st.columns([1.5, 1.5])

        with col1:
            st.image(image, caption="Imagen original", use_container_width=True)

        with col2:
            st.image(image, caption="Resultado de la inferencia", use_container_width=True)
        
        col1, col2 = st.columns([1.5, 1.5])
        with col1:
            
        
            st.subheader("Informe de resultados:")
            if informee!="":
                st.error(informee)
            else:
                st.success("No se han detectado anomalías en la imagen.")

        with col2:
            options = ["Resultado", "JSON zona dibujada", "Informe"]
            st.subheader("Descargar resultados:")

            selection = st.segmented_control(
                " ", options, selection_mode="single", label_visibility="collapsed"
            )

            if selection == "Resultado":
                st.download_button(
                    label="Descargar resultado",
                    data=uploaded_json.read(),
                    file_name="resultado_inferencia.png",
                    mime="image/png"
                )

            elif selection == "JSON zona dibujada":
                st.download_button(
                    label="Descargar json",
                    data=canvas_result.json_data,
                    file_name="zona_dibujada.json",
                    mime="application/json"
                )

            elif selection == "Informe":
                st.download_button(
                    label="Descargar informe",
                    data="informe.txt",
                    file_name="informe.txt",
                    mime="text/plain"
                )