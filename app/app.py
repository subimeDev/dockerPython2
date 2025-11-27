import os
import time
from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    """Se conecta a la BBDD con reintentos."""
    conn = None
    # Bucle de reintentos
    for i in range(10):
        try:
            conn = mysql.connector.connect(
                host=os.environ.get('DB_HOST'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
                database=os.environ.get('DB_NAME')
            )
            if conn.is_connected():
                print('Conectado a la base de datos MySQL')
                return conn
        except Error as e:
            print(f"Error conectando a MySQL (intento {i+1}): {e}")
            time.sleep(3) # Espera 3 segundos
    
    return None

@app.route('/')
def index():
    """Ruta principal que muestra los usuarios."""
    conn = get_db_connection()
    if conn is None:
        return "<h1>Error: No se pudo conectar a la base de datos.</h1>"
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        
        html = "<h1>Usuarios en la Base de Datos:</h1><ul>"
        for usuario in usuarios:
            html += f"<li>ID: {usuario[0]}, Nombre: {usuario[1]}</li>"
        html += "</ul>"
        return html

    except Error as e:
        return f"<h1>Error al ejecutar la consulta: {e}</h1>"
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    # 'host=0.0.0.0' es crucial para que el contenedor sea accesible
    app.run(host='0.0.0.0', port=8000, debug=True)