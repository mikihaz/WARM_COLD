# for random integer numbers
import random
# to clear the screen
from os import system, name


# define our clear function
def clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


dif1 = 0
# to count turns
turns = 0
num = random.randint(1, 100)
guess = int(input("Enter Any Number in Between 1 to 100 >> "))
dif = abs(num - guess)
if dif <= 10:
    print("     << WARM >>")
elif (guess <= 1 and guess >= 100):
    print("<< OUT OF THE BOX >>")
else:
    print("     << COLD >>")
dif1 = dif
while (guess >= 1 and guess <= 100):
    turns += 1
    guess = int(input("Enter Any Number in Between 1 to 100 >> "))
    clear()
    dif = abs(num - guess)
    if guess == num:
        print("     << SUCCESS >>")
        print("<< YOU TOOK ", turns + 1, " TURNS TO GUESS >>")
        break
    elif dif <= dif1:
        print("     << WARMER >>")
    else:
        print("     << COLDER >>")
    dif1 = dif
else:
    print("<< OUT OF THE BOX >>")
