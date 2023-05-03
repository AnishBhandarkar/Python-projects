"""The qrcode library in Python is used to generate QR (Quick Response) codes. 
These are 2D barcodes that can be scanned using a smartphone or a QR code reader to quickly access
information encoded within the code."""

# import package
import qrcode

print('Enter url to be encoded in QR code: ')
url = input()

# genaerates qr code from data
# url is mandatory and remaining arguments are optional
img = qrcode.make(url, box_size=5, border=5)

# save qr code as image in jpg/jpeg/png/gif
img.save('qrcode.png')
