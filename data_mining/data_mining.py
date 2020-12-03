"""
    Cross-industry standard process for data mining

"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from data_mining.vars import download, adult_data, adult_test, adult_data_test
from data_mining import crawler
from data_mining.utils import (
    append_files,
    create_continent_column,
    delete_lines,
    replace_characters,
    build_final_decision_tree,
    build_decision_tree,
    create_index
)

models = []

def get_data():
    print('Extracting data from website...')
    crawler.extract_data()
    print('Data has been extracted.')

def integrate_data():
    print(f'Appending {adult_data_test}...')
    append_files(
        output_file=adult_data_test,
        input_filenames=[adult_data, adult_test],
        basepath=download
    )
    print(f'Data from {adult_data} and {adult_test} has been appended to {adult_data_test}.')

def clean_data(filename):
    print('Deleting invalid lines...')
    delete_lines(bad_word="?", basepath=download, filename=filename)
    delete_lines(bad_word="|1x3", basepath=download, filename=filename)
    delete_lines(bad_word="South", basepath=download, filename=filename)
    replace_characters(', ', ',', filename=filename)
    print('Invalid lines deleted.')

def build_data(filename):
    print('Building data...')
    create_index()
    create_continent_column(basepath=download, filename=filename)
    print('Data has been builded.')

def format_data(filename):
    print('Formatting data...')
    # Salary
    replace_characters('>50K.', '>50K', filename=filename)
    replace_characters('<=50K.', '<=50K', filename=filename)
    # Country
    replace_characters('Columbia', 'Colombia', filename=filename)
    replace_characters('Hong', 'Hong Kong', filename=filename)
    replace_characters('Trinadad&Tobago', 'Trinidad and Tobago', filename=filename)
    replace_characters('United-States', 'United States', filename=filename)
    replace_characters('Puerto-Rico', 'Puerto Rico', filename=filename)
    replace_characters('Dominican-Republic', 'Dominican Republic', filename=filename)
    replace_characters('El-Salvador', 'El Salvador', filename=filename)
    replace_characters('Holand-Netherlands', 'Netherlands', filename=filename)
    print('Data has been formatted.')

def build_final_tree(filename):
    print('Building decision tree...')
    build_final_decision_tree(filename)
    print('Decision tree has been built')
    
def clear_decision_model():
    print('cleared')

def build_tree(columns, criterion, splitter, max_depth, min_samples_split, test_size):
    print('Building decision tree...')
    build_decision_tree(columns, criterion, splitter, max_depth, min_samples_split, test_size)
    print('Decision tree has been built')