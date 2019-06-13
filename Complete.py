import json
import re
def findIndex(name,files):
    for item in jsonData:
        if (item["nome"]==name):
            return item["indice"]
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
    if(re.match(r"presidente_empresa\((.*),(.*)\)",i)):
        a =re.match(r"presidente_empresa\((.*),(.*)\)",i).group(1)
        b=re.match(r"presidente_empresa\((.*),(.*)\)",i).group(2)
        print(a)
        aIndex = findIndex(a,jsonData)
        print(aIndex)
        print(b)
        bIndex = findIndex(b,jsonData)
        jsonData[aIndex]["aresta"].append(bIndex)
        jsonData[aIndex]["peso"].append("presidiuempresa")
        print(bIndex)
        jsonData[bIndex]["aresta"].append(aIndex)
        jsonData[bIndex]["peso"].append("presididapor")
        print(jsonData[aIndex])
        print(jsonData[bIndex])
    if(re.match(r"politicopart\((.*),(.*)\)",i)):
        a =re.match(r"politicopart\((.*),(.*)\)",i).group(1)
        b=re.match(r"politicopart\((.*),(.*)\)",i).group(2)
        a=a.replace(" ","")
        print(a)
        aIndex = findIndex(a,jsonData)
        print(aIndex)
        b= b.replace(" ","")
        print(b)
        bIndex = findIndex(b,jsonData)
        if(bIndex ==None or aIndex == None):
            continue
        print(bIndex)
        jsonData[aIndex]["aresta"].append(bIndex)
        jsonData[aIndex]["peso"].append("filiado")
        jsonData[bIndex]["aresta"].append(aIndex)
        jsonData[bIndex]["peso"].append("temcomofiliado")
        print(jsonData[aIndex])
        print(jsonData[bIndex])


filejson = open("graph2.json","w")
filejson.write("[\n")
for i in jsonData:
        filejson.write("\t{\n")
        filejson.write('\t\t"indice" : '+str(i["indice"])+',\n')
        filejson.write('\t\t"nome" : "'+i["nome"]+'",\n')
        filejson.write('\t\t"aresta" : '+str(i["aresta"])+',\n')
        pesos =str(i["peso"])
        pesos =pesos.replace("\'","\"")
        filejson.write('\t\t"peso" : '+pesos+'\n')
        if(i == len(itens)-1):
                filejson.write("\t}\n")
        else:
                filejson.write("\t},\n")

filejson.write("]\n")
filejson.close()
