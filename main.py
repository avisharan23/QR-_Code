import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr=pyqrcode.create('QRCODE')
qr.png('mycode.png',scale=8)