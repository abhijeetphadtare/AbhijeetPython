def Prime(ino):
    isum=0;
    
    if ino<0:
      ino=-ino;
     
    for i in range(1,ino):
         if ino%i==0:
            isum=isum+i;
         
    if isum==1:
       return True
    else:
       return False
  
print("enter the number")
a=int(input())
bret=Prime(a)
if bret==1:
   print("it is prime number")
else:
   print("it is not prime number")  