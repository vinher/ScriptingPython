import mysql.connector
from faker import Faker
import random

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="developer",
    password="",
    database="almacen_db"
)
cursor = conexion.cursor()

# Crear un objeto Faker para generar datos ficticios
faker = Faker()

# Generar e insertar mil registros en la tabla productos
for _ in range(50):
    nombre  = faker.word()
    precio  = round(random.uniform(1.0, 100.0), 2)
    stock   = random.randint(1, 100)
    imagen  = "http://172.16.102.238:5000/static/images/warehouse_icon.png"
    
    # Insertar el registro en la tabla productos
    consulta = "INSERT INTO producto (nombre, precio, stock, image) VALUES (%s, %s, %s, %s)"
    valores = (nombre, precio, stock, imagen)
    cursor.execute(consulta, valores)

# Confirmar la inserción de los registros
conexion.commit()

# Cerrar la conexión a la base de datos
cursor.close()
conexion.close()

print("Se han insertado mil registros en la tabla productos.")
