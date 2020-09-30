import os
from data_mining.vars import (
    download,
    adult_data,
    adult_test,
    adult_data_test,
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
            outfile.write(line.replace('\n', '') + ', ' + get_continent(str(line)) + '\n')
        infile.close()
        outfile.close()
        os.remove(basepath + filename)
        os.rename(basepath + 'outfile', basepath + filename)

def delete_lines(bad_word='?', basepath=download, filename=adult_data_test):
    with open(basepath + filename, 'r') as infile, open(basepath + 'outfile', 'w') as outfile:
        for line in infile:
            # Verificando tambem se a linha nao está vazia (tem algumas linhas vazias no source file)
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
    country = line.split(', ', 14)[13]
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
