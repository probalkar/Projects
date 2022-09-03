import random
def rps(comp,mine):
    if comp==mine:
        return None
    elif (comp=='r' and mine=='p') or (comp=='p' and mine=='s') or (comp=='s' and mine=='r'):
        return True
    else:
        return False 

choice=('r','p','s')
comp=random.randint(0,2)
comp=choice[comp]
mine=input("Choose between 'r', 'p', 's': ")

win=rps(comp,mine)
print(f"You chose {mine} and computer chose {comp}")

if win is None:
    print("Match drawn")
elif win:
    print("You won")
else:
    print("You lost")
