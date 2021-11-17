#reconhecendo qrcode a partir de um arquivo de imagem
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('Lamotte.png')
result = decode(img)
for i in result:
    print(i.data.decode("utf-8"))
