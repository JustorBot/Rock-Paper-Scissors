import random

#User Input for Game
print("1)Rock\n2)Paper\n3)Scissors")
rps = None

while True:
    rps = input("Pick 1, 2 or 3: ")
    try:
        rps = int(rps)
        if rps not in (1, 2, 3):
            print("Only numbers 1, 2 or 3 are allowed.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

#Ai inputs
rockAI = 1
paperAI = 2
scissorsAI = 3
rpsAI = [rockAI, paperAI, scissorsAI]

#Ai Choice of input handler
rpsAIChoice = random.choice(rpsAI)

#Players int value to string of game choice
if rps == 1:
    print("You choose Rock")
elif rps == 2:
    print("You choose Paper")
elif rps == 3:
    print("You choose Scissors")

#AIs int value to string of game choice
if rpsAIChoice == 1:
    print("AI choose Rock")
elif rpsAIChoice == 2:
    print("AI choose Paper")
elif rpsAIChoice == 3:
    print("AI choose Scissors")

#Game win and lose outcomes
if rps == rpsAIChoice:
    print("Draw")
elif rps == 1 and rpsAIChoice == 2:
    print("Lose")
elif rps == 1 and rpsAIChoice == 3:
    print("Win")
elif rps == 2 and rpsAIChoice == 1:
    print("Won")
elif rps == 2 and rpsAIChoice == 3:
    print("Lose")
elif rps == 3 and rpsAIChoice == 1:
    print("Lose")
elif rps == 3 and rpsAIChoice == 2:
    print("Won") 