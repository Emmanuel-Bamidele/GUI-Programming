import wifi_qrcode_generator as qr
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt


def qr_generator():
    wifi_name = str(wifi.get())
    wifi_ps = str(wifi_p.get())
    fname = str(filename.get())

    qr_out = qr.wifi_qrcode(wifi_name, False, 'WPA', wifi_ps)
    fname = out_path + "/" + fname
    qr_out.save(fname + ".png")

    result.delete(0.0, END)
    result.insert(END, "Successful...")


window = Tk()
window.geometry("250x300")  # the size of the window
window.title("© Bamidele-21")
window.iconbitmap(
    r"C:\Users\bamid\Desktop\BamSpace\Data_Science_Tutorial\Python Codes\GUIs\QR-generator\qr-icon.ico")

Programname = Label(window, font=('Verdana', 20, 'bold'), text="QR-WIFI", fg="blue")
Programname.place(relx=0.15, rely=0.02)

wifi_label = Label(window, text="Wifi Name", font=('Copperplate Gothic', 12, 'bold'))
wifi_label.place(relx=.28, rely=.15)

wifi = Entry(window)
wifi.place(relx=.2, rely=.25)

wifi_p_label = Label(window, text="Password", font=('Copperplate Gothic', 12, 'bold'))
wifi_p_label.place(relx=.3, rely=.35)

wifi_p = Entry(window, show="*")
wifi_p.place(relx=.2, rely=.45)

file_label = Label(window, text="File Name", font=('Copperplate Gothic', 12, 'bold'))
file_label.place(relx=.3, rely=.55)

filename = Entry(window)
filename.place(relx=.2, rely=.65)

Generate = Button(window, text="Generate", command=qr_generator)
Generate.place(relx=.32, rely=.75)

result = Text(window, height=1, width=20, wrap=WORD, fg="red")
result.insert(END, "Enter Inputs...")
result.place(relx=.2, rely=.87)

out_path = filedialog.askdirectory()

window.mainloop()