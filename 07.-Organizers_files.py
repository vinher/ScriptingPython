import os
import shutil

# Directorio de origen
directorio_origen = "/home/kevin/Downloads"

# Directorios de destino
carpetas_destino = {
    "imagenes": "home/kevin/Pictures",
    "videos": "home/kevin/Videos",
    "audio": "home/kevin/Music",
    "pdf": "home/kevin/Documents",
    "xslx": "home/kevin/Documents"
}

# Extensiones de archivos por tipo
extensiones = {
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "videos": [".mp4", ".avi", ".mov", ".mkv"],
    "audio": [".mp3", ".wav", ".ogg", ".flac"],
    "pdf": [".pdf"],
    "xslx": [".xlsx"]
}

# Función para mover archivos a las carpetas de destino
def organizar_archivos():
    for archivo in os.listdir(directorio_origen):
        for tipo, extensiones_tipo in extensiones.items():
            for extension in extensiones_tipo:
                if archivo.lower().endswith(extension):
                    origen = os.path.join(directorio_origen, archivo)
                    destino = os.path.join(carpetas_destino[tipo], archivo)
                    shutil.move(origen, destino)
                    print(f"Se movió '{archivo}' a '{carpetas_destino[tipo]}'")

# Crear directorios de destino si no existen
for carpeta in carpetas_destino.values():
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

# Organizar archivos
organizar_archivos()


react199->SAT

React1996# -> Infonavit