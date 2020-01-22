i=1
def pattern2():
    global i 
    if i<=5:
       print(i , end ="  ");
       i=i+1;
       pattern2();


def main():
 
 pattern2()




if __name__== "__main__":
    main()  