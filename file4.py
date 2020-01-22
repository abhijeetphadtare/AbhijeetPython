import os
from sys import*

def Filecompare(f1,f2):
  
  x=open(f1,"r")
  y=open(f2,"r")
  flag = False
  for line1 in x:
      for line2 in y:
          if line1==line2:
              pass
          else:
              print("Failure : File contents are not same");
              flag = True
          break
  if flag == False:
       print("Sucess : File Contents are same")
        
  x.close();
  y.close();




def main():
       print("Comparing two files");
       print("Application name is:"+argv[0])

       if(len(argv) != 3):
         print("Error : Invalid number of arguments");
         print("Example : ")
         print("python Assignment9_4.py FileName1 FileName2");
         print("FileName1 : Name of the first file");
         print("FileName2 : Name of the second file");
                  
       try:
            Filecompare(argv[1],argv[2])
     
       except Exception:
            print("Error: Invalid input");
       

if __name__=="__main__":
   main();
