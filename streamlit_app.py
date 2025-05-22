import streamlit as st
from PIL import Image

# Inicializar sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Función para login
def login():
    st.title("Iniciar sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if username == "admin" and password == "4dm1n":
            st.session_state.logged_in = True
            st.success("Inicio de sesión exitoso")
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos")

# Función para logout
def logout():
    st.session_state.logged_in = False
    st.success("Sesión cerrada correctamente")
    st.stop()

# Función para página principal
def home():
    st.title("Demo | Monitoreo de uso de EPIs")
    st.video("archivos/DETECCION_EPIS_EJEMPLO_corto.mp4", 
             format="video/mp4",
             loop=True, autoplay=True, muted=True)

# Función para tutorial
def tutorial():
    st.title("Tutorial")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Acerca de la API")
        st.write("Desarrollado por Oesía Networks, este servicio permite " \
                 "al usuario detectar incumplimientos en el uso de EPIs mediante visión por computadora. " \
                 "El sistema está diseñado para detectar.")
    with col2:
        st.video("archivos/DETECCION_EPIS_EJEMPLO_corto.mp4", loop=True, autoplay=True, muted=True)

    st.subheader("¿Cómo funciona?")
    st.write("El usuario puede subir imágenes, vídeos, o iniciar sesiones en tiempo real. " \
             "El sistema generará un informe con los resultados de la detección y una visualización práctica.")

# Si no ha iniciado sesión, mostrar login
if not st.session_state.logged_in:
    login()
else:
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
    directo = st.Page("metodo/directo.py", title="Directo", icon=":material/videocam:")

    # Estilos y navegación
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

    st.logo("archivos/logo.png")

    pg = st.navigation(
        {
            "Inicio": [home_page, tutorial_page],
            "Métodos": [imagen, video, directo],
            "Herramientas": [bugs, alerts],
            "Cuenta": [logout_page]
        }
    )

    pg.run()