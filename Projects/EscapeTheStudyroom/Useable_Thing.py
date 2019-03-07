from Thing import Thing

class Useable_Thing(Thing):
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2) # == self.description = arg1; self.ID = arg2
        self._use = arg3
    
    def use(self):
        return
