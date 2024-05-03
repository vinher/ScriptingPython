import segno

texto = print(input("Ingrese URL: "))

qrcode = segno.make_qr(texto)
qrcode.save(
    "basic_qrcode.png",
    scale = 18,
    border= 9,
    light = "blue")