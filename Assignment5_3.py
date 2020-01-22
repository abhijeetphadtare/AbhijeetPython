i=5

def pattern3():
    global i
    if i>0:
       print(i , end ="  ")
       i=i-1;
       pattern3();
         
 
def main():
 
 pattern3();



if __name__=="__main__":
   main()     