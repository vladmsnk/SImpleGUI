
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path = 'data/books.csv'

def make_data(path):
    data = pd.read_csv(path, error_bad_lines=(False))
    data.drop('bookID', axis=1, inplace=True)
    data.drop('isbn', axis=1, inplace=True)
    data.drop('isbn13', axis=1, inplace=True)
    data.dropna(0, inplace=True)
    data.replace(to_replace=('en-US', 'en-GB', 'en-CA'), value='eng', inplace=True)
    data.rename(columns={'  num_pages': 'num_pages'}, inplace=True)
    return data
def save_normal_data(data):
    data.to_csv('clean_data.csv')

