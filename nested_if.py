
# Nested example explained.
# Ask the user what to do
print(" What should I do (recover/study)?")
activity = input()
# Decide if user should recover or study.
if activity == "recover":
    # ask user how they want to recover
    print("How would you like to recover (sleep/socialise)?")
    recover_by = input()
    # decide if user should sleep or socialise
    if recover_by == "sleep":
        print("zzzZZZzzz")
    else:
        print("I will text my friends!")
else:
    print("I will study")

# Nested task.
# Ask user to enter the cover type (hard or soft) of the book.
print("Please enter the cover type (hard or soft) of the book.")
book = input()
if book == "soft":
    print(" Is the book perfect bound?")
    soft = input()
    if soft == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books.")
else:
    print("Books with hard covers can be more expensive!")

