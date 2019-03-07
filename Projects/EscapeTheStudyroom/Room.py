from Thing import Thing

class Room:
    def __init__(self,des = "This Room is Empty",name = "Empty Room"):
        self.description = des
        self.name = name

    def examine(self):
        print(self.description)

    def enter(self):
        print("You just entered "+self.name+"\n"+self.description)
