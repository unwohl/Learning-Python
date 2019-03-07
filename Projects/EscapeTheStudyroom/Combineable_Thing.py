from Takeable_Thing import Takeable_Thing

class Combineable_Thing(Takeable_Thing):
    abort = "you cannot combine this."
    
    def __init__(self,arg1,arg2,arg3,arg4,arg5,arg6):
        Takeable_Thing.__init__(self,arg1,arg2,arg3,arg4)
        self.combine_msg = arg5
        self.combine_objID = arg6
        
    def combine(self,objID):
        if objID == combine_objID:
            print(self.combine_msg.format(objID))
        else:
            print(abort)
                
