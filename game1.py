
import random

def pcs(comp,mine):
        if(comp==mine):
            return "draw"
        elif(comp=='stone' and mine=='paper'):
            return True
        elif(comp=='paper' and mine=='scissor'):
            return True
        elif(comp=='scissor' and mine=='stone'):
            return True
        else:
            False

            
choice=('stone','paper','scissor')
comp = random.randint(0, 2)
comp = choice[comp]
mine = input('choose either Stone ,Paper or Scissor:')
win = pcs(comp,mine)
print(f"you choose {mine} and the computer choose {comp}")
if win == "draw":
    print("match drawn")
elif win:
    print("you won")
else:
    print("you lose")