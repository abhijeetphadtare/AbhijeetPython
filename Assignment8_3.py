import threading





def Evenlist(arr):
    isum1=0;
    for i in arr:
        if i%2==0:
           isum1=isum1+i;

    print("the addition of evenlist is ", isum1);                 



def Oddlist(crr):
    isum2=0;
    for i in crr:
        if i%2 !=0:
           isum2=isum2+i;
 
    print("the addition of oddlist is ", isum2);




def main():


    brr=list()
    
    num = int(input("Enter how many of elements  "));
 
    print("Enter numbers in list : ")

    for i in range(0,int(num)):
         no=input("num : ")
        
         brr.append(int(no))

    print("Enterd elements are : ", brr);


    evenlist = threading.Thread(target = Evenlist, args = (brr,));
    
    oddlist = threading.Thread(target = Oddlist, args = (brr,));

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()
    

 



if __name__=="__main__":
   main()           