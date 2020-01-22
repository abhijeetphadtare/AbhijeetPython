
import threading






def Small(value):
    icnt=0;
    for i in value:
        if (i.islower()):
            icnt=icnt+1;

    print("the number of small digit is", icnt);



def Capital(value):
    icnt=0;
    for i in value:
         if (i.isupper()):
             icnt=icnt+1;

    print("the number of capital digit is", icnt);


def Digit(value):
    icnt=0;
    for i in value:
          if (i.isdigit()):
              icnt=icnt+1;
    
    print("the number of digit is",icnt);



def main():

  a=input("enter the string:  ");
 
    
  small = threading.Thread(target = Small , args=(a,))
 
  capital = threading.Thread(target = Capital , args =(a,))

  digit = threading.Thread(target = Digit , args =(a,))

  small.start()
  capital.start()
  digit.start()
 
  



if __name__=="__main__":
   main()     