isum=0;
def Digitadd(x):
    global isum;
     
    if(x!=0):
       isum=isum+(int(x%10));
       x=x/10;
       Digitadd(x);
      
    return isum;


def main():
  
  z=int(input("enter the no"));
  iret=Digitadd(z);
  print("the addition of digit is ",iret);



if __name__=="__main__":
    main() 