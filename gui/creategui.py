from tkinter import *
import tkinter.ttk as ttk
from configs.config import guI_height,gui_width

def make_root():
    root = Tk()
    root.title("Python - Import CSV File To Tkinter Table")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (gui_width / 2)
    y = (screen_height / 2) - (guI_height / 2)
    root.geometry("%dx%d+%d+%d" % (gui_width, guI_height, x, y))
    return root


