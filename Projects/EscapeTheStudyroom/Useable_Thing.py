from Thing import Thing

class Useable_Thing(Thing):
    def __init__(self,arg1,arg2,arg3):
        Thing.__init__(self,arg1,arg2)
        self.use_msg = arg3
    
    def use(self):
        return
