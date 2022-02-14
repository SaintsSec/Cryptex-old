from menu import qrLogo
import qrcode

#Print the logo
print(qrLogo)
#Ask user for link input.
linkie = input("What link would you like to QR Encode: ")

#Generate the QRCode:
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(linkie)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('qrout001.png')
input("\n\nYour image has been saved press enter to return to main menu")
exec(open("cryptex.py").read())