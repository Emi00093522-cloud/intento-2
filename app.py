# app.py
import streamlit as st
from modulos.ventas import mostrar_venta  # Importamos la función mostrar_ventas del módulo ventas
from modulos.login import login

# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
    # Mostrar el menú lateral
opciones = ["Ventas", "Otra opción"]  # Agrega más opciones si las necesitas
seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

# Según la opción seleccionada, mostramos el contenido correspondiente
if seleccion == "Ventas":
    mostrar_venta()  # Corregido: mostrar_venta() → mostrar_ventas()
elif seleccion == "Otra opción":
    st.write("Has seleccionado otra opción.")  # Aquí podrías agregar el contenido de otras opciones
   
else:
    # Si no hay sesión iniciada, mostrar el login
    login()
