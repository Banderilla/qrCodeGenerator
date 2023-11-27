#This little program generates qr codes.

import qrcode
from tkinter import *
from PIL import ImageTk, Image

def generate_qr_code():
    data = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save('qr_code.png')
    show_qr_code()

def show_qr_code():
    img = Image.open('qr_code.png')
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

root = Tk()
root.title("Qr Code Gen")

entry = Entry(root)
entry.pack()

button = Button(root, text="Generate QR Code", command=generate_qr_code)
button.pack()

panel = Label(root)
panel.pack()

root.mainloop()
