import qrcode
import datetime
x = datetime.datetime.now()

def generate_qrcode(text):
    
    qr = qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # file is saved as DD-MM-YYYY-HH-MM-SS.png
    img.save(f"{x.strftime('%d-%b-%Y-%H-%M-%S')}.png") 

url = input("Enter the text you want to convert to QR code: ")
generate_qrcode(url)