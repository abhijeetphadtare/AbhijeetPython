import os



def FileOpen(input):
    f2 = open(input)

    file_contents=f2.read()

    print(file_contents);


def main():

 f1=input("Enter the file name to be opened  ");
 
 FileOpen(f1)






if __name__=="__main__":
   main();
