 import os
from sys import*;
import time;
import MarvellousChecksum;

def DuplicateFilesRemove(Directoryname):
     
    if not os.path.exists(Directoryname):
          os.mkdir(Directoryname);
     
    dups = {}
    filename = os.path.join(Directoryname, "Log.txt") 
    fobj = open(filename,"w")
    for Folder,SubFolders,Files in os.walk(Directoryname):
         print(Folder)
         for file in Files:
            path = os.path.join(Folder,file)
            path1 = MarvellousChecksum.hashfile(path)	
            if path1 in dups :
                 dups[path1].append(path)
                 fobj.write(file)
            else:
                 dups[path1]= [path]

    fobj.close()
    
    data = [];
    count = 0;

    data = list(filter(lambda z : len(z)>1, dups.values()));
  
    for i in data:
        icnt= 0;
        for j in i:
           icnt+=1;
           if icnt>=2:
              count +=1;
              print("Delete",j);
              os.remove(j);
              print("Total file deleted", count);
         
       
def main():
    print("This Script Is Used For Find The Duplicates File from The Directory ")
    if (len(argv) > 2):
        print("Invalid Number Of Arguments ")
        print("Please use -h or -u for help and usage ");
        exit()
    if argv[1].lower() == "-h":
        print("This Script Is Used For Find The Duplicates File from The Directory");
        print("Example :")
        print("python Filename Folder1")
        print("python DirectoryDuplicate.py Demo ")
        print("DirectoryDuplicate.py : Name Of The file")
        print("Demo : Name of the Folder ")
        exit()
    if argv[1].lower() == "-u":
        print("This Script Is Used For Find The Duplicates File from The Directory")
        exit()

    Directoryname = argv[1];
    try:

        DuplicateFilesRemove(argv[1])
        
    except Exception as er:
        print("Exception Occurred :",er)

if __name__ == "__main__":
    main();