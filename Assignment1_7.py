def Num3(ino):
   if ino<0:
      ino=-ino
   if ino%5==0:
       return True
   else:
       return False


print("enter the number");
x=int(input())
iret=Num3(x)
print(iret)  