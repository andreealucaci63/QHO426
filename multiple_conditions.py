
# Multiple conditions task 1
# Asking the user to enter the type of adventure.
print("Please enter the type of adventure(scary or short)")
adventure = input()
#identify the adventure
if (adventure == "scary") or (adventure == "short"):
    print("Entering the dark forest!")
else :
    print("Not sure which route to take.")

print("Please enter the type of adventure(safe or long)")
adventure= input()
if (adventure == "safe") or (adventure == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")