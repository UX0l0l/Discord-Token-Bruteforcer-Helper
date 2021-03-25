#!/usr/bin/python3
import ctypes, os, threading, base64
from strgen import StringGenerator
tokenid = "4030200023"


class Discord:
    def __init__(self):
        self.regularExpression = ".([a-zA-Z0-9]{6})\.([a-zA-Z0-9]{27})" # This is the regular expression for discord.
        self.generated = 0

    def generate(self):
        discordToken = StringGenerator(self.regularExpression).render()
        discordToken = discordToken.replace("..", ".")
        discordToken = str(id) + discordToken 
        print(discordToken)
        self.generated += 1
        self.write(discordToken)

    def new_method(self):
        return self.regularExpression
    
    def write(self, discordToken):
        if os.path.isfile("./tokens.txt"):
            writeToken = open("./tokens.txt", "a")
            writeToken.write(f"{discordToken}\n")
        else:
            open("./tokens.txt", "w").close() # Simply create the file.

open("./tokens.txt", "w").close() # Create and clear our token file each time
token = Discord()
amountToGen = int(input("Enter amount of tokens to generate: "))

id = base64.b64encode((input("Enter ID: ")).encode("ascii"))
id = str(id)[2:-1]

for _ in range(amountToGen):
    threading.Thread(target=token.generate).start()
