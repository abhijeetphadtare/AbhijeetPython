from sys import *
import os
import shutil


def FileCopyExtension(D1,D2,E1):
    flag = os.path.isabs(D1)
    flag1 = os.path.isabs(D2)

    if flag == False:
        D1 = os.path.abspath(D1)

    if flag1 == False:
        D2 = os.path.abspath(D2)

    isDir = os.path.isfile(D2)

    if isDir == True:
        print("Please Enter File Name :")
        exit()

    isDirexits = os.path.exists(D2)

    if isDirexits == False:
        print("Directory is making ")
        os.mkdir(D2)

    srcf = os.listdir(D1)
    print("___________________________________________________")
    for fn in srcf:
        ffn = os.path.join(D1, fn)
        print(ffn)

        if os.path.isfile(ffn):
            if ffn.endswith(E1):
                shutil.copy(ffn, D2)
    print("Files copy sucessfully!!!");
     


def main():
    print("This Script Is Used For Copy files From  One Directory to Another Directory With Specified Extension ")
    if (len(argv) > 4):
        print("Invalid Number Of Arguments ")
        print("Please use -h or -u for help and usage ");
        exit()
    if argv[1].lower() == "-h":
        print("This Script Is Used For Copy files From  One Directory to Another Directory With Specified Extension ");
        print("Example :")
        print("python Filename Folder1 Folder2 Extension")
        print("python DirectoryCopy.py Demo Demo1 .py")
        exit()
    if argv[1].lower() == "-u":
        print("This Script Is Used For Copy files From  One Directory to Another Directory With Specified Extension ")
        exit()

   
    try:
        FileCopyExtension(argv[1], argv[2] ,argv[3])
    except Exception:
        print("Exception Occurred :", Exception)


if __name__ == "__main__":
    main();
