class Circle:
 
   PI=3.14;
 
   def __init__(self):
        self.Radius=0.0;
        self.Area=0.0;
        self.Circumference=0.0;
         
    
   def Accept(self):
         self.Radius=int(input("enter the radius")); 
      
   def CalculateArea(self):
               
         self.Area = Circle.PI*self.Radius*self.Radius;

   def CalculateCircumference(self):
         self.Circumference = 2*Circle.PI*self.Radius;
 
   def Display(self):
       print("Radius of cirlce is",self.Radius);
       print("Area of cirlce is",self.Area);
       print("Circumference of circle is",self.Circumference);




def main():

  obj1 = Circle()
  obj2 = Circle() 
  obj3 = Circle()


  obj1.Accept()     
  obj1.CalculateArea()
  obj1.CalculateCircumference()
  obj1.Display()

  obj2.Accept()     
  obj2.CalculateArea()
  obj2.CalculateCircumference()
  obj2.Display()

  obj3.Accept()     
  obj3.CalculateArea()
  obj3.CalculateCircumference()
  obj3.Display()



if __name__=="__main__":
     main()      