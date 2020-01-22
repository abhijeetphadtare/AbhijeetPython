def Add(ino1,ino2):
   ians=ino1+ino2
   return ians

      
print("enter first number")
a=int(input())
print("enter second number")
b=int(input())

iret=Add(a,b)

print("the addition of two number is",iret)