file = open("entrada.txt","r")
itens =[]
lines = file.readlines()
for line in lines:
        newline =line.replace("\n","")
        if(not newline in itens):
                itens.append(newline)
print(len(itens))
itens.sort()
for i in itens:
        print(i)

print(len(itens))
file.close()
filejson = open("graph.json","w")
filejson.write("[\n")
for i in range(len(itens)):
        filejson.write("\t{\n")
        filejson.write('\t\t"indice" : '+str(i)+',\n')
        filejson.write('\t\t"nome" : "'+itens[i]+'",\n')
        filejson.write('\t\t"aresta" : [],\n')
        filejson.write('\t\t"peso" : []\n')
        if(i == len(itens)-1):
                filejson.write("\t}\n")
        else:
                filejson.write("\t},\n")

filejson.write("]\n")
filejson.close()
