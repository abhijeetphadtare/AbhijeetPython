
from functools import *;
def Acceptlist():
    size=int(input("enter the no of element"))
    ab=list();
    print("enter the number in list  ");
    for i in range(0,size,1):
        print("enter number", i+1);
        n=int(input())
        ab.append(n)

    return ab;


def grtles(no):
    if ((no>=70)&(no<=90)):
       return no;

def modify(no):
    return no+10;

def product(no1,no2):
    return no1*no2;



def main():
 iret=Acceptlist();
 print("accepted list is");
 print(iret);

 FilterList= list(filter(grtles,iret));
 print("filter list is");
 print(FilterList);

 ModifiedList = list(map(modify,FilterList));
 print("modified list is");
 print(ModifiedList);
 
 result = reduce(product,ModifiedList);

 print("final result is",result);


if __name__ == "__main__":
    main()
  

     