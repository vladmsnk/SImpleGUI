# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:44:33 2021

@author: Администратор
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from 


# 'title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code',
# '  num_pages', 'ratings_count', 'text_reviews_count',
# 'publication_date', 'publisher'

plt.figure(figsize=(15, 10))


# 1 количество рецензий - название книги (ПЕРЕВЕРНУТЬ....)
def text_reviews_count_title():
    plt.figure(figsize=(12, 7))
    highest_reviews = data.nlargest(10, ['text_reviews_count'])
    plt.plot(highest_reviews['text_reviews_count'], highest_reviews['title'], color='r')
    plt.grid()
    plt.xlabel('Количество рецензий')
    plt.ylabel('Название книги')
    plt.savefig('text_reviews_count_title.png')


# 2 средний рейтинг - количество страниц (ДОБАВИТЬ СРЕДНЮЮ ЛИНИЮ)
def average_rating_num_pages():
    plt.figure(figsize=(12, 7))
    # highest_reviews = data.nlargest(20000, ['num_pages'])
    plt.scatter(data['num_pages'], data['average_rating'], color='r', )
    plt.xlim(0, 2000)
    plt.grid()
    plt.xlabel('Количество страниц')
    plt.ylabel('Средний рейтинг')
    plt.savefig('average_rating_num_pages.png')


# 3 количество рецензий - количество оценок (ДОРАБОТАТЬ КАК 2)
def text_reviews_count_ratings_count():
    plt.figure(figsize=(12, 7))
    plt.scatter(data['text_reviews_count'], data['ratings_count'], color='r', )
    plt.ylim(0, 500000)
    plt.xlim(0, 20000)
    plt.grid()
    plt.xlabel('Количество рецензий')
    plt.ylabel('Количество оценок')
    plt.savefig('text_reviews_count_ratings_count.png')


# 4 количество книг - язык
def number_of_books_langeuage(df, nGraphShown, nGraphPerRow):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[
        col] < 50]]  # For displaying purposes, pick columns that have between 1 and 50 unique values
    nRow, nCol = df.shape
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(num=None, figsize=(6 * nGraphPerRow, 8 * nGraphRow), dpi=80, facecolor='w', edgecolor='k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.xlabel('Язык')
        plt.ylabel('Количество книг')
        plt.xticks(rotation=90)
    plt.tight_layout(pad=1.0, w_pad=1.0, h_pad=1.0)
    plt.savefig('number_of_books_langeuage.png')


text_reviews_count_title()
average_rating_num_pages()
text_reviews_count_ratings_count()
number_of_books_langeuage(data, 100, 100)
