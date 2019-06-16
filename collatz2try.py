def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return (3 * number + 1)  

while True:
    try:
        num = int(input("Enter number: "))
        break
    except:
        print("Wrong! That was not a valid number. Please try again")
collatz(num)

