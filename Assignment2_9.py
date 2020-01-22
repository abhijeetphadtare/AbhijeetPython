def Countdigit(ino):
      icnt=0
      while (ino>0):
         ino = ino // 10
         icnt=icnt+1
      return icnt

print("enter the no")
a=int(input())
iret=Countdigit(a)
print("the no of digit is",iret)
 