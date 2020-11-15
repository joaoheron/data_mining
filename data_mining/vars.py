download = 'download/'
adult_data = 'adult.data'
adult_names = 'adult.names'
adult_test = 'adult.test'
adult_data_test = 'adult.data.test'
chromedriver_path = 'res/chromedriver'
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/%s'

adult_col_names = [
    'age',
    'workclass',
    'fnlwgt',
    'education',
    'education-num',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'capital-gain',
    'capital-loss',
    'hours-per-week',
    'native-country',
    'salary',
    'continent'
]

africa = []
asia = ['Cambodia', 'India', 'Japan', 'China', 'Iran', 'Philippines', 'Vietnam', 'Laos', 'Taiwan','Thailand', 'Hong']
central_america = ['Cuba', 'Honduras', 'Jamaica', 'Dominican-Republic', 'Haiti', 'Guatemala', 'Nicaragua', 'El-Salvador', 'Trinadad&Tobago']
europe = ['Germany', 'England', 'Greece', 'Italy', 'Poland', 'Portugal', 'Ireland', 'France', 'Hungary', 'Scotland', 'Yugoslavia', 'Holand-Netherlands']
north_america = ['United-States', 'Canada', 'Mexico', 'Puerto-Rico', 'Outlying-US(Guam-USVI-etc)']
south_america = ['Ecuador', 'Columbia', 'Peru']

continents = {
    'africa': africa,
    'asia': asia,
    'central_america': central_america,
    'europe': europe,
    'north_america': north_america,
    'south_america': south_america
}

download_data = download + adult_data
download_names = download + adult_names
download_test = download + adult_test

url_download_data = url % adult_data
url_download_names = url % adult_names
url_download_test = url % adult_test

TIMEOUT=30