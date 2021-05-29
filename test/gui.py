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
    TableMargin = Frame(root, width=10)
    TableMargin.pack(side= RIGHT)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    columns = ("title", "authors", "average_rating", 'language_code','num_pages','text_reviews_count','publication_date','publisher','pub_year','century')
    tree = ttk.Treeview(TableMargin, columns= columns, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    for i in columns:
        tree.heading(f'{i}', text=f'{i}', anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    for i in range(1,11):
        tree.column(f'#{i}', stretch=NO, minwidth=0, width=100)
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