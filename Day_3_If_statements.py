# The objective of the game is to show the power of 
# nested if statements.

print("Welcome to Treasure Island.Your mission is to find the treasure")

first =input("Left of Right: ")

if first.lower() == "left":
    second = input("Swim or Wait: ")
    if second.lower() == "wait":
        third = input("Which door?, Red, Blue or Yellow: ")
        if third.lower() == "yellow":
            print("You win")
        else:
            print('Game Over')
    else:
        print("Game Over")
else:
    print("Game Over")