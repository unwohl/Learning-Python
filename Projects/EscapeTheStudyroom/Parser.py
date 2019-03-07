pattern = ("examine","use","take","combine")

abort = "Wrong input!"
abort2 = "Too many words in input!"
def getInput():
    input(":",_input)
    inputs = _input.split(" ")
    if not inputs[0] in pattern 
        print(abort)
        if len(inputs) > 3:
            print(abort2)
        return inputs
    
    
