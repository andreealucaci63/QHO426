# the book task
print("What tipe of book is this?")
adventure_book = input()
if adventure_book:
    print("I like adventure book!")
print("Finished reading book")

# calculation task if...else
print("Please enter the activity to be performed.")
calculate =input()
if calculate:
    print("Performing calculation...")
else:
    print("Performing activity...")
print("Activity compleated!")

# instruction to a robot if...elife...else
print("Towards which direction should I go (up, down, left or right)?")
up= 1
down= 2
left= 3
right= 4
if up == 1:
    print("up")
elif down <= 1:
    print("down")
elif left >= 1:
    print("left")
else:
    print("right")
print("I'm moving in an upright direction!")