"""
    Cross-industry standard process for data mining

"""
from data_mining.vars import download, adult_data, adult_test, adult_data_test
from data_mining import crawler
from data_mining.utils import (
    append_files,
    create_continent_column,
    delete_lines,
    replace_characters
)

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

def clean_data():
    print('Deleting invalid lines...')
    delete_lines(bad_word="?", basepath=download, filename=adult_data_test)
    delete_lines(bad_word="|1x3", basepath=download, filename=adult_data_test)
    delete_lines(bad_word="South", basepath=download, filename=adult_data_test)
    print('Invalid lines deleted.')

def build_data():
    print('Building data...')
    replace_characters('<=50K.', '1')
    replace_characters('>50K.', '2')
    replace_characters('<=50K', '1')
    replace_characters('>50K', '2')
    replace_characters('Female', 'F')
    replace_characters('Male', 'M')
    create_continent_column(basepath=download, filename=adult_data_test)
    print('Data has been builded.')

def format_data():
    print('Formatting data...')
    replace_characters('Columbia', 'Colombia')
    replace_characters('Hong', 'Hong Kong')
    replace_characters('Trinadad&Tobago', 'Trinidad and Tobago')
    replace_characters('United-States', 'United States')
    replace_characters('Puerto-Rico', 'Puerto Rico')
    replace_characters('Dominican-Republic', 'Dominican Republic')
    replace_characters('El-Salvador', 'El Salvador')
    replace_characters('Holand-Netherlands', 'Netherlands')
    print('Data has been formatted.')
