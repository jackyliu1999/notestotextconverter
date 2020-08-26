import pytesseract
pytesseract.pytesseract.tesseract_cmd = "./pytess/tesseract.exe"
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import simpledialog

filePath = ""

def browseFile():
    global filePath
    filePath = askopenfilename()
    img = Image.open(filePath)
    img2 = img.resize((360, 640), Image.ANTIALIAS)
    gui.photo = ImageTk.PhotoImage(img2)
    vlabel.configure(image=gui.photo)
    label1.configure(text="Filepath = "+filePath)
    newFile = simpledialog.askstring("input string","Input file name to write to:")
    newFile = newFile+".txt"
    toText(filePath, newFile)

def toText(filePath, fileName):
    im = Image.open(filePath)
    text = pytesseract.image_to_string(im, lang="eng")
    file1 = open(fileName, "w")
    file1.write(text)
    file1.close()

gui = Tk()
gui.geometry("800x800")

b = Button(gui, text="Browse File", command=browseFile)
b.pack(side=TOP)

label1 = tk.Label(gui)
label1.pack()

photo = "testCases/Base.png"
gui.photo = ImageTk.PhotoImage(Image.open(photo))
vlabel=tk.Label(gui,image=gui.photo)
vlabel.pack()

gui.mainloop()
print(filePath)