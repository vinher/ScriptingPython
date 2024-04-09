from PIL import Image
import os

def convert_to_webp(image_path):
    try:
        # Abre la imagen
        img = Image.open(image_path)
        
        # Obtiene el nombre y la extensión del archivo
        filename, extension = os.path.splitext(image_path)
        
        # Convierte la imagen a WebP
        webp_path = filename + ".webp"
        img.save(webp_path, "WEBP")
        
        print(f"Imagen {image_path} convertida a WebP: {webp_path}")

    except Exception as e:
        print(f"Error al convertir la imagen {image_path}: {str(e)}")


def delete_image(image_path):
    try:
        os.remove(image_path)
        print(f"La imagen '{image_path}' ha sido eliminada correctamente.")
    except OSError as e:
        print(f"No se pudo eliminar la imagen '{image_path}': {e}")



def main():
    # Directorio que contiene las imágenes
    directory = "/home/kevin/Pictures/portfolio"
    # Itera sobre los archivos en el directorio
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(directory, filename)
            convert_to_webp(image_path)
            delete_image(image_path)

if __name__ == "__main__":
    main()
