from pyqrcode import *
def qrgen(s):
    qr = create(s)
    qr.png(s+".png",scale = 8)