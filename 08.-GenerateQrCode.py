import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save(
    "basic_qrcode.png",
    scale = 18,
    border= 9,
    light = "blue")