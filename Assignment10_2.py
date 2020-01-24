import os
from sys import *

def RenameExtension(d,e1,e2):
   
   flag = os.path.isabs(d)
   if flag == False:
      d = os.path.abspath(d)
   
   flag = os.path.isdir(d);
   
   if flag == False:
       print(" it is not Directory") ;
       exit()
   
  
   count = 0;
   print(d);
   print("------------------------------------------------------------");
   for foldername,subfolder, filename in os.walk(d):
         print("---------------------------------------------");
         print("Current Directory is " ,foldername);
         print("----------------------------------------------");
         for fn in filename:
              print(fn); 
              file1,ext = os.path.splitext(fn)
              print(file1)
              print("--------------------------------------");
              print(os.path.abspath(fn));
              print("-------------------------------------------");
              full_file = os.path.join(foldername, fn)
              print("full file name is ::",full_file);
              if ext == e1:
                  count = count+1;
                  print("No of same extensin is",count);
                  os.rename(full_file,file1+e2)
                  print("----The rename file extension sucessfull !!!---");
    
        
        
                       
   if count == 0:
      print("There is no file with ",e1);       

def main(): 
  
   print("Application Name is" +argv[0]);
     
   if (len(argv) !=4):
        print("Invalid number of arguments");
 
   if argv[1] == "-h" or argv[1] == "-H ":
      print("This script is helps to rename the file extension in directory");
      exit()
 
   if argv[1] == "-u" or argv[1] == "-U":
      print("This script is used to change extension of file");
      print(" For Demo : ");
      print("Python Filename Directoryname FirstExtension SecondExtension ");
      print("Usage: DirectoryRename.py Demo .txt .doc ");
      exit()
       
   try:
      RenameExtension(argv[1],argv[2],argv[3])
  
   except Exception:
      print("Exception occurred: ",Exception);


if __name__=="__main__":
   main();
