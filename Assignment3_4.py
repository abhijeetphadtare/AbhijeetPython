def Freqno(arr,x):
     icnt=0;
     for i in arr:
         if i==x:
            icnt=icnt+1;
     return icnt     
          
def main():
   size=int(input("enter the no of elements  "))
   a= list(); 
   print("Insert the numbers in list ");
   for i in range(0,size,1):
       print("Enter element ",i+1)
       no=int(input());
       a.append(no)
   print(a);
   b=int(input("enter the searching number "))  
   iret=Freqno(a,b);
   print(" the  frequency of number is",iret);     
   
if __name__== "__main__":
    main()

           