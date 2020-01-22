from functools import *; 
def Acceptdata():
   size=int(input("enter the no of elements"));
   arr=list();
   print("enter the element in list");
   for i in range(0,size,1):
       print("enter element ",i+1);
       a=int(input())
       arr.append(a)
   return arr;

 
def Evenno(no1):
    return (no1%2==0);


def Square(no1):
    return no1*no1;
 
def Add(no1,no2):
    return no1+no2;

def main():
   iret=Acceptdata();
   print("the Accepted data is");
   print(iret);
  
    
   Filterdata=list(filter(Evenno,iret))
   print("the filterd data is ");
   print(Filterdata);

   Mapdata=list(map(Square,Filterdata))
   print("the map data is");
   print(Mapdata);
 
   result = reduce(Add,Mapdata);
   print("the final result is");
   print(result);
 

if __name__ == "__main__":
     main()
 
