iFact=1

def fact(a):
   global iFact;

   if a>0:
      iFact=int(iFact*a);
      a=a-1;
      fact(a);
    
   return iFact;
 
def main():
 
 s=int(input("enter the number"));
 r=fact(s);
 print("the factorial of number is",r);



if __name__=="__main__":
    main()  