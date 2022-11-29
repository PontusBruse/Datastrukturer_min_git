import os


def file_crawler(start_dirpath, search_word):
    with start_dirpath as dirs:

        for file in dirs:
            # print(file.name)

            if file.is_file():
                try:

                    with open(file, encoding='utf-8') as my_file:
                        content = my_file.read()
                        if search_word in content:
                            print(os.path.abspath(file.name))
                except FileNotFoundError:
                    print("Error while opening: " + start_dirpath + "/" + file)

            elif file.is_dir():
                print(file.name)
                file_crawler(os.path.abspath(file.name), search_word)




if __name__ == '__main__':
    search_word = input("Skriv in ditt sökord: ")
    start_dirpath = os.scandir()
    file_crawler(start_dirpath, search_word)