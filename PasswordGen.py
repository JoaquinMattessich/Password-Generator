import random
import string
import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Generador de Contraseñas Seguras",
    page_icon="🔒",
    layout="centered"
)

st.title("🔒 Generador de Contraseñas Seguras")
st.write("Genera contraseñas aleatorias y personalizadas para proteger tus cuentas.")

st.markdown("---")

# Parámetros en la interfaz de usuario
col1, col2 = st.columns([2, 1])

with col1:
    length = st.slider("Longitud de la contraseña:", min_value=6, max_value=64, value=16)

with col2:
    use_uppercase = st.checkbox("Mayúsculas (A-Z)", value=True)
    use_lowercase = st.checkbox("Minúsculas (a-z)", value=True)
    use_digits = st.checkbox("Números (0-9)", value=True)
    use_symbols = st.checkbox("Símbolos (!@#$%...)", value=True)

# Función para generar la contraseña
def generar_password(longitud, mayus, minus, nums, simbs):
    caracteres = ""
    password = []

    # Garantizar al menos un carácter de cada tipo seleccionado
    if mayus:
        caracteres += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if minus:
        caracteres += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if nums:
        caracteres += string.digits
        password.append(random.choice(string.digits))
    if simbs:
        caracteres += string.punctuation
        password.append(random.choice(string.punctuation))

    if not caracteres:
        return None

    # Rellenar el resto de la longitud deseada
    for _ in range(longitud - len(password)):
        password.append(random.choice(caracteres))

    # Mezclar caracteres para evitar patrones predecibles
    random.shuffle(password)
    return "".join(password)

# Botón para generar
if st.button("🔑 Generar Contraseña", type="primary", use_container_width=True):
    nueva_password = generar_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    
    if nueva_password is None:
        st.error("⚠️ Debes seleccionar al menos un tipo de carácter.")
    else:
        st.success("¡Contraseña generada con éxito!")
        # Muestra la contraseña en un bloque de código para fácil copiado
        st.code(nueva_password, language="")

        # Evaluación básica de seguridad según la longitud
        if length < 10:
            st.warning("Nivel de seguridad: **Bajo**. Se recomiendan al menos 12 caracteres.")
        elif length < 14:
            st.info("Nivel de seguridad: **Medio**.")
        else:
            st.success("Nivel de seguridad: **Alto**.")
