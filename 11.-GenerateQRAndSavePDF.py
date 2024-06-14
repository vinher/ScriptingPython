import qrcode
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def generate_qr_codes_from_file(file_path, output_pdf):
    # Leer los números del archivo
    with open(file_path, 'r') as file:
        numbers = file.readlines()

    # Crear el canvas para el PDF
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    # Configurar la cuadrícula para los códigos QR
    qr_size = 5 * cm
    margin = 2 * cm
    x_positions = [margin, width/2 + margin/2]
    y_positions = [height - margin - qr_size * (i + 1) for i in range(4)]

    index = 0
    for number in numbers:
        number = number.strip()  # Elimina los espacios en blanco
        if number:  # Asegúrate de que no esté vacío
            img = qrcode.make(number)
            img_path = f"temp_{number}.png"
            img.save(img_path)

            # Calcular la posición en la cuadrícula
            x = x_positions[index % 2]
            y = y_positions[(index // 2) % 4]
            
            c.drawImage(img_path, x, y, qr_size, qr_size)
            os.remove(img_path)  # Eliminar la imagen temporal

            index += 1

            # Cada 8 códigos QR, crear una nueva página
            if index % 8 == 0:
                c.showPage()

    c.save()
    print(f"PDF generado: {output_pdf}")

if __name__ == "__main__":
    import argparse

    # Crear el parser de argumentos
    parser = argparse.ArgumentParser(description="Generar un PDF con códigos QR desde un archivo de texto con números.")
    parser.add_argument("file_path", help="Ruta al archivo de texto con los números.")
    parser.add_argument("output_pdf", help="Ruta donde se guardará el PDF generado.")

    # Parsear los argumentos
    args = parser.parse_args()

    # Llamar a la función principal
    generate_qr_codes_from_file(args.file_path, args.output_pdf)
