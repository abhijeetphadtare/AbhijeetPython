import threading




def Factor(fun,no1,lock):
     fun(no1,lock)



def Evenfactor(value,lock):
      
      lock.acquire()
      isum=0;
      for i in range(1,value):
           if (value % i ==0)&(i%2==0):
               print(i)
               isum=isum+i;
      
      print("The addition of even factor is : ", isum)
      lock.release()


def Oddfactor(value1,lock):
       
       lock.acquire()
       isum=0;
       for i in range(1,value1):
            if (value1 % i ==0)&(i%2!=0):
                  print(i)
                  isum=isum+i; 

       print("The addition of odd factor is : ", isum)   
       lock.release()

             
               
def main():

   x=int(input("Enter the number  "));
   
   lock = threading.Lock()
 
   evenfactor = threading.Thread(target=Factor, args=(Evenfactor,x,lock))
   
   oddfactor = threading.Thread(target=Factor, args=(Oddfactor,x,lock))

   evenfactor.start()
   oddfactor.start()

  
   evenfactor.join()
   oddfactor.join() 
   
   print("exit from main"); 



if __name__=="__main__":
    main();   