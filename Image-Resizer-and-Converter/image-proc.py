from skimage import io
import os
from matplotlib import pyplot as plt
import numpy as np
from skimage.transform import rescale, resize, downscale_local_mean
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


def resizer():
    Length = int(Image_Length.get())
    Breadth = int(Image_Breadth.get())
    new_size = (Length, Breadth)
    file_format = str(Output_fformat.get())
    selected = Typechoice.get()

    if Length == "" or Breadth == "" or file_format == "":
        result.delete(0.0, END)
        result.insert(END, "\n Enter all inputs")

    img = io.imread(file_path, as_gray=selected)

    folder = out_path + "/"
    file_name = str(Output_fname.get())
    fname = folder + file_name + "." + file_format

    resized_img = resize(img, new_size)
    plt.axis('off')
    save = io.imsave(fname, resized_img)

    result.delete(0.0, END)
    result.insert(END, "\n Successful...")

    return


def format_converter():
    file_format = str(Output_fformat.get())
    selected = Typechoice.get()

    if file_format == "":
        result.delete(0.0, END)
        result.insert(END, "\n Enter paths and format")

    img = io.imread(file_path, as_gray=selected)

    folder = out_path + "/"
    file_name = str(Output_fname.get())
    fname = folder + file_name + "." + file_format

    plt.axis('off')
    save = io.imsave(fname, img)

    result.delete(0.0, END)
    result.insert(END, "\n Successful...")

    return


window = Tk()
window.geometry("400x500")  # the size of the window
window.title("Image-Proc | © Privima 2021")
window.iconbitmap(
    r"/Users/emmanuel_bamidele/Desktop/Bamspace/Data_Science_Tutorial/Python projects/Image_Processing/img-icon.ico")

Programname = Label(window, font=('Verdana', 25, 'bold'), text="IMAGE-PROC", fg="blue")

Programname.grid(row=1, column=6, padx=90, pady=30)

Choosepath = Label(window, font=('Verdana', 14, 'italic'), text="Choose image path and output folder", fg="red")
Choosepath.place(relx=.08, rely=.18)  # second method of placing

file_path = askopenfilename()

out_path = filedialog.askdirectory()

EnterDetails = Label(window, font=('Verdana', 14, 'italic'), text="Please enter the following inputs", fg="blue")
EnterDetails.place(relx=.08, rely=.24)

Length = Label(window, text="Image Length", font=('Copperplate Gothic', 15, 'bold'))
Length.place(relx=.02, rely=.32)

Image_Length = Entry(window)
Image_Length.place(relx=.37, rely=.32)

Breadth = Label(window, text="Image Breadth", font=('Copperplate Gothic', 15, 'bold'))
Breadth.place(relx=.02, rely=.40)

Image_Breadth = Entry(window)
Image_Breadth.place(relx=.37, rely=.40)

Output_name = Label(window, text="Output File Name", font=('Copperplate Gothic', 15, 'bold'))
Output_name.place(relx=.02, rely=.48)

Output_fname = Entry(window)
Output_fname.place(relx=.37, rely=.48)

Output_format = Label(window, text="Output Format", font=('Copperplate Gothic', 15, 'bold'))
Output_format.place(relx=.02, rely=.56)

Output_fformat = Entry(window)
Output_fformat.place(relx=.37, rely=.56)

Typechoice = BooleanVar()
Choice = Radiobutton(window, text="Color", variable=Typechoice, value=False)
Choice.place(relx=.23, rely=.64)

Choice = Radiobutton(window, text="Grayscale", variable=Typechoice, value=True)
Choice.place(relx=.45, rely=.64)

Resize = Button(window, text="Resize & Download", command=resizer)
Resize.place(relx=.05, rely=.74)

Convert = Button(window, text="Convert & Download", command=format_converter)
Convert.place(relx=.45, rely=.74)

result = Text(window, height=4, width=50, wrap=WORD)
result.place(relx=.03, rely=.82)

window.mainloop()
