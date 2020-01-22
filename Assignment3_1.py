
def Add(mylist):
       total=0;
       for i in mylist:
          total=total+i
       return total
       
     

def main():
  
  size = int(input("Enter number of elements"));    
  arr= list();     
  print("Enter the elements");    
  for i in range(0,size,1):        
       print("Enter number",i + 1)        
       no = int(input());        
       arr.append(no);
   
  print(arr);   
  iret=Add(arr)
  print(iret)
if __name__ == "__main__":
   main()    
   
