def fact(n):
 
    f = 1;
    if n<0:
      
        n=-n 
    
    for i in range(1,n+1):
        f = f*i
   
    return f

print("enter the no")

x=int(input())

result=fact(x)

print(result)