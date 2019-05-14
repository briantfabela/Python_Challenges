def collatz(number):
    if number % 2 == 0: # if number is even
        print(number // 2)
        return number // 2
    else: # if number is odd
        print(3 * number + 1)
        return 3*number+1

def main():
    
    try:
        num = int(input("Enter Number: ")) # convert input as int and store it in 'num' var
        num = collatz(num)
        
        while num != 1:
            num = collatz(num)

    except ValueError:
        print("Please enter a valid integer")
        main()

if __name__ == "__main__":
    main()