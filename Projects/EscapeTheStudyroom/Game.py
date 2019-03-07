from Thing import Thing
from Room import Room
import Parser

game_ended = False

inventory = {}

nput = {}

roomID = 0

Rooms = open("Rooms.txt","r")

while not game_ended:
    nput = Parser.getInput()
    print (nput)
