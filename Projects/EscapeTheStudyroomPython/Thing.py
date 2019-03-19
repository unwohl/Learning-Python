class Thing:
    def __init__(self,arg1 = "No description available...",arg2 = 0):
        self.description = arg1
        self.ID = arg2 

    def examine(self):
        print(self.description)

    def getID(self):
        return self.ID


    
