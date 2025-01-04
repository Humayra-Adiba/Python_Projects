import tkinter as tk
from tkinter import font
import pyqrcode
from PIL import Image, ImageTk

qrcodeimg = None

def generateQrCode():
    generatedqrcode = pyqrcode.create(inputText.get())
    generatedqrcode.png("qr_code.png", scale =5 )
    global qrcodeimg
    # qrcodeimg = Image.open("qr_code.png")
    qrcodeimg = ImageTk.PhotoImage(Image.open("qr_code.png"))
    qrcoderesultLabel.config(image=qrcodeimg)

def clearQrCode():
    inputText.delete(0, tk.END)
    qrcoderesultLabel.config(image="")


root = tk.Tk()
root.title("QR code generator")

headerLabel = tk.Label( root, text="QR code generator", padx=8, pady=6,font=font.Font(size=22))
headerLabel.grid(row=0, column=0, columnspan=2)

inputText = tk.Entry(root, font=font.Font(size=22),)
inputText.grid(row=1, column=0, padx=8, pady=6, sticky="ew", columnspan=2)

generateButton = tk.Button(root, text="Generate", background="gray", foreground="white", font=font.Font(size=18), command=generateQrCode)
generateButton.grid(row=2, column=0, sticky="ew")

clearButton = tk.Button(root, text="Clear", background="gray", foreground="white", font=font.Font(size=18), command=clearQrCode)
clearButton.grid(row=2, column=1, sticky="ew")

qrcoderesultLabel = tk.Label(root, text="Please press generate button to generate QR code", image=None, padx=14, pady=14,font=font.Font(size=16) )
qrcoderesultLabel.grid(row=3, column=0, columnspan=2)


root.mainloop()
