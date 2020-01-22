
class Demo():
     value=10;
                  
     def __init__(self,x,y):        
       self.no1 = x        
       self.no2 = y
       
     def Fun(self):
       print("inside instance fun");
       print(self.no1) 
       print(self.no2) 

     def Gun(self):
       print("inside instance gun");       
       print(self.no1)
       print(self.no2) 
  


def main():
    
    print("inside main")
 
    obj1 = Demo(11,21);
    obj2 = Demo(51,101);   
 
    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()
    
if __name__=="__main__":
    main()



 