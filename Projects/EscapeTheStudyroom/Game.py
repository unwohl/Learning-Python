from Thing import Thing
from Useable_Thing import Useable_Thing
from Takeable_Thing import Takeable_Thing
from Combineable_Thing import Combineable_Thing
from Room import Room
import Parser

Desk = Thing("This is a desk",1)
Desk_Drawer = Useable_Thing("This is a drawer",2,"You try to open the drawer but it is locked.")
Desk_Drawer_Key = Takeable_Thing("This is the key for the drawer.",3)
Desk_Drawer_Lock = Combineable_Thing("This is the lock of the drawer.",4)



game_ended = False 

inventory = {}

roomID = 0

Rooms = open("Rooms.txt","r")

while not game_ended:
    _Input = Parser.getInput()
