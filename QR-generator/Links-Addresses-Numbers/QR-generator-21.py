import os
import pyqrcode
from pyqrcode import *
from tkinter import *
from tkinter import filedialog


def qr_generator():
    content = str(input_qr.get())
    fname = str(filename.get())

    url = pyqrcode.create(str(content))
    fname = out_path + "/" + fname
    url.svg(fname + ".svg", scale=8)
    url.eps(fname + ".eps", scale=8)

    result.delete(0.0, END)
    result.insert(END, "Successful...")


window = Tk()
window.geometry("250x300")  # the size of the window
window.title("© Bamidele")
window.iconbitmap(
    r"C:\Users\bamid\Desktop\BamSpace\Data_Science_Tutorial\Python Codes\GUIs\QR-generator\qr-icon.ico")

Programname = Label(window, font=('Verdana', 20, 'bold'), text="QR-GEN-PY", fg="blue")
Programname.place(relx=0.15, rely=0.02)

input_label = Label(window, text="QR Content", font=('Copperplate Gothic', 12, 'bold'))
input_label.place(relx=.28, rely=.22)

input_qr = Entry(window)
input_qr.place(relx=.2, rely=.32)

file_label = Label(window, text="File Name", font=('Copperplate Gothic', 12, 'bold'))
file_label.place(relx=.3, rely=.45)

filename = Entry(window)
filename.place(relx=.2, rely=.55)

Generate = Button(window, text="Generate", command=qr_generator)
Generate.place(relx=.35, rely=.70)

result = Text(window, height=1, width=20, wrap=WORD, fg="red")
result.insert(END, "Enter Inputs...")
result.place(relx=.2, rely=.85)

out_path = filedialog.askdirectory()

window.mainloop()