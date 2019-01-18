import random

def getThreeDoors():
    doors = [0,0,0]
    doors[random.randint(0,len(doors) - 1)] = 1
    return doors

def revealAfterChoice(doors, choice):
    for i in range(len(doors)):
        if i is not choice and doors[i] is 0:
            return i

def nonSwopper(doors):
    choice = random.randint(0,2)
    revealed = revealAfterChoice(doors, choice)
    return choice

def swopper(doors):
    choice = random.randint(0,2)
    revealed = revealAfterChoice(doors, choice)
    for i in range(len(doors)):
        if i is not choice and i is not revealed:
            choice = i
            break
    return choice

def playNonSwoper():
    doors = getThreeDoors()
    choice = nonSwopper(doors)
    if doors[choice] is 1:
        return True
    else:
        return False

def playSwoper():
    doors = getThreeDoors()
    choice = swopper(doors)
    if doors[choice] is 1:
        return True
    else:
        return False


def testNonSwopper(rounds):
    wins = 0
    for i in range(rounds):
        didIWin = playNonSwoper()
        if didIWin:
            wins += 1
    return "NonSwopper: " + str(wins) + " wins out of " + str(rounds) + " rounds."

def testSwopper(rounds):
    wins = 0
    for i in range(rounds):
        didIWin = playSwoper()
        if didIWin:
            wins += 1
    return "Swopper: " + str(wins) + " wins out of " + str(rounds) + " rounds."

rounds = 100000
print(testNonSwopper(rounds))
print(testSwopper(rounds))