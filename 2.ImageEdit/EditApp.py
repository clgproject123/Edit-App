from tkinter import *
from PIL import Image,ImageTk,ImageEnhance
from tkinter import filedialog
import tkinter as tk
import tkinter.messagebox
import numpy as np

number = 0
rotateDegree = 0
numpyImage = []
contrastLevel = 1

class UniversePack():
    def ShowImage():
        global filename,numpyImage
        filename = filedialog.askopenfilename(title="Select an Image", filetype=(('image    files','*.jpg'),('all files','*.*')))
        img = Image.open(filename)
        numpyImage = np.array(img)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img)
        lbl.image = img
        
    def Info():
        global numpyImage
        converNumpyToPIL = Image.fromarray(numpyImage)
        tkinter.messagebox.showinfo('size',('size:',str(converNumpyToPIL.size),'\nforamt:',converNumpyToPIL.format,'\nmode:',converNumpyToPIL.mode))
    
    def IncreaseImageSize():
        global number,numpyImage
        number += 10
        converNumpyToPIL = Image.fromarray(numpyImage)
        resizeImg = converNumpyToPIL.resize((list(converNumpyToPIL.size)[0]+ number, list(converNumpyToPIL.size)[1]+ number))
        numpyImage = np.array(resizeImg)
        img = ImageTk.PhotoImage(resizeImg)
        lbl.configure(image=img)
        lbl.image = img

    def DecreaseImageSize():
        global number,numpyImage
        number -= 10
        converNumpyToPIL = Image.fromarray(numpyImage)
        resizeImg = converNumpyToPIL.resize((list(converNumpyToPIL.size)[0]+ number, list(converNumpyToPIL.size)[1]+ number))
        numpyImage = np.array(resizeImg)
        img = ImageTk.PhotoImage(resizeImg)
        lbl.configure(image=img)
        lbl.image = img

    def RotateImage():
        global rotateDegree,numpyImage
        rotateDegree += 5
        converNumpyToPIL = Image.fromarray(numpyImage)
        rotateImage = converNumpyToPIL.rotate(rotateDegree, expand=True)
        numpyImage = np.array(rotateImage)
        img = ImageTk.PhotoImage(rotateImage)
        lbl.configure(image=img)
        lbl.image = img

    def LeftToRight():
        global numpyImage
        converNumpyToPIL = Image.fromarray(numpyImage)
        rightToleft = converNumpyToPIL.transpose(Image.FLIP_LEFT_RIGHT)
        numpyImage = np.array(rightToleft)
        img = ImageTk.PhotoImage(rightToleft)
        lbl.configure(image=img)
        lbl.image = img

    def TopToBotton():
        global numpyImage
        converNumpyToPIL = Image.fromarray(numpyImage)
        topTobottom = converNumpyToPIL.transpose(Image.FLIP_TOP_BOTTOM)
        numpyImage = np.array(topTobottom)
        img = ImageTk.PhotoImage(topTobottom)
        lbl.configure(image=img)
        lbl.image = img

    def ContrastIncrease():
        global numpyImage,contrastLevel
        contrastLevel += 0.1
        converNumpyToPIL = Image.fromarray(numpyImage)
        contrastChanger = ImageEnhance.Contrast(converNumpyToPIL)
        contrastHighLevel = contrastChanger.enhance(contrastLevel)
        numpyImage = np.array(contrastHighLevel)
        img = ImageTk.PhotoImage(contrastHighLevel)
        lbl.configure(image=img)
        lbl.image = img

    def ContrastDecrease():
        global numpyImage,contrastLevel
        contrastLevel -= 0.1
        converNumpyToPIL = Image.fromarray(numpyImage)
        contrastChanger = ImageEnhance.Contrast(converNumpyToPIL)
        contrastHighLevel = contrastChanger.enhance(contrastLevel)
        numpyImage = np.array(contrastHighLevel)
        img = ImageTk.PhotoImage(contrastHighLevel)
        lbl.configure(image=img)
        lbl.image = img

    def save():
        global numpyImage
        converNumpyToPIL = Image.fromarray(numpyImage)
        result = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(
            ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif')))
        if result:
            converNumpyToPIL.save(result)

root = Tk()
root.geometry("940x450")
root.title('Edit App')

lbl = Label(root)
lbl.pack()

fotterFrame = Frame(root, bg='yellow', width=840, height=100, cursor='dot')
fotterFrame.pack(side=BOTTOM)

selectImageBtn = Button(fotterFrame,bg='blue' ,text="Select image",fg="white", command=UniversePack.ShowImage)
selectImageBtn.pack(side=tk.LEFT,padx=5,pady=5)

infoBtn = Button(fotterFrame, bg='blue' ,text="Info",fg="white", command=UniversePack.Info)
infoBtn.pack(side=tk.LEFT,padx=5,pady=5)

reSizeImageBtnIncrease = Button(fotterFrame, bg='blue' ,text="Increase image",fg="white",command=UniversePack.IncreaseImageSize)
reSizeImageBtnIncrease.pack(side=tk.LEFT,padx=5,pady=5)

reSizeImageBtnDecrease = Button(fotterFrame, bg='blue' ,text="Decrease image",fg="white",command=UniversePack.DecreaseImageSize)
reSizeImageBtnDecrease.pack(side=tk.LEFT,padx=5,pady=5)

rotateImageBtn = Button(fotterFrame, bg='blue' ,text="Rotate image",fg="white", command=UniversePack.RotateImage)
rotateImageBtn.pack(side=tk.LEFT,padx=5,pady=5)

transposeImageTTB = Button(fotterFrame, bg='blue', text='Top to Bottom', fg="white", command=UniversePack.TopToBotton)
transposeImageTTB.pack(side=tk.LEFT,padx=5,pady=5)

transposeImageLTR = Button(fotterFrame, bg='blue', text='left to right', fg="white", command=UniversePack.LeftToRight)
transposeImageLTR.pack(side=tk.LEFT,padx=5,pady=5)

contrastIncrease = Button(fotterFrame, bg='blue', text='contrast increase', fg="white",command=UniversePack.ContrastIncrease)
contrastIncrease.pack(side=tk.LEFT,padx=5,pady=5)

contrastDecrease = Button(fotterFrame, bg='blue', text='contrast decrease', fg="white", command=UniversePack.ContrastDecrease)
contrastDecrease.pack(side=tk.LEFT,padx=5,pady=5)

saveBtn = Button(fotterFrame, bg='blue', text='save', fg="white", command=UniversePack.save)
saveBtn.pack(side=tk.LEFT,padx=5,pady=5)

exitBtn = Button(fotterFrame, bg='red', text='Exit',fg='white',command=lambda:exit())
exitBtn.pack(side=tk.LEFT,padx=5,pady=5)

mainloop()


