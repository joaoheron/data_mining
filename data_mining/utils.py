import os
from data_mining.vars import (
    download,
    adult_data,
    adult_test,
    adult_data_test
)

def apply_lower_case(basepath=download, filename=adult_data_test):
    with open(basepath + filename, 'r') as infile, open(basepath + 'outfile', 'w') as outfile:
        for line in infile:
            outfile.write(str(line).lower())
        infile.close()
        outfile.close()
        os.remove(basepath + filename)
        os.rename(basepath + 'outfile', basepath + filename)

def replace_characters(replaced, replace, basepath=download, filename=adult_data_test):
    # for filename in os.listdir(basepath):
    #     if '.gitignore' in filename:
    #         continue 
    with open(basepath + filename, 'r') as infile, open(basepath + 'outfile', 'w') as outfile:
        for line in infile:
            outfile.write(str(line).replace(replaced, replace))
        infile.close()
        outfile.close()
        os.remove(basepath + filename)
        os.rename(basepath + 'outfile', basepath + filename)

def delete_lines(bad_words=["?"], basepath=download, filename=adult_data_test):
    with open(basepath + filename, 'r') as infile, open(basepath + 'outfile', 'w') as outfile:
        for line in infile:
            if not any(bad_word in line for bad_word in bad_words):
                outfile.write(line)
        infile.close()
        outfile.close()
        os.remove(basepath + filename)
        os.rename(basepath + 'outfile', basepath + filename)

def append_files(output_file=adult_data_test, input_filenames=[adult_data, adult_test], basepath=download):
    with open(basepath + output_file, 'w') as outfile:
        for fname in input_filenames:
            with open(basepath + fname) as infile:
                for line in infile:
                    outfile.write(line)
        outfile.close()
