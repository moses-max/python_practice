def collatz(number):
    try:
        if number % 2 == 0:
            return number // 2
        elif number % 2 == 1:
            return (3 * number + 1)
    except:
       print("Wrong! That was not a valid number. Please try again")

num = int(input("Enter number: "))
while num != 1:
   
    break

collatz(num)

