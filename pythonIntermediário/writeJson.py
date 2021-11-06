import json

d1 = {
    "Pessoa 1": {"nome": "Pedro", "idade": "50"},
    "Pessoa 2": {"nome": "Pedro", "idade": "60"},
}

d1_json = json.dumps(d1, indent=True)

with open("app.json", "w+") as file:
    file.write(d1_json)

print(d1_json)
