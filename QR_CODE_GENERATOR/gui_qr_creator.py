from tkinter import *  
import qrcode
from PIL import Image, ImageTk
#creating the application main window.   
root = Tk() 

root.geometry("500x500+0+0")
root.title("QR Code Generator")
root.configure(background = 'cyan')


url_var = StringVar()
boxSize_var = IntVar()
border_var = IntVar()
 

def submit():
    url= url_var.get()
    boxSize=boxSize_var.get()
    border = border_var.get()

    if boxSize == 0:
        boxSize = 10
    if border == 0:
        border = 4

    img = qrcode.make(url, box_size=boxSize, border=border)
    img.save('qrcode.png')

    image_path = 'qrcode.png'
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image = photo)
    label.image = photo
    label.grid(row=4)



url_label = Label(root, text = 'URL', font=('calibre',11, 'bold'), bg='cyan')
url_entry = Entry(root,textvariable = url_var, font=('calibre',11,'normal'), width=50)
  
boxSize_label = Label(root, text = 'Box size', font = ('calibre',11,'bold'), bg='cyan')
boxSize_entry=Entry(root, textvariable = boxSize_var, font = ('calibre',11,'normal'), width=50)

border_label = Label(root, text = 'Border', font = ('calibre',11,'bold'), bg='cyan')
border_entry=Entry(root, textvariable = border_var, font = ('calibre',11,'normal'), width=50)
  
# creating a button using the widget
sub_btn=Button(root,text = 'Submit', command = submit)
  
# placing the label and entry in the required position using grid
url_label.grid(row=0,column=0)
url_entry.grid(row=0,column=1)
boxSize_label .grid(row=1,column=0)
boxSize_entry.grid(row=1,column=1)
border_label.grid(row=2,column=0)
border_entry.grid(row=2,column=1)
sub_btn.grid(row=3,column=1)

#Entering the event main loop  
root.mainloop()