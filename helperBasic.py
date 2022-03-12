import random

def Helper():
    returnVal = ""
    returnVal += "FUNCTION\n"
    returnVal += "\t Helper()\n"
    returnVal += "\t Roll(a, b)\n"
    returnVal += "\t RollFull(a, b, c)\n"
    returnVal += "\t RandomList(List)\n"
    returnVal += "\t RandomWeightedList(List)\n"
    returnVal += "\t Pisagor(List)\n"
    return returnVal

def Roll(a, b):
    Sum = 0
    for x in range(0,int(a)):
        Sum = Sum + random.randint(1,int(b))
    return Sum

def RollFull(a, b, c):
    return (Roll(a,b)+int(c))
    

def RollList(List):
    Sum = 0
    for x in range(0,len(List)):
        if ('d' in List[x]):
            Sum = Sum + Roll((List[x].split('d')[0]),(List[x].split('d')[1]))
        else:
            Sum = Sum + int(List[x])
    return Sum

def RandomList(List):
    return List[Roll(1, len(List)) - 1]

def RandomWeightedList(List):
    totalWeight = 0
    length = len(List)
    for entry in List:
        totalWeight = totalWeight + entry[0]
    roll = Roll(1, totalWeight)
    for x in range(0, length):
        roll = roll - List[x][0]
        if(roll <= 0):
            return List[x][1:]

def Pisagor(List):
    Sum = 0;
    for x in range(0,len(List)):
        Sum = Sum + (int(List[x])*int(List[x]))
    ret = 0
    while(True):
        if(ret<Sum):
            ret= ret + 1
        else:
            return ret
