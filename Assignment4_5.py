from functools import *; 
def Acceptdata():
    size=int(input("Enter the no of elements"))
    x=list();
    print("enter the elements in list")
    for i in range(0,size,1):
         print("enter the element",i+1);
         y=int(input());
         x.append(y);
    return x;


def Primeno(x):
    for i in range(2, x + 1):
        if i != x:
            if x % i == 0:
                return False
        else:
            return True


def Mul(no1):
    return no1*2;

def Max(no1,no2):
    return max(no1,no2)





def main():
    rawdata=Acceptdata();
    print("the Rawdata is ");
    print(rawdata);

    filterdata=list(filter(Primeno,rawdata));
    print("the filtered data is ");
    print(filterdata);
   
    Mapdata=list(map(Mul,filterdata));
    print("the modified data is");
    print(Mapdata);
 
    result=reduce(Max,Mapdata);
    print("the final result is");
    print(result);       



if __name__ == "__main__":
    main()















