import streamlit as st
from PIL import Image

# Inicializar sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True

# Función para login/tutorial
def home():
    st.title("Demo | Monitoreo de uso de EPIs")
    st.video("archivos/DETECCION_EPIS_EJEMPLO_corto.mp4", 
             format="video/mp4",
             loop=True, autoplay=True, muted=True)
    

# Función para logout
def logout():
    st.title("Aplicación finalizada")
    
    st.stop()

def tutorial():
    st.title("Tutorial")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Acerca de la API")
        st.write("Desarrollado por Oesía Networks, este servicio permite " \
        "al usuario detectar incumplimientos en el uso de EPIs mediante visión por computadora." \
        "El sistema está diseñado para detectar, ")
    with col2:
        st.video("archivos/DETECCION_EPIS_EJEMPLO_corto.mp4",loop=True, autoplay=True, muted=True)

    st.subheader("¿Cómo funciona?")
    st.write("El usuario puede subir " \
        "imágenes o vídeos, o sesiones en tiempo real en las respectivas páginas que se encuentran en la barra lateral, así como configuar los parámetros de la inferencia" \
        "El sistema generará un informe con los resultados de la detección, así" \
        " como una visualización práctica de dichas detecciones.")

# Páginas
home_page = st.Page(home, title="Página principal", icon=":material/home:", default=True)
tutorial_page = st.Page(tutorial, title="Tutorial", icon=":material/info:")
logout_page = st.Page(logout, title="Cerrar sesión", icon=":material/logout:")

dashboard = st.Page("reports/dashboard.py", title="Dashboard", icon=":material/dashboard:")
bugs = st.Page("reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
alerts = st.Page("reports/alerts.py", title="System alerts", icon=":material/notification_important:")

search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")

imagen = st.Page("metodo/imagen.py", title="Imagen", icon=":material/photo_camera:")
video = st.Page("metodo/video.py", title="Video", icon=":material/movie:")
directo= st.Page("metodo/directo.py", title="Directo", icon=":material/videocam:")

# Navegación condicional
if st.session_state.logged_in:
    
    st.markdown(
        """
        <style>
            div[data-testid="stSidebarHeader"] > img, div[data-testid="collapsedControl"] > img {
                height: auto;
                width: 18rem;
            }

            div[data-testid="stSidebarHeader"], div[data-testid="stSidebarHeader"] > *,
            div[data-testid="collapsedControl"], div[data-testid="collapsedControl"] > * {
                display: flex;
                align-items: center;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.logo("archivos/logo.png") #,size="large") # You can still use st.sidebar.logo, the CSS will override the default size
    pg = st.navigation(
        {
            "Inicio": [home_page,tutorial_page],
            "Métodos": [imagen, video, directo],
            #"Herramientas": [search, history],
            #"Cuenta": [logout_page],
            "Herramientas": [bugs, alerts],
        }
    )
else:
    pg = st.navigation([home_page])

pg.run()