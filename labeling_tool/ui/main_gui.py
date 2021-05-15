import tkinter as tk
from ui.component.header import Header
from ui.component.image_canvas import ImageCanvas
import glob

class MainGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1920x1080")

        # ===== define params ====
        self.current_img_index = -1
        self.num_img_files = 0
        self.png_imgs_path = []

        # ===== pack component =====
        self.header = Header(self.root,self.open_folder)
        self.header.pack(side=tk.TOP,fill=tk.X)
        self.image_canvas = ImageCanvas(self.root,bg="red")
        self.image_canvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

        # ===== key event ======
        self.root.bind("<Key>",self.__key_pressed)
        self.root.bind("<Control-Key>",self.__key_pressed_with_control)
        self.root.mainloop()

    def open_folder(self,folder_path):
        files = glob.glob(f"{folder_path}/*")
        png_files = [file for file in files if file.endswith(".png")]
        self.png_imgs_path = png_files
        self.current_img_index = -1
        self.num_img_files = len(self.png_imgs_path)
        self.__next_img()

    
    def __key_pressed(self,event):
        key = event.keysym
        if key == "s":
            self.__skip_img()
        elif key == "space":
            self.__next_img()

    def __key_pressed_with_control(self,event):
        pass

    def __next_img(self):
        self.current_img_index+=1
        print(self.num_img_files)
        if self.current_img_index < self.num_img_files:
            print("next")
            self.header.update_count_text(self.current_img_index,self.num_img_files)
            self.image_canvas.open_image(self.png_imgs_path[self.current_img_index])

    def __skip_img(self):
        self.__next_img()

    
