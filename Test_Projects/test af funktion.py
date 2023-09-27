import tkinter
from tkinter import *
from subprocess import call   
from PIL import ImageTk, Image

XY = "720x720"
XL = 720
YW = 720   

root = Tk()
root.wm_title("Main Interface")
root.geometry(XY)

class Window(Frame):
       
    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)
        
        QRMenu = Menu(menu)      
        menu.add_cascade(label="QR",menu=QRMenu)
        
        QRCodeMenu = Menu(menu)
        QRCodeMenu.add_command(label="Front Page QR Code",command=self.QRCodeFront)
        QRCodeMenu.add_command(label="QR yt",command=self.QRCodeYT)
        QRMenu.add_cascade(label="QR Codes", menu=QRCodeMenu)
                     
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        #create a image variable and finde where the image you want to show 
        image1 = Image.open("lion.jpg")
        #here we set test to be the image on the window    
        test = ImageTk.PhotoImage(image1)

        #in order to get the image on the window we make a lable with the image
        label1 = tkinter.Label(image=test)
        label1.image = test

        # Position lable with the image
        label1.place(x=XL-505, y=YW-600)
        
        #how we make buttons and give them functions
        # PrintHI = Button(self, text= "Print Hi",command=self.PrintHI,width= 20)            
        # Title = Label(self,text="Interface for Program",font=('Helvetica bold', 25),fg="green")  
        
        Title = Label(self,text="Interface for Program",font=('Helvetica bold', 25),fg="green")
        QRButton = Button(self, text="QR Reader", command=self.openQR,fg= "white",bg="black", width= 20)
        PrintHI = Button(self, text="Print Hi", command=self.PrintHI,fg= "white",bg="black", width= 20)
        
        #how we set position of stuff
        #QRButton.place(x=XL-440,y=((YW)-200)) or Title.pack(pady=20)
        
        Title.pack(pady=20) 
        QRButton.place(x=XL-440,y=((YW)-200))
        PrintHI.place(x=XL-440,y=((YW)-250))        
    
    #functions for the buttons and menu commands    
    def openQR(self):
        call(["python","QR\QR_reader.py"])
    
    def QRCodeFront(self):
        call(["python","QR\FrontImage.py"])
    def QRCodeYT(self):
        call(["python","QR\QR_yt.py"])
    
    def exitProgram(self):
        exit()
    
    def PrintHI(self):
        print("Hi")  

#keeps the window functional and loops the window until you close it       
app = Window(root)
root.mainloop()