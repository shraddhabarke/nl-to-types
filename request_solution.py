import requests
import json

with open("conala-test-annotated.json") as jsonFile:
    data = json.load(jsonFile)

for d in data:
    intent = d['rewritten_intent']
    if intent == None:
        intent = d['intent']
    response = requests.get("http://moto.clab.cs.cmu.edu:8081/parse/conala?q={query}".format(query = intent))
    obj = json.loads(response.content)
    program = list(obj.values())[0][0]['value']
    print(intent, program)