import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bjiezmunaora5oi898fu-mysql.services.clever-cloud.com,
            user='ueeb4z38vt9xtz3c',
            password='dSyQ74Vhjr57QxhpEi1e',
            database='bjiezmunaora5oi898fu',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
