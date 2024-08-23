# This is a very dumb idea, but I'm bored.
# Do not judge my code, because if you do, I will SEVERELY not care >:(
# For the context, Orpheus the Hack Club dinosaur told me to do that, and I listen because Orpheus is handsome <3
# Perhaps this code will become a meme in the Python dev community in a few years (I have the right to dream ok?)

from random import *

newmessage = ""

message = input("What message would you like to ABSOLUTELY DESTROY? ")
if message != "":
    listmessage = list(message)
    for i in range (randint(len(message)//10, len(message)//2)):
        listmessage.pop(randint(0,len(listmessage)-1))
else:
    print("You haven't written anything :< *sad Orpheus noises*")

for i in range (len(listmessage)):
    newmessage = newmessage + listmessage[i]

print("               __\n              / _)   < " + newmessage + "\n     _.----._/ /\n    /         /\n __/ (  | (  |\n/__.-'|_|--|_|")