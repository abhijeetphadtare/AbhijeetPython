def Maxno(ele):
    max=ele[0];
    for i in ele:
       if i>max:
           max=i
    return max; 
     
def main():
   size=int(input("enter the no of elements"))
   a= list();
   print("Insert the Element in list");
   for i in range(0,size,1):
       print("Enter element ",i+1)
       no=int(input());
       a.append(no)
   print(a);
   iret=Maxno(a);
   print(" the maximum element is",iret);     
   
if __name__== "__main__":
    main()

           