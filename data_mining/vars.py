download = 'download/'
adult_data = 'adult.data'
adult_names = 'adult.names'
adult_test = 'adult.test'
adult_data_test = 'adult.data.test'
chromedriver_path = 'res/chromedriver'
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/%s'

download_data = download + adult_data
download_names = download + adult_names
download_test = download + adult_test

url_download_data = url % adult_data
url_download_names = url % adult_names
url_download_test = url % adult_test

TIMEOUT=30