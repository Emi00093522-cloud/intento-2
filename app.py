# app.py
import streamlit as st
from modulos.ventas import mostrar_ventas  # Importamos la función mostrar_ventas del módulo ventas
from modulos.login import login

# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
    # Si la sesión está iniciada, mostrar el contenido de ventas
    mostrar_ventas()
else:
    # Si no hay sesión iniciada, mostrar el login
    login()
