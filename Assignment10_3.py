from sys import *
import os
import shutil


def FileCopy(d1 , d2):
    flag = os.path.isabs(d1)
    flag1 = os.path.isabs(d2)

    if flag == False:
        d1 = os.path.abspath(d1)

    if flag1 == False:
        d2 = os.path.abspath(d2)

    isDir = os.path.isfile(d2)

    if isDir == True:
        print("Please Enter File Name :")
        exit()

    isDirexits = os.path.exists(d2)

    if isDirexits == False:
        print("Directory is making ")
        os.mkdir(d2)

    src_files = os.listdir(d1)
    print(src_files)
    for fn in src_files:
        full_file_name = os.path.join(d1, fn)
        print(full_file_name)
        if os.path.isfile(full_file_name):
            #print("Copy file sucessfull!!!");
            shutil.copy(full_file_name, d2)
    print("copy file sucessfull!!!");           

def main():
    print("This Script Is Used For Copy files From  One Directory to Another")

    if (len(argv) > 3):
        print("Invalid Number Of Arguments ")
        print("Please use -h or -u for help and usage ");
        exit()
    if argv[1].lower() == "-h":
        print("This Script Is Used For Copy files From  One Directory to Another ");
        print("Example :")
        print("python Filename Folder1 Folder2")
        print("python DirectoryCopy.py Demo Demo1")
        exit()
    if argv[1].lower() == "-u":
        print("This Script Is Used For Copy files From  One Directory to Another")
        exit()

   

    try:
        FileCopy(argv[1],argv[2])
    except Exception:
        print("Exception Occurred :", Exception)


if __name__ == "__main__":
    main();
