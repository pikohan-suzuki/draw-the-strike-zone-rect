import tkinter as tk
from PIL import Image, ImageTk

class ImageCanvas(tk.Canvas):

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)

    def open_image(self,img_path):
        global pil_image,photo_image
        try:
            self.delete("image")
            pil_image = Image.open(img_path)
            photo_image = ImageTk.PhotoImage(image=pil_image)
            self.create_image(self.winfo_width()/2,self.winfo_height()/2,image=photo_image,tag="image")
        except Exception as e:
            self.create_text(self.winfo_width()/2,self.winfo_height()/2,text=f"could not open image file\n{img_path}",tag="image") 
