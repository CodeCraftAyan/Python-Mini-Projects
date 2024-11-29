import qrcode
import qrcode.constants

data = input("\nEnter your data to generate the QR code =  ")

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 2
)

qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(back_color='#003049', fill_color='#80ed99')
img.save("QRcode.png")

print("QR code generated successfully !")