import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics, preprocessing
from sklearn.compose import ColumnTransformer
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

    # Dropping Column education because all needed info is on education-num
    df = df.drop(columns=['education'])

    # Encoding labels into numeric values using dummies values approach:
    # Column workclass
    df_workclass = df['workclass']
    dummy_workclass_df = pd.get_dummies(df_workclass, columns=['workclass'], prefix='workclass_is')
    print(str(dummy_workclass_df))

    # Column marital-status
    df_marital_status = df['marital-status']
    dummy_marital_status_df = pd.get_dummies(df_marital_status, columns=['marital-status'], prefix='marital-status_is')
    print(str(dummy_marital_status_df))

    # Column occupation
    df_occupation = df['occupation']
    dummy_occupation_df = pd.get_dummies(df_occupation, columns=['occupation'], prefix='occupation_is')
    print(str(dummy_occupation_df))

    # Column relationship
    df_relationship = df['relationship']
    dummy_relationship_df = pd.get_dummies(df_relationship, columns=['relationship'], prefix='relationship_is')
    print(str(dummy_relationship_df))

    # Column race
    df_race = df['race']
    dummy_race_df = pd.get_dummies(df_race, columns=['race'], prefix='race_is')
    print(str(dummy_race_df))

    # Getting everything together
    transformed_df = df

    # Dropping columns that will not be considered on the model
    transformed_df = transformed_df.drop(columns=['capital-gain', 'capital-loss', 'native-country', 'continent', 'fnlwgt', 'age'])

    # Replacing categorical column 'workclass' with dummy values
    transformed_df = transformed_df.drop(columns=['workclass'])
    transformed_df = transformed_df.join(dummy_workclass_df)

    # Replacing categorical column 'marital-status' with dummy values
    transformed_df = transformed_df.drop(columns=['marital-status'])
    transformed_df = transformed_df.join(dummy_marital_status_df)

    # Replacing categorical column 'occupation' with dummy values
    transformed_df = transformed_df.drop(columns=['occupation'])
    transformed_df = transformed_df.join(dummy_occupation_df)

    # Replacing categorical column 'relationship' with dummy values
    transformed_df = transformed_df.drop(columns=['relationship'])
    transformed_df = transformed_df.join(dummy_relationship_df)

    # Replacing categorical column 'race' with dummy values
    transformed_df = transformed_df.drop(columns=['race'])
    transformed_df = transformed_df.join(dummy_race_df)

    # Replacing categorical column 'sex' with values 1 and 0 using LabelEncoder
    le_sex = preprocessing.LabelEncoder()
    le_sex.fit(transformed_df['sex'])
    list(le_sex.classes_)
    transformed_df['sex'] = le_sex.transform(transformed_df['sex'])

    # Replacing categorical column 'salary' with values 1 and 0 using LabelEncoder
    le_salary = preprocessing.LabelEncoder()
    le_salary.fit(transformed_df['salary'])
    list(le_salary.classes_)
    transformed_df['salary'] = le_salary.transform(transformed_df['salary'])

    print(str(transformed_df))

    # split dataset in features(independent) and target variable(dependent)
    df_independent = transformed_df.drop(columns=['salary']) # Features variables: All columns but salary
    df_dependent = transformed_df['salary'] # Target variable: Column salary

    independent_columns = df_independent.columns.tolist()

    # Creating random training and test sets
    x_train, x_test, y_train, y_test = train_test_split(df_independent, df_dependent, test_size=0.3, random_state=1) # 70% training and 30% test

    # Create Decision Tree classifier object
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=9)

    # Train Decision Tree Classifier
    clf = clf.fit(x_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(x_test)

    dot_data = StringIO()
    export_graphviz(
        clf,
        out_file=dot_data,
        filled=True,
        rounded=True,
        special_characters=True,
        feature_names=independent_columns,
        class_names=['0','1']
    )
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_png('adults.png')
    Image(graph.create_png())

    print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
