pattern = ("examine","use","take","combine")

abort = "Wrong input!"
abort2 = "Too many words in input!"
def getInput():
    _input = input(":")
    inputs = _input.split(" ")
    print(inputs)
    if not inputs[0] in pattern:
        print(abort)
        if len(inputs) > 3 or len(inputs) < 2:
            print(abort2)
        return
    return inputs
    
getInput()
