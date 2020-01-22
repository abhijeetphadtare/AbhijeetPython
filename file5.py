from sys import*;



def Frequency(f1,f2):
    
     file1 = open(f1,"r");
     str1 = str(f2);
     count = 0;
     for line1 in file1:
         word = line1.split()
         for s in word:
             if s == str1 :
                 count = count + 1;
             else:
                 print("String ",str1,"is incorrect");
     print("Frequency of ",str1 ,"is : ",count)
     file1.close()


def main():
    print("----Count Frequency of string in file----");
    print("Application Name is : "+argv[0]);

    if (len(argv) < 3):
 
          print("Invalid number of arguments ");
    
   
    try:   
        Frequency(argv[1],argv[2])
   
    except Exception:
        print("Error : Invalid input");
  

if __name__=="__main__":
   main();




           





