import threading
import os

def Evenodd(no,fun,lock):
    print("the parent id of Evenodd is",os.getppid())
    print("the process id of Evenodd is", os.getpid())
    fun(no,lock)
    
  
 
 
def Even(no1,lock):
   print("the parent of Even id is",os.getppid())
   print("the process of Even id is ", os.getpid())
   lock.acquire()
   for i in range(no1):
      if i%2==0:
        print(i);
   lock.release()



def Odd(no2,lock):
   print("the parent  id  of Odd is",os.getppid())
   print("the process id of Odd is",os.getpid())
   lock.acquire()   
   for i in range(no2):
        if i%2!=0:
          print(i);
   lock.release()


def main():

  value1=20; 
   
  lock = threading.Lock()
  
  even = threading.Thread(target=Evenodd,args=(value1,Even,lock,)) 

  odd = threading.Thread(target=Evenodd,args=(value1,Odd,lock,))

 
  even.start()
  odd.start() 

  even.join()
  odd.join()

  print("parent id is",os.getppid())
  print("process id is", os.getpid())

if __name__=="__main__":
   main();