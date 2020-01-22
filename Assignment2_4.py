def Factor(ino):
   isum=0 
   if ino<0:
      
      ino=-ino
   
   for i in range(1,ino):
         if ino%i==0:
            isum=isum+i
       
   return isum


print("enter the no")
x=int(input())
iret=Factor(x)
print("the addition of factors is",iret)   
 