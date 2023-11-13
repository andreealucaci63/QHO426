
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

# Multiple nested decisions task.
# You are looking for your phone... It was literally in your hand a second ago!
# Ask the user were to look.
print("Where should I look?")
phone = input()

if phone == "in the bedroom":
    print("Where in the bedroom should I look?")
    in_the_bedroom = input()
    if in_the_bedroom == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")

if phone == "in the bathroom":
    print("Where in the bathroom should I look?")
    in_the_bathroom = input()
    if in_the_bathroom == " in the bathtub":
        print("Found a rubber duck but no phone.")
    else:
        print("Found bathroom stuff but no phone.")

if phone == "in the living room":
    print("Where in the living room should I look?")
    in_the_living_room = input()
    if in_the_living_room == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")

else:
    print("I do not know where that is but I will keep looking.")