import threading


def Number(fun,lock):
     fun(lock)

def Printno(lock):
   lock.acquire()
   n=50;
   for i in range(1,n+1):
       print(i);

   print("end of thread1");
   lock.release()


def Reverseno(lock):
    lock.acquire()  
    n=50;
    for i in range(n,0,-1):
        print(i);

    print("end of thread2");
    lock.release()
    




def main():
 
  lock = threading.Lock()

  thread1 = threading.Thread(target=Number, args=(Printno,lock,));
 
  thread2 = threading.Thread(target=Number,args=(Reverseno,lock,));


  thread1.start()
  thread2.start()



if __name__=="__main__":
   main();