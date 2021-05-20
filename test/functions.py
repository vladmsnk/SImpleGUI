
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path = '../data/books.csv'
def make_plot(piv_data):
    plt.hist(piv_data['text_reviews_count'])

def make_data(path):
    data = pd.read_csv(path, error_bad_lines=(False))
    data.drop('bookID', axis=1, inplace=True)
    data.drop('isbn', axis=1, inplace=True)
    data.drop('isbn13', axis=1, inplace=True)
    data.dropna(0, inplace=True)
    data.replace(to_replace=('en-US', 'en-GB', 'en-CA'), value='eng', inplace=True)
    data.rename(columns={'  num_pages': 'num_pages'}, inplace=True)
    return data
def add_year_column(data):
    data['pub_year'] = data['publication_date'].apply(lambda x: int(x.split('/')[2]))
    data['century'] = data['pub_year'].apply(lambda x: '20th' if x < 2000 else '21th')
    return data
def add_binary_column(data):
    data['is_big_book'] =data['num_pages'].apply(lambda x: 'big' if x > 400 else 'small')
    return data


def save_normal_data(data):
    data.to_csv('clean_data.csv')

data = make_data(path)
data = add_year_column(data)
data = add_binary_column(data)

def make_pivot_table(data):
    pivot1 = pd.pivot_table(data, index= ['language_code'])
    pivot2 = pd.pivot_table(data, index= ['is_big_book'])
    pivot3 = pd.pivot_table(data, index= ['century'])
    return (pivot1,pivot2,pivot3)

piv_tuple = make_pivot_table(data)
piv1 = piv_tuple[0]
piv2  = piv_tuple[1]
piv3 = piv_tuple[2]

plt.title("distribution")
plt.hist(piv1['text_reviews_count'])
plt.xlabel('mean text reviews count for each publisher')
plt.savefig('first.png')
plt.show()


