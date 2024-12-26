import streamlit as st

# Título de la aplicación
st.title('Interfaz de Selección Múltiple')

# Crear una selección múltiple
opciones = st.multiselect(
    'Selecciona tus opciones favoritas:',
    ['Opción 1', 'Opción 2', 'Opción 3', 'Opción 4']
)

# Mostrar las opciones seleccionadas
if opciones:
    st.write('Has seleccionado:', ', '.join(opciones))
else:
    st.write('No has seleccionado ninguna opción.')
