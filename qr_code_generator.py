import qrcode

# qr = qrcode.make('prasanth')
# qr.save('qr.png')

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=2
    )

data = 'https://www.instagram.com/prasanth_vinnakota/'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='blue', back_color='white')
img.save('C:\\Users\\Prasanth Vinnakota\\Desktop\\instagram_profile.png')
