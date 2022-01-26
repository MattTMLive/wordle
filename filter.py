import json

with open("donda.txt") as words:
    words = words.read().splitlines()

fiveletterwords = []

for word in words:
    if len(word) == 5:
        fiveletterwords.append(word)

with open("words.json", "w+") as words:
    json.dump(fiveletterwords, words)
