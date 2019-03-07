pattern = ("examine","use","take","combine")

abort = "Wrong input!"
abort2 = "Too many words in input!"
def getInput():
    eingabe = input("insert something")
    inputs = eingabe.split(" ")
    if not inputs[0] in pattern: 
        print(abort)
        if len(inputs) > 3:
            print(abort2)
        return inputs
    
    
def examine():
    print("examine")

def use():
    print("use")

def take():
    print("take")

def combine():
    print("combine")

getInput()