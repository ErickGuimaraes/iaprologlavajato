import json
file = open("lavajato.pl","r")
itens =[]
lines = file.readlines()
for line in lines:
        newline =line.replace("\n","")
        if(not newline in itens):
                itens.append(newline)
file.close()
print(len(itens))
jsonFile = open("graph.json","r")
text = jsonFile.read()
jsonFile.close()
jsonData = json.loads(text)
for i in itens:
    print(i)