try :
    with open("noname.txt","r") as fr:
        read = fr.readlines()
        print(read)
except FileNotFoundError :
    print("there are no file")

