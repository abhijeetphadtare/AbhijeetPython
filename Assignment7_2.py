class  BankAccount:

     ROI=10.5;
    
     def __init__(self,name,val):
         self.Name=name;
         self.Balance=val;
         
         print(" Hello!!! Welcome to the Deposit & Withdrawal System");
         #print("The user name is :",self.Name);
         #print("the user balance is:",self.Balance); 
   
     def Display(self):
         print("The user name is :" ,self.Name);
         print("The user total balabce is :",self.Balance);      
        
     def Deposit(self):
          Amount = float(input(" enter amount to be deposited :"));
          self.Balance=self.Balance+Amount;
          print("The balance after dopositing amount is : ",self.Balance);
             
     def Withdraw(self):
          Amount = float(input(" enter amount to be withdrawn: "));
             
          if self.Balance>=Amount:
             
              self.Balance=self.Balance-Amount;
              print("The   balance after withdrawing is :",self.Balance); 
               
          else:
              print(" Insufficien balance ");   
                     
          

     def CalculateIntrest(self):
           
           interest=self.Balance/BankAccount.ROI
           print("the interest is :",interest);
 


def main():

       a=input("Enter the user name :");
       b=float(input("enter the user balance :"));
      

       obj1 = BankAccount(a,b)
       

       obj1.Deposit();
       obj1.Withdraw();
       obj1.Display();
       obj1.CalculateIntrest();
       
       i=input("Enter the user name : ");
       j=float(input("Enter the user balance : "));
  
       obj2 = BankAccount(i,j) 

  
       obj2.Deposit();
       obj2.Withdraw();
       obj2.Display();
       obj2.CalculateIntrest();


 
        
if __name__=="__main__":
   main()






  