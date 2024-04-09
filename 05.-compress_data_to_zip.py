import os
import zipfile

def zip_directory(directory, zip_filename):
    try:
        # Abre un archivo ZIP para escribir
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Itera sobre los archivos en el directorio y los añade al archivo ZIP
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, directory)
                    zipf.write(file_path, arcname=arcname)

        print(f"La carpeta '{directory}' ha sido comprimida en '{zip_filename}'")
    except Exception as e:
        print(f"Error al comprimir la carpeta: {str(e)}")

def main():
    # Directorio que deseas comprimir
    directory = "/home/kevin/Pictures/portfolio"

    # Nombre del archivo ZIP resultante
    zip_filename = "/home/kevin/Pictures/archivo_comprimido.zip"

    # Comprimir la carpeta en un archivo ZIP
    zip_directory(directory, zip_filename)

if __name__ == "__main__":
    main()
