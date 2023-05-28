# Encoding Data into Quick Response Code (QR Code)
import qrcode
import constants
data = input("enter data")
qr_code = qrcode.QRCode(version= None,error_correction= constants.ERROR_CORRECT_M, box_size  = 10, border= 4)
qr_code.add_data(data)
qr_code.make(fit =True)
qr_code = qr_code.make_image(fill_color = "green", back_color ="orange" )

qr_code.save("my_QRCODE.png")

data = "img.png"
qr_code = qrcode.QRCode(version= None,error_correction= constants.ERROR_CORRECT_M, box_size  = 10, border= 4)
qr_code.add_data(data)
qr_code.make(fit =True)
qr_code = qr_code.make_image(fill_color = "green", back_color ="blue" )
qr_code.save("QRCODE_image.png")



qr_code.save("from_qrimage.png")

