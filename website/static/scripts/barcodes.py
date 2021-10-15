import os
import sys

# this_dir = os.path.dirname(os.path.abspath(__file__))
# activate_this = this_dir + '/obsidian/bin/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))

# # anhadir dir de este fichero a path
# sys.path.insert(0, this_dir)

from barcode import EAN13
from pyzbar import pyzbar
import cv2
import qrcode
from barcode.writer import ImageWriter

# Basic barcode maker allows for the creation of barcode with 
# export to png or svg
def make_barcode(number, name='newCode', png=False):
    # If eplicitly stated that must be PNG format
    if png:
        code = EAN13(number, writer=ImageWriter())
    # Else code is automatically created in SVG format
    else:
        code = EAN13(number)
    
    code.save(name)

# Basic QR code maker allows for the creation of QR codes exported
# directly to png
def make_qrcode(website, name='qrcode001.png', version=1, box_size=10, border=5):
    # QR Codre creator based on passed parameters
    qr = qrcode.QRCode(
        version=version,
        box_size=box_size,
        border=border)
    qr.add_data(website)
    
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode001.png')


def read_barcode():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        suc, frame = cap.read()
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            print(barcode.type)
            print(barcode.data.decode('utf-8'))

        cv2.imshow('TestScan', frame)
        cv2.waitKey(1)

        # x, y, w, h = barcode.rect
        
        # #1
        # barcode_info = barcode.data.decode('utf-8')
        # cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        #
        # #2
        # font = cv2.FONT_HERSHEY_DUPLEX
        # cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        
        #3
        # with open("barcode_result.txt", mode ='w') as file:
        #     file.write("Recognized Barcode:" + barcode_info)
            
    return frame

make_barcode('1234567891023',png=True)
make_qrcode('https://gihub.com')
read_barcode()
