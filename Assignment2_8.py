def Pattern3(ino):
   for i in range(1,ino+1):
       for j in range(1,i+1):
            print(j, end = " ")
       print()
            

print("enter the no")
x=int(input())
Pattern3(x)  