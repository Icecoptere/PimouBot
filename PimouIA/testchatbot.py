from __future__ import print_function
import os
import aiml
os.chdir(".")

# config ------------------------------------------------
bot = "test"

BRAIN_FILE = f"{bot}_model.dump"

# Create the kernels ------------------------------------
x = aiml.Kernel()
x.verbose(True)

# Initialize bot
print("Initializing Bot" )
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    x.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    x.bootstrap(learnFiles = f"{bot}_learn.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    x.saveBrain(BRAIN_FILE)

while True:
    response = x.respond("message.content", "message.author.name")
    if response:
        print("Bot > ", response)
    else:
        print("Bot > :p ", )
