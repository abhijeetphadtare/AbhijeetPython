class Arithmatic:
      
 
     def __init__(self):
        self.Value1=0;
        self.Value2=0;
       
     
     def Accept(self):
         self.Value1=int(input("enter first value"));
         self.Value2=int(input("enter second value"));
     
     def Addition(self):
          Value3 = self.Value1+self.Value2
          return Value3 ;
 
     def Substraction(self):
          Value3 = self.Value1-self.Value2
          return Value3;
   
     def Multiplication(self):
         Value3 = self.Value1*self.Value2
         return Value3;
 
     def Division(self):
         Value3 = int(self.Value1/self.Value2)    
         return Value3;                      


def main():
 
  obj1 = Arithmatic();
  obj2 = Arithmatic();
  obj3 = Arithmatic();    
  
  obj1.Accept()
  result=obj1.Addition();
  print("the addition is",result);
  
  result=obj1.Substraction();
  print("the substraction is",result);

  result=obj1.Multiplication();
  print("the multiplication is",result);

  result=obj1.Division();
  print("the division is ",result);

      
  obj2.Accept()
  result=obj2.Addition();
  print("the addition is",result);
  
  result=obj2.Substraction();
  print("the substraction is",result);

  result=obj2.Multiplication();
  print("the multiplication is",result);

  result=obj2.Division();
  print("the division is ",result);

  obj3.Accept()
  result=obj3.Addition();
  print("the addition is",result);
  
  result=obj3.Substraction();
  print("the substraction is",result);

  result=obj3.Multiplication();
  print("the multiplication is",result);

  result=obj3.Division();
  print("the division is ",result);


if __name__=="__main__":
    main()

