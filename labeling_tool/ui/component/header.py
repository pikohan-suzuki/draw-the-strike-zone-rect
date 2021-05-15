import tkinter as tk
import tkinter.filedialog
import os

class Header(tk.Frame):
    def __init__(self, master=None, open_folder_func=None,cnf=None, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        self.open_folder_func = open_folder_func
        open_folder_button = tk.Button(self,text="Open Folder",command=self.__on_open_folder_button_clicked)
        open_folder_button.pack(side=tk.LEFT)
        self.file_count_label= tk.Label(self,text="0 / 0")
        self.file_count_label.pack(side=tk.LEFT)

    def __on_open_folder_button_clicked(self):
        iDir = os.path.abspath(os.path.dirname(__file__))
        folder_path = tk.filedialog.askdirectory(initialdir=iDir)
        if len(folder_path) > 0:
            self.open_folder_func(folder_path)
    
    def update_count_text(self,current_cnt,num_files):
        self.file_count_label.config(text=f"{current_cnt+1} / {num_files}")
