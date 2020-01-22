from MarvellousNum import *;


def ListPrime():
    def Accept(num):
        arr = list()
        brr = list()
        sum = 0
        print("Enter Numbers in list :")
        for i in range(0, num):
            print("enter number",i+1);
            no = int(input())
            arr.append(no)
            ans = CheckPrime(no)
            if ans == True:
                # print("prime")
                sum += no
                brr.append(no)

        return arr,brr,sum

    num = int(input("Enter number of elements :"))
    arr,brr,sum = Accept(num)
    print("Inserted number in list is :", arr)
    print("prime numbers in list is :", brr)
    print("Addition of Prime Numbers is :", sum)


def main():
    ListPrime()


if __name__ == "__main__":
    main()
