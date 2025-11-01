import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bckpifwzkoz49qo7der9-mysql.services.clever-cloud.com',
            user='uympslytyir9cne4',
            password='a8CYQR2FO5x4tpYHwrYZ',
            database='bckpifwzkoz49qo7der9',
            port=3306 )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
