from tkinter import *
import tkinter.ttk as ttk
from configs.config import gui_height,gui_width,table_columns,clean_data_path
import pandas as pd
import csv
import numpy as np

path = clean_data_path
def download():
    scrollbarx = Scrollbar(frame3, orient=HORIZONTAL)
    scrollbary = Scrollbar(frame3, orient=VERTICAL)
    columns = (
    "title", "authors", "average_rating", 'language_code', 'num_pages', 'text_reviews_count', 'publication_date',
    'publisher', 'pub_year', 'century')
    tree = ttk.Treeview(frame3, columns=columns, selectmode="extended", yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side = RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side = BOTTOM, fill=X)
    for i in columns:
        tree.heading(f'{i}', text=f'{i}', anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    for i in range(1, 11):
        tree.column(f'#{i}', stretch=NO, minwidth=0, width=150)
    tree.pack()
    with open(path) as f:
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
            tree.insert("", 0, values=(
            title, authors, average_rating, language_code, num_pages, text_reviews_count, publication_date, publisher,
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
            if all(chk) and av2 > float(str[3])  > av1 and pag2 > int(str[5])  > pag1 \
                    and rate2 > int(str[6]) > rate1 and rew2 > int(str[7]) > rew1:
                newcsv.append(str)
                spamwriter.writerow(str)
            elif all(chk[:3]) and not chk[-1] and av2 > float(str[3])  > av1 and pag2 > int(str[5])  > pag1 \
                    and rate2 > int(str[6]) > rate1:
                newcsv.append(str)
                spamwriter.writerow(str)

            elif chk[0] and not chk[1] and all(chk[2:]) and av2 > float(str[3])  > av1 \
                and rate2 > int(str[6]) > rate1 and rew2 > int(str[7]) > rew1:
                newcsv.append(str)
                spamwriter.writerow(str)

            elif chk[-1] and not chk[2] and all(chk[:2]) and av2 > float(str[3])  > av1 and pag2 > int(str[5])  > pag1 \
                and rew2 > int(str[7]) > rew1:
                newcsv.append(str)
                spamwriter.writerow(str)

            elif all(chk[1:]) and not chk[0] and pag2 > int(str[5])  > pag1 \
                    and rate2 > int(str[6]) > rate1 and rew2 > int(str[7]) > rew1:
                newcsv.append(str)
                spamwriter.writerow(str)

            elif all(chk[:2]) and not any(chk[2:]) and av2 > float(str[3]) > av1 and pag2 > int(str[5]) > pag1:
                newcsv.append(str)
                spamwriter.writerow(str)

            elif all(chk[2:]) and not any(chk[:2]) and rate2 > int(str[6]) > rate1 and rew2 > int(str[7]) > rew1:
                newcsv.append(str)
                spamwriter.writerow(str)
            elif all(chk[1:3]) and not chk[0] and not chk[-1] and pag2 > int(str[5])  > pag1 and rate2 > int(str[6]) > rate1:
                newcsv.append(str)
                spamwriter.writerow(str)
            elif chk[0] and chk[2] and not chk[1] and not chk[-1] and av2 > float(str[3])  > av1 and rate2 > int(str[6]) > rate1:
                newcsv.append(str)
                spamwriter.writerow(str)

            elif chk[1] and not chk[0] and not chk[3] and chk[-1] and pag2 > int(str[5])  > pag1 and rew2 > int(str[7]) > rew1:
                newcsv.append(str)
                spamwriter.writerow(str)

            elif  (chk[0] and not any(chk[1:]) and av2 > float(str[3])  > av1) or (chk[1] and not chk[0] and not any(chk[2:]) and pag2 > int(str[5])  > pag1 ) or \
                    (not any(chk[:2]) and chk[3] and not chk[-1] and rate2 > int(str[6]) > rate1) or (not any(chk[:3]) and chk[-1] and rew2 > int(str[7]) > rew1) :
                newcsv.append(str)
                spamwriter.writerow(str)
def change_frame():
    for widgets in frame3.winfo_children():
        widgets.destroy()


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
frame1 = Frame(root, width=600, height=350 )
frame2 = Frame(root, width=600, height=350)
frame3 = Frame(root, width=1200, height=350)
frame1.grid(row=0, column=0, sticky="ns")
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=0, columnspan=2, sticky="we")



lbl_0 = Label(frame1, text='Отбор по базе данных')
lbl_0.config(font=("Courier", 12))
lbl_0.grid(row=0, column=3, columnspan=2, rowspan=1)
lbl_1 = Label(frame1, text='Построение зависимостей')
lbl_1.config(font=("Courier", 12))
lbl_1.grid(row=0,column=9)
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
sca_6= Scale(frame1, variable = var_6, orient=HORIZONTAL, length=150, from_=0, to=4600000, tickinterval=4600000, resolution=1000)
sca_6.grid(row=3, column=3)
lbl_7 = Label(frame1, text="to")
lbl_7.grid(row=3, column=4)
sca_7= Scale(frame1, variable = var_7, orient=HORIZONTAL, length=150, from_=0,  to=4600000, tickinterval=4600000, resolution=1000)
sca_7.set(4600000.0)
sca_7.grid(row=3, column=5)
lbl_8 = Label(frame1, text="Text reviews from")
lbl_8.grid(row=4, column=1)
sca_8= Scale(frame1,variable = var_8, orient=HORIZONTAL, length=150, from_=0, to=94300, tickinterval=94300, resolution=100)
sca_8.grid(row=4, column=3)
lbl_9 = Label(frame1, text="to")
lbl_9.grid(row=4, column=4)
sca_9= Scale(frame1,variable = var_9, orient=HORIZONTAL, length=150, from_=0, to=94300, tickinterval=94300, resolution=100)
sca_9.set(94300)
sca_9.grid(row=4, column=5)

download_init_data_base = Button(frame1, text ='Скачать',command=download)
download_init_data_base.grid(row=5, column=1)
reload_data_base= Button(frame1, text='Обновить базу данных', command=update_table)
reload_data_base.grid(row=5, column=2)



root.mainloop()
