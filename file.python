from sys import *
import os


def Filecheck(Filename):
    flag = os.path.exists(Filename);
    if flag:
        print("File Exits ")
    else:
        print("File Does Not Exits")
        exit()


def main():
    if len(argv) < 2:
        print("Invalid Number Of Argument ")
        print("Example :")
        print("python Assignment9_1.py FileName");
        exit()
    FileName = argv[1];
    try:
        Filecheck(FileName);
    except Exception:
        print("Exception Occurred :", Exception)


# print(FileName);


if __name__ == "__main__":
    main();
