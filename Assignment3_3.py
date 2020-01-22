def Minno(ele):
    min=ele[0];
    for i in ele:
       if i<min:
           min=i
    return min; 
     
def main():
   size=int(input("enter the no of elements "))
   a= list();
   print("Insert the Element in list");
   for i in range(0,size,1):
       print("Enter element ",i+1)
       no=int(input());
       a.append(no)
   print("the list is",a);
   iret=Minno(a);
   print(" the  minimum element in list is",iret);     
   
if __name__== "__main__":
    main()

           