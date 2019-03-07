from Useable_Thing import Useable_Thing

class Takeable_Thing(Useable_Thing):
    def __init__(self,arg1,arg2,arg3,arg4):
        Useable_Thing.__init__(self,arg1,arg2,arg3)
        self.take_msg = arg4
        
    def take(self):
        return
