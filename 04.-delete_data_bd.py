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
#faker = Faker()

# Generar e insertar mil registros en la tabla productos
#for i in range(80):
 #   nombre      = faker.name()
 #  direccion   = faker.address()
 #  telefono    = faker.phone_number()
    
    
    # Insertar el registro en la tabla productos
consulta = "DELETE FROM producto WHERE id > 900 "
cursor.execute(consulta)

# Confirmar la inserción de los registros
conexion.commit()

# Cerrar la conexión a la base de datos
cursor.close()
conexion.close()

print("Se han Borrado 80 registros de productos.")
