import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


qr = pyqrcode.create("HELLO EVERYONE")
qr.png("Hello.png", scale=8)

d = decode(Image.open("Hello.png"))
print(d[0].data.decode("ascii"))