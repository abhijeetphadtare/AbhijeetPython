def Sumdigit(n):
    iDigit=0
    iSum=0

    if n<0:
      n=-n
    while(n>0):
        iDigit=int(n % 10)
        iSum=iSum+iDigit
        n=n/10
    
    return iSum


print("enter the number")
x=int(input())
z=Sumdigit(x)
print("the addition of digit is",z)