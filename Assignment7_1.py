class BookStore:
 
    NoOfBooks=0;
  
    def __init__(self,a,b):
       self.Name = a;
       self.Author = b;
       BookStore.NoOfBooks=BookStore.NoOfBooks+1;

    def Display(self):
        print("Bookname:",self.Name);
        print("Authorname:",self.Author);
        print("Noofbook:",BookStore.NoOfBooks);
     
        

def main():

  Obj1 = BookStore("Linux System Programming", "Robert Love");
  Obj1.Display() 

  Obj2 = BookStore("C Programming","Dennis Ritchie");
  Obj2.Display()



  


if __name__=="__main__":
    main()


    