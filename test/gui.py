from tkinter import *
import tkinter.ttk as ttk
import csv
import pandas as pd

def download():
    TableMargin = Frame(root, width=400)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("title", "authors", "average_rating", 'language_code'), height=400,
                        selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('title', text="title", anchor=W)
    tree.heading('authors', text="authors", anchor=W)
    tree.heading('average_rating', text="average_rating", anchor=W)
    tree.heading('language_code', text="language_code", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.column('#4', stretch=NO, minwidth=0, width=300)
    tree.pack()
    with open('../data/new.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            title = row['title']
            authors = row['authors']
            average_rating = row['average_rating']
            language_code = row['language_code']
            tree.insert("", 0, values=(title, authors, average_rating, language_code))
def get():
    da = pd.read_csv('../data/new.csv')
    value = name.get()
    value = value.split(',')
    label = Label(root,text = str(da.iloc[int(value[0]),int(value[1])]))
    label.pack()

root = Tk()
root.title("Python - Import CSV File To Tkinter Table")
width = 800
height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

name = Entry(root)
name.pack()
button = Button(root, text = 'Download',command = download)
button.pack()

button1 = Button(root, text = 'get_info',command = get)
button1.pack()

# name = Entry(roo)


#
#
# with open('../data/new.csv') as f:
#     reader = csv.DictReader(f, delimiter=',')
#     for row in reader:
#         title = row['title']
#         authors = row['authors']
#         average_rating = row['average_rating']
#         language_code = row['language_code']
#         tree.insert("", 0, values=(title, authors, average_rating,language_code))



if __name__ == '__main__':
    root.mainloop()