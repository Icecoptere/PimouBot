import os
import aiml
os.chdir('./PimouIA')

BRAIN_FILE = "test_model.dump"
k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    print(os.getcwd())
    k.bootstrap(learnFiles="test_learn.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)


def get_response(input_text,input_user):
    return k.respond(input_text, input_user)
