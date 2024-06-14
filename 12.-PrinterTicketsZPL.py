import socket

def imprimir_etiqueta_zpl(zpl_code, printer_ip, printer_port=9100):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((printer_ip, printer_port))
        s.sendall(zpl_code.encode('utf-8'))



def generar_zpl(tela, clave, medida, composicion, kilos, ancho, variante, lote, elemento, hechoen):
    zpl = "^XA^CI28^MUd,300,300"

    zpl += "^A0N,30,35^FO10,30^FD" + tela + "^FS"
    zpl += "^CF30,30^FO12,65^FD Clave: ^FS"
    zpl += "^A0N,30,30^FO130,65^FD " + clave + " ^FS"
    zpl += "^A0N,30,30^FO650,100^FD " + medida + " MTS ^FS"
    zpl += "^CF30,30^FO12,110^FD Composición: ^FS"
    zpl += "^A0N,30,30^FO20,155^FD " + composicion + " ^FS"
    zpl += "^A0N,30,30^FO650,150^FD " + kilos + " KG ^FS"
    zpl += "^CF30,30^FO10,200^FD Ancho: ^FS"
    zpl += "^A0N,30,30^FO130,200^FD " + ancho + " mts ^FS"
    zpl += "^CF30,30^FO640,200^FD Dispo: ^FS"
    zpl += "^A0N,30,30^FO650,230^FD - ^FS"
    zpl += "^CF30,30^FO10,250^FD Diseño/Color: ^FS"
    zpl += "^A0N,30,30^FO20,280^FD " + variante + " ^FS"
    zpl += "^CF30,30^FO10,320^FD Lote: ^FS"
    zpl += "^A0N,30,30^FO120,320^FD " + lote + " ^FS"
    zpl += "^FO130,365^BY2^B3N,N,60,Y,N^FD" + elemento + "^FS"
    zpl += "^CF30,20^FO30,470^FD Lavar a máquina/mano con agua fría, secar en secadora a baja ^FS"
    zpl += "^CF30,20^FO30,490^FD temperatura, no usar blanqueador, planchado temperatura baja ^FS"
    zpl += "^CF30,20^FO20,510^FD " + hechoen + " Comercializadora Círculo Textil ^FS"
    zpl += "^CF30,20^FO50,530^FD S.A. de C.V. , ANICETO ORTEGA 817 C, DEL VALLE, BENITO ^FS"
    zpl += "^CF30,20^FO280,550^FD JUÁREZ, CDMX.03100 ^FS"
    zpl += "^CF30,20^FO310,570^FD CCT2206022DA " + ancho + " mts ^FS"
    zpl += "^XZ"

    return zpl

zpl_code = generar_zpl("Prueba", "12345", "10", "100% TEST", "1.5", "1.5", "Rojo", "67890", "0123456789", "Hecho en México")
print(zpl_code)

printer_ip = "192.168.14.39"
imprimir_etiqueta_zpl(zpl_code, printer_ip)