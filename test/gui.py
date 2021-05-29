from tkinter import *
import tkinter.ttk as ttk
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
def make_plot():
    da = pd.read_csv('../data/new.csv')
    fig = Figure(figsize=(6, 6))
    a = fig.add_subplot(111)
    a.hist(da.average_rating)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()
    canvas.draw()
    # plt.title('distribution')
    # plt.xlabel('average rating')
    # plt.show()
    # plt.gcf().canvas.draw()
    # fig = plt.figure()
    # canvas = FigureCanvasTkAgg(fig, master=root)
    # canvas.get_tk_widget().pack()
    # canvas.draw()
def download():
    TableMargin = Frame(root, width=300)
    TableMargin.pack()
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("title", "authors", "average_rating", 'language_code','num_pages','text_reviews_count','publication_date','publisher','pub_year','century'),
                        selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('title', text="title", anchor=W)
    tree.heading('authors', text="authors", anchor=W)
    tree.heading('average_rating', text="average_rating", anchor=W)
    tree.heading('language_code', text="language_code", anchor=W)

    tree.heading('num_pages', text='num_pages',anchor = W)
    tree.heading('text_reviews_count', text="text_reviews_count", anchor=W)
    tree.heading('publication_date', text="publication_date", anchor=W)
    tree.heading('publisher', text="publisher", anchor=W)
    tree.heading('pub_year', text="pub_year", anchor=W)
    tree.heading('century', text="century", anchor=W)
    # tree.heading('is_big_book', text="is_big_book", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
    tree.column('#7', stretch=NO, minwidth=0, width=100)
    tree.column('#8', stretch=NO, minwidth=0, width=100)
    tree.column('#9', stretch=NO, minwidth=0, width=100)
    tree.column('#10', stretch=NO, minwidth=0, width=100)
    tree.pack()
    with open('../data/new.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            title = row['title']
            authors = row['authors']
            average_rating = row['average_rating']
            language_code = row['language_code']
            num_pages = row['num_pages']
            text_reviews_count = row['text_reviews_count']
            publication_date = row['publication_date']
            publisher = row['publisher']
            pub_year = row['pub_year']
            century = row['century']
            # is_big_book = row['is_big_book']
            tree.insert("", 0, values=(title, authors, average_rating, language_code,num_pages,text_reviews_count,publication_date,publisher,pub_year,century))

def get():
    da = pd.read_csv('../data/new.csv')
    value = name.get()
    value = value.split(',')
    label = Label(root,text = str(da.iloc[int(value[0]),int(value[1])]))
    label.pack()

root = Tk()
root.title("Python - Import CSV File To Tkinter Table")
width = 1500
height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))


name = Entry(root)
name.pack(side = LEFT)
button = Button(root, text = 'Download',command = download)
button.pack(side = LEFT)

button1 = Button(root, text = 'get_info',command = get)
button1.pack(side = LEFT)

button2 = Button(root, text ='make plot', command = make_plot)
button2.pack(side = LEFT)


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