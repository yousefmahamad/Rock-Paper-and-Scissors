import random

#Main DEV : Yousef Mohamad

def game_win(comp, you):
    if comp == you:
        return None

    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False

    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False

    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False


print("Comp's Turn: Rock(r) Paper(p) or Scissors(s)?")
Comp_Input = random.randint(1, 3)
if Comp_Input == 1:
    comp = 'r'
elif Comp_Input == 2:
    comp = 'p'
elif Comp_Input == 3:
    comp = 's'

name = input("Enter your Name: ")
you = input(f"{name}'s Turn: Rock(r) Paper(p) or Scissors(s)?")
x = game_win(comp, you)

print(f"Computer chose : {comp}")
print(f"{name} chose : {you}")

if x == None:
    print("The Game is a Tie!!")
elif x:
    print(f"Congratulations!!! {name} Won The Game")
else:
    print(f"{name} Lost The Game!!!")

print("Thankyou!!! for playing our game")
