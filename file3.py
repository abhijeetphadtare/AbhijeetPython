from sys import *
import os


def Filecopy(f1,f2):
  
    fread = open(f1,"r");
    fwrite = open(f2,"w");
 
    fwrite.write(fread.read());
    fread.close();
    fwrite.close();  
      
 



def main():
  
 print("----Developed by Abhijeet Phadtare----");
 print("Application name : "+argv[0]);
 if len(argv)<3: 
      print("Invalid no of argument");
      print("Example:");
      print("python Assignment9_3.py Filename1 filename2");
      print("Filename1 : Name of the file");
      print("Filename2 : Name of the file to copy first file contents");
      exit()
 try:
    Filecopy(argv[1],argv[2])
 
 except Exception: 
     print("Error: Invalid input");
  
if __name__=="__main__":
   main();
