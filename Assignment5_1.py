

def pattern1(ino):
    
    if ino>0:
        print("*",end =" ");
        ino=ino-1;
        pattern1(ino)


     
def main():
  x=int(input("enter the no "));
  pattern1(x)


if __name__=="__main__":
     main()      