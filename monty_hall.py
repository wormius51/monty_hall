import random

def getThreeDoors():
    doors = [0,0,0]
    doors[random.randint(0,len(doors) - 1)] = 1
    return doors

def revealAfterChoice(doors, choice):
    for i in range(len(doors)):
        if i is not choice and doors[i] is 0:
            return i

def nonSwitcher(doors):
    choice = random.randint(0,2)
    revealed = revealAfterChoice(doors, choice)
    return choice

def switcher(doors):
    choice = random.randint(0,2)
    revealed = revealAfterChoice(doors, choice)
    for i in range(len(doors)):
        if i is not choice and i is not revealed:
            choice = i
            break
    return choice

def playNonSwitcher():
    doors = getThreeDoors()
    choice = nonSwitcher(doors)
    if doors[choice] is 1:
        return True
    else:
        return False

def playSwitcher():
    doors = getThreeDoors()
    choice = switcher(doors)
    if doors[choice] is 1:
        return True
    else:
        return False


def testNonSwitcher(rounds):
    wins = 0
    for i in range(rounds):
        didIWin = playNonSwitcher()
        if didIWin:
            wins += 1
    return "Non Switcher: " + str(wins) + " wins out of " + str(rounds) + " rounds."

def testSwitcher(rounds):
    wins = 0
    for i in range(rounds):
        didIWin = playSwitcher()
        if didIWin:
            wins += 1
    return "Switcher: " + str(wins) + " wins out of " + str(rounds) + " rounds."

rounds = 100000
print(testNonSwitcher(rounds))
print(testSwitcher(rounds))
