import os
from sys import *;

def ExtensionSearch(d,e):
     
    flag = os.path.isdir(d)
    if flag == False:
        print("it is not directory ");
        exit()
    
    count = 0;
    for folder , subfolder, files  in os.walk(d):
         print("Current Directory os ",folder);
         for fn in files:
             if fn.endswith(e):
                 count = count + 1;
                 print(fn);
      
    
    if count ==0 :
        print("No such file with extension", e);


def main():
   print("----Developed by Abhijeet phadtare----");
   print("Application name is :" +argv[0]);
   print("This Script used to search specific file extension in directory");
  
   if(len(argv) !=3):
       print("Invalid Number of arguments");
       print("Please use -h or -u for help and usage ");
       exit()
  
   if argv[1] == "-h" or argv[1] == "-H":
         print("This script is used for search directory");
         print("Example");
         print("python Filename DirectoryName Extension");
         print("python Assignment10_1.py Demo .txt ");  
         exit()

   if argv[1] == "-u" or argv[1] == "-U":
         print(" This script is used for search specific file extension in directory");
         exit()
   
 

   try:
         ExtensionSearch(argv[1],argv[2])
    
   except Exception:
         print("Exception Occured",Exception)

if __name__=="__main__":
   main();