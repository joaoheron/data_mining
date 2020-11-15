import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics, preprocessing
from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus
from data_mining.vars import (
    download,
    adult_data,
    adult_test,
    adult_data_test,
    adult_col_names,
    continents
)

def append_files(output_file=adult_data_test, input_filenames=[adult_data, adult_test], basepath=download):
    with open(basepath + output_file, 'w') as outfile:
        for fname in input_filenames:
            with open(basepath + fname) as infile:
                for line in infile:
                    outfile.write(line)
        outfile.close()

def apply_lower_case(basepath=download, filename=adult_data_test):
    with open(basepath + filename, 'r') as infile, open(basepath + 'outfile', 'w') as outfile:
        for line in infile:
            outfile.write(str(line).lower())
        infile.close()
        outfile.close()
        os.remove(basepath + filename)
        os.rename(basepath + 'outfile', basepath + filename)

def create_continent_column(basepath=download, filename=adult_data_test):
    with open(basepath + filename, 'r') as infile, open(basepath + 'outfile', 'w') as outfile:
        for line in infile:
            outfile.write(line.replace('\n', '') + ',' + get_continent(str(line)) + '\n')
        infile.close()
        outfile.close()
        os.remove(basepath + filename)
        os.rename(basepath + 'outfile', basepath + filename)

def delete_lines(bad_word='?', basepath=download, filename=adult_data_test):
    with open(basepath + filename, 'r') as infile, open(basepath + 'outfile', 'w') as outfile:
        for line in infile:
            if (not bad_word in line) and line.strip() != "":
                outfile.write(line)
            else:
                print(f'bad word: {bad_word}')
        infile.close()
        outfile.close()
        os.remove(basepath + filename)
        os.rename(basepath + 'outfile', basepath + filename)

def get_continent(line):
    print(f'LINE:{line}')
    country = line.split(',', 15)[14]
    if country in continents['africa']:
        return 'Africa'
    elif country in continents['asia']:
        return 'Asia'
    elif country in continents['central_america']:
        return 'Central America'
    elif country in continents['europe']:
        return 'Europe'
    elif country in continents['north_america']:
        return 'North America'
    elif country in continents['south_america']:
        return 'South America'
    return 'INVALID'

def get_db_props_from_url(url):
    db_host = url.split('@')[1].split(':')[0]
    db_name = url.split('/', 4)[3]
    db_user = url.split(':')[1].replace('//', '')
    db_pass = url.split(':', 3)[2].split('@')[0]
    db_port = url.split(':', 4)[3].split('/')[0]
    return db_host, db_name, db_user, db_pass, db_port

def replace_characters(replaced, replace, basepath=download, filename=adult_data_test):
    with open(basepath + filename, 'r') as infile, open(basepath + 'outfile', 'w') as outfile:
        for line in infile:
            outfile.write(str(line).replace(replaced, replace))
        infile.close()
        outfile.close()
        os.remove(basepath + filename)
        os.rename(basepath + 'outfile', basepath + filename)

def create_index(basepath=download, filename=adult_data_test):
    with open(basepath + filename, 'r') as infile, open(basepath + 'outfile', 'w') as outfile:
        i = 1
        for line in infile:
            outfile.write(str(i) + ',' + str(line))
            i+=1
        infile.close()
        outfile.close()
        os.remove(basepath + filename)
        os.rename(basepath + 'outfile', basepath + filename)

def build_decision_tree(data_set=adult_data_test):
    col_names = adult_col_names
    # Loading data set into pandas dataframe
    df = pd.read_csv(download + data_set, header=None, names=col_names)
    df.head()

    # Encoding labels into numeric values
    # Column workclass
    le_workclass = preprocessing.LabelEncoder()
    le_workclass.fit(df['workclass'])
    list(le_workclass.classes_)
    df['workclass'] = le_workclass.transform(df['workclass'])

    # Column education
    df = df.drop(columns=['education'])

    # Column marital-status
    le_marital_status = preprocessing.LabelEncoder()
    le_marital_status.fit(df['marital-status'])
    list(le_marital_status.classes_)
    df['marital-status'] = le_marital_status.transform(df['marital-status'])

    # Column education
    le_occupation = preprocessing.LabelEncoder()
    le_occupation.fit(df['occupation'])
    list(le_occupation.classes_)
    df['occupation'] = le_occupation.transform(df['occupation'])

    # Column relationship
    le_relationship = preprocessing.LabelEncoder()
    le_relationship.fit(df['relationship'])
    list(le_relationship.classes_)
    df['relationship'] = le_relationship.transform(df['relationship'])

    # Column race
    le_race = preprocessing.LabelEncoder()
    le_race.fit(df['race'])
    list(le_race.classes_)
    df['race'] = le_race.transform(df['race'])

    # Column sex
    le_sex = preprocessing.LabelEncoder()
    le_sex.fit(df['sex'])
    list(le_sex.classes_)
    df['sex'] = le_sex.transform(df['sex'])

    # Column native-country
    le_native_country = preprocessing.LabelEncoder()
    le_native_country.fit(df['native-country'])
    list(le_native_country.classes_)
    df['native-country'] = le_native_country.transform(df['native-country'])

    # Column salary
    le_salary = preprocessing.LabelEncoder()
    le_salary.fit(df['salary'])
    list(le_salary.classes_)
    df['salary'] = le_salary.transform(df['salary'])

    # Column continent
    le_continent = preprocessing.LabelEncoder()
    le_continent.fit(df['continent'])
    list(le_continent.classes_)
    df['continent'] = le_continent.transform(df['continent'])

    # split dataset in features(independent) and target variable(dependent)
    independent_cols = ['education-num', 'marital-status', 'race', 'sex', 'hours-per-week']
    dependent_cols = ['salary']

    df_independent = df[independent_cols] # Features variables
    df_dependent = df[dependent_cols] # Target variable

    print(str(df_independent))
    print(str(df_dependent))

    # Creating random training and test sets
    x_train, x_test, y_train, y_test = train_test_split(df_independent, df_dependent, test_size=0.3, random_state=1) # 70% training and 30% test

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

    # Train Decision Tree Classifer
    clf = clf.fit(x_train, y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(x_test)

    print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
    dot_data = StringIO()
    export_graphviz(
        clf,
        out_file=dot_data,
        filled=True,
        rounded=True,
        special_characters=True,
        feature_names=independent_cols,
        class_names=['0','1']
    )
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_png('adults.png')
    Image(graph.create_png())
