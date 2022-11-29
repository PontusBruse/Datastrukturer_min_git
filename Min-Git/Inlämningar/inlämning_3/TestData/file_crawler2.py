import os


def file_crawler(start_dirpath, search_word):
    # os.listdir creates a list of all the items in the current directory
    dirs = os.listdir(start_dirpath)

    for file in dirs:
        if file.endswith(".txt"):
            try:  # If it's a textfile we'll search for our "search_word in that file"
                with open(os.path.join(start_dirpath, file), encoding='utf-8') as my_file:
                    content = my_file.read()
                    if search_word in content:
                        print(start_dirpath + file)

            # Only runs if our try-statement above isn't working
            except FileNotFoundError as e:
                print("Error while opening: " + start_dirpath + "/" + file)
                print(e)

        # If the current item we look at is a (sub)folder, we try to make a recursive call on file_crawler()
        elif os.path.isdir(os.path.join(start_dirpath, file)):
            try:
                file_crawler(start_dirpath + "/" + file, search_word)

            # Only runs if our try-statement above isn't working
            except FileNotFoundError as e:
                print("Error while opening: " + start_dirpath + "/" + file)
                print(e)


if __name__ == '__main__':

    search_word = input("Skriv in ditt sökord: ")
    # State your directory where, where you want to start the search (down bellow is an example)
    start_dirpath = "/Users/bruse/Documents/Skola/Datastrukturer och algoritmer/Min-Git/Inlämningar/inlämning_3/TestData"
    file_crawler(start_dirpath, search_word)
