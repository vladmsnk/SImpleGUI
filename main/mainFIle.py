from tkinter import *
import tkinter.ttk as ttk
from configs.config import gui_height,gui_width,table_columns,clean_data_path
import pandas as pd

data = pd.read_csv(clean_data_path)

root = Tk()
root.resizable(False,False)
root.title("Analyse")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (gui_width / 2)
y = (screen_height / 2) - (gui_height / 2)
root.geometry("%dx%d+%d+%d" % (gui_width, gui_height, x, y))
frame1 = Frame(root, width=600, height=350, bg='green')
frame2 = Frame(root, width=600, height=350, bg='yellow')
frame3 = Frame(root, width=1200, height=350, bg='blue')
frame1.grid(row=0, column=0, sticky="ns")
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=0, columnspan=2, sticky="we")


columns = list(data.columns)

scrollbarx = Scrollbar(frame3, orient=HORIZONTAL)
scrollbary = Scrollbar(frame3, orient=VERTICAL)
table = ttk.Treeview(frame3, columns= columns, show ='headings',yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=table.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=table.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
for head in columns:
    table.heading(head, text=head, anchor='center')
    table.column(head, anchor='center',stretch=NO, minwidth=50, width=100)
for str_num in range(data.shape[0]):
    table.insert('',END,values = list(data.iloc[str_num]))
table.pack(expand=YES, fill=BOTH)


root.mainloop()