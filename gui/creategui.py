from tkinter import *
import tkinter.ttk as ttk
from configs.config import gui_height,gui_width,table_columns,clean_data_path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import csv
import numpy as np

path = clean_data_path
tmp_columns = [
    "Название", "Автор", "Средний", 'Язык', 'Количество', 'Количество рейтингов','Количество отзывов', 'Дата публикации',
    'Издательство', 'Год публикации', 'Век публикации','Большая ли она']

tmp_data = pd.read_csv('../data/clean_data.csv')


def show():
    if combo_plot1.get() != 'choose':
        for widgets in frame22.winfo_children():
            widgets.destroy()
        if combo_plot1.get() != combo_plot2.get() and combo_plot1.get() != 'choose'and combo_plot2.get() != 'choose':
            figure = plt.Figure(figsize=(5,2))
            ax = figure.add_subplot(111)
            ax.scatter(tmp_data[combo_plot1.get()],tmp_data[combo_plot2.get()],s = 7)
            chart_type = FigureCanvasTkAgg(figure, frame22)
            chart_type.get_tk_widget().place(x=10, y=10)
            # ax.set_xlabel(combo_plot1.get())
            # ax.set_ylabel(combo_plot1.get())
        elif combo_plot1.get() != 'choose'and combo_plot2.get() != 'choose' and combo_plot1.get() == combo_plot2.get():
            figure = plt.Figure(figsize=(5, 2))
            ax = figure.add_subplot(111)
            ax.hist(tmp_data[combo_plot1.get()])
            chart_type = FigureCanvasTkAgg(figure,frame22)
            chart_type.get_tk_widget().place(x = 10, y =10)




def download():
    scrollbarx = Scrollbar(frame3, orient=HORIZONTAL)
    scrollbary = Scrollbar(frame3, orient=VERTICAL)
    columns = (
    "title", "authors", "average_rating", 'language_code', 'num_pages', 'ratings_count','text_reviews_count', 'publication_date',
    'publisher', 'pub_year', 'century')

    tree = ttk.Treeview(frame3, columns=columns, selectmode="extended",height = 15)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side = RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side = BOTTOM, fill=X)
    for i in columns:
        tree.heading(f'{i}', text=f'{i}', anchor=W)
    # tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column("#0", minwidth=0, width=0)
    for i in range(1, 12):
        tree.column(f'#{i}', stretch=NO, minwidth=106, width=106)

    tree.pack()
    with open(path) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            title = row['title']
            authors = row['authors']
            average_rating = row['average_rating']
            language_code = row['language_code']
            num_pages = row['num_pages']
            ratings_count = row['ratings_count']
            text_reviews_count = row['text_reviews_count']
            publication_date = row['publication_date']
            publisher = row['publisher']
            pub_year = row['pub_year']
            century = row['century']
            # is_big_book = row['is_big_book']
            tree.insert("", 0, values=(
            title, authors, average_rating, language_code, num_pages,ratings_count, text_reviews_count, publication_date, publisher,
            pub_year, century))

def check(av2,pag2,rate2,rew2):
    result = (np.array([av2,pag2,rate2,rew2]) !=0)
    return result

def reload():
    av1 = float(var_2.get())
    av2 = float(var_3.get())
    pag1 = int(var_4.get())
    pag2 = int(var_5.get())
    rate1 = float(var_6.get())
    rate2 = float(var_7.get())
    rew1 = int(var_8.get())
    rew2 = int(var_9.get())
    chk = check(av2,pag2,rate2,rew2)
    newcsv = []
    with open(clean_data_path) as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        reader = list(reader)

    with open('../data/reload.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        if not newcsv:
            newcsv.append(reader[0])
            spamwriter.writerow(reader[0])
            reader.pop(0)
        for str in reader:
            if av2 > float(str[3])  > av1 and pag2 > int(str[5])  > pag1 \
                    and rate2 > int(str[6]) > rate1 and rew2 > int(str[7]) > rew1:
                newcsv.append(str)
                spamwriter.writerow(str)
    global tmp_data
    tmp_data = pd.read_csv('../data/reload.csv')
    # tmp_data.rename(columns=tmp_columns)
    # print(tmp_columns)
    # print(tmp_data.columns)
def download_main():
    for widgets in frame3.winfo_children():
        widgets.destroy()
    global path
    path = clean_data_path
    download()

def update_table():
    for widgets in frame3.winfo_children():
        widgets.destroy()
    global path
    reload()
    path = '../data/reload.csv'
    download()



root = Tk()
root.title("Analyse")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (gui_width / 2)
y = (screen_height / 2) - (gui_height / 2)
root.geometry("%dx%d+%d+%d" % (gui_width, gui_height, x, y))
frame1 = Frame(root, width=600, height=350)
frame2 = Frame(root, width=600, height=100)
frame22 = Frame(root, width=600, height=300)
frame3 = Frame(root, width=1200, height=300)
frame1.place(x = 10, y =10 )
frame2.place(x = 610, y =10 )
frame22.place(x = 610, y =110)
frame3.place(x = 10, y = 360)



lbl_0 = Label(frame1, text='Отбор по базе данных')
lbl_0.config(font=("Courier", 12))
lbl_0.place( x =0, y = 0)
lbl_1 = Label(frame2, text='Построение зависимостей')
lbl_1.config(font=("Courier", 12))
lbl_1.place(x = 0 , y =0)
var_2 = DoubleVar()
var_3 = DoubleVar()
var_4 = DoubleVar()
var_5 = DoubleVar()
var_6 = DoubleVar()
var_7 = DoubleVar()
var_8 = DoubleVar()
var_9 = DoubleVar()


lbl_2 = Label(frame1, text="Average rating from")
lbl_2.grid(row=1, column=1)
sca_2= Scale(frame1, variable = var_2, orient=HORIZONTAL, length=150, from_=0, to=5, tickinterval=1, resolution=0.1)
sca_2.grid(row=1, column=3)
# btn_0 = Button(root, text="Get Scale Value", command=sel) #обработка значения курсора
# btn_0.grid(row=3, column=6)
lbl_3 = Label(frame1, text="to")
lbl_3.grid(row=1, column=4)
sca_3= Scale(frame1, variable = var_3, orient=HORIZONTAL, length=150, from_=0, to=5, tickinterval=1, resolution=0.1)
sca_3.set(5.0)
sca_3.grid(row=1, column=5)
lbl_4 = Label(frame1, text="Number of pages from")
lbl_4.grid(row=2, column=1)
sca_4= Scale(frame1,variable = var_4, orient=HORIZONTAL, length=150, from_=0, to=6576, tickinterval=3288, resolution=1)
sca_4.grid(row=2, column=3)
lbl_5 = Label(frame1, text="to")
lbl_5.grid(row=2, column=4)
sca_5= Scale(frame1,variable = var_5, orient=HORIZONTAL, length=150, from_=0, to=6576, tickinterval=3288, resolution=1)
sca_5.set(6576.0)
sca_5.grid(row=2, column=5)
lbl_6 = Label(frame1, text="Rating count from")
lbl_6.grid(row=3, column=1)
sca_6= Scale(frame1, variable = var_6, orient=HORIZONTAL, length=150, from_=0, to=250000, tickinterval=250000, resolution=1000)
sca_6.grid(row=3, column=3)
lbl_7 = Label(frame1, text="to")
lbl_7.grid(row=3, column=4)
sca_7= Scale(frame1, variable = var_7, orient=HORIZONTAL, length=150, from_=0,  to=250000, tickinterval=250000, resolution=1000)
sca_7.set(4600000.0)
sca_7.grid(row=3, column=5)
lbl_8 = Label(frame1, text="Text reviews from")
lbl_8.grid(row=4, column=1)
sca_8= Scale(frame1,variable = var_8, orient=HORIZONTAL, length=150, from_=0, to=20000, tickinterval=20000, resolution=100)
sca_8.grid(row=4, column=3)
lbl_9 = Label(frame1, text="to")
lbl_9.grid(row=4, column=4)
sca_9= Scale(frame1,variable = var_9, orient=HORIZONTAL, length=150, from_=0, to=20000, tickinterval=20000, resolution=100)
sca_9.set(94300)
sca_9.grid(row=4, column=5)


download_init_data_base = Button(frame1, text ='Скачать',command=download_main)
download_init_data_base.grid(row=5, column=1)
reload_data_base= Button(frame1, text='Обновить базу данных', command=update_table)
reload_data_base.grid(row=5, column=2)

values = ['Choose', 'average_rating','num_pages','ratings_count','text_reviews_count']


combo_hist =ttk.Combobox(frame2,values = values)
graph_label = Label(frame2, text ='График',font='bold')
graph_label.place(x =0, y= 30)
combo_plot1 = ttk.Combobox(frame2,values =values )
combo_plot2 = ttk.Combobox(frame2,values =values )
combo_plot1.place(x = 0, y = 60)
combo_plot2.place(x = 200, y = 60)
combo_plot1.current(0)
combo_plot2.current(0)
ttk.Button(frame2, text = 'PLOT' ,command =show).place(x = 60, y = 30)


root.mainloop()
