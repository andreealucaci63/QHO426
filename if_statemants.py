# the book task
print("What tipe of book is this?")
adventure_book = input()
if adventure_book:
    print("I like adventure book!")
print("Finished reading book")

# calculation task if...else
print("Please enter the activity to be performed.")
calculate = input()
if calculate:
    print("Performing calculation...")
else:
    print("Performing activity...")
print("Activity completed!")

# instruction to a robot if...elife...else
print("Towards which direction should I go (up, down, left or right)?")
up = 1
down = 2
left = 3
right = 4
if up == 1:
    print("up")
elif down <= 1:
    print("down")
elif left >= 1:
    print("left")
else:
    print("right")
print("I'm moving in an upright direction!")

# Modulo operator task
# Prompt the user to enter a number and convert the input to an integer
num = int(input("Enter a number: "))

# Calculate the remainder when the number is divided by 2
reminder = num % 2

# Check if the remainder is greater than 0, indicating an odd number
if reminder > 0:
    # Print a message indicating that the number is odd
    print("This is an odd number.")
else:
    # Print a message indicating that the number is even
    print("This is an even number.")

# Comparison Operators Task
# Prompt the user to enter the first number
num1 = int(input("Please enter the first number."))
# Prompt the user to enter the second number
num2 = int(input("Please enter the second number."))
# Check which number is the smallest.
if num1 < num2:
    print("The first number is the smallest!")
elif num1 > num2:
    print("The second number is the smallest!")
else:
    print("Both are equal!")
