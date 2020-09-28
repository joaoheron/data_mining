def replace_characters(replaced, replace, basepath='download/'): # , filename='adult.data'
    for filename in os.listdir(basepath):
        if '.gitignore' in filename:
            continue 
        with open(basepath + filename, 'r') as infile, open(write_file, 'w') as outfile:
            for line in infile:
                outfile.write(str(line).replace(replaced, replace))
            infile.close()
            outfile.close()
            # substitui o arquivo antigo pelo novo arquivo e renomeia
            os.remove(basepath + filename)
            os.rename(write_file, final_path + filename)

def delete_line(bad_words=["?"], basepath='download/'): # , filename='adult.data'
    for filename in os.listdir(basepath):
        if '.gitignore' in filename:
            continue 
        with open(basepath + filename, 'r') as infile, open(write_file, 'w') as outfile:
            for line in infile:
                if not any(bad_word in line for bad_word in bad_words):
                    outfile.write(line)
            infile.close()
            outfile.close()
            os.remove(basepath + filename)
            os.rename(write_file, final_path + filename)
