import os
import aiml

BRAIN_FILE = "brain.dump"

k = aiml.Kernel()


if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

while True:
    input_text = input("> ")
    response = k.respond(input_text)
    print(response)
