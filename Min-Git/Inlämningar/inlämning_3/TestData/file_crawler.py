import os

search_word = input("Skriv in ditt sökord: ")

for dirpath, dirs, files in os.walk("/Users/bruse/Documents/Skola/Datastrukturer och algoritmer/Min-Git/Inlämningar/inlämning_3/TestData"):
    print(dirpath)
    print(dirs)
    print(files)
    for filename in files:
        fname = os.path.join(dirpath, filename)
        with open(fname, encoding='utf-8') as myfile:
            content = myfile.read()
            if search_word in content:
                print(os.path.join(dirpath, filename))



if __name__ == '__main__':
    pass