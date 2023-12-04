def dieRollSimulation():
    import random
    randNum = random.randrange(1, 7)
    return randNum


def callDieRoll(numberOfRolls):
    rollCounter = 0
    doubleCounter = 0
    while True:
        die1 = dieRollSimulation()
        die2 = dieRollSimulation()
        if die1 == die2:
            doubleCounter += 1
        rollCounter += 1
        if rollCounter == numberOfRolls:
            break
    prob = (doubleCounter/numberOfRolls) * 100
    return prob
    
print(callDieRoll(10000000))
