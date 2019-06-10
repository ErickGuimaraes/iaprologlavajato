import json
class Graph:
    indice = 0
    nome = ""
    aresta = []
    peso = []
    def __init__(self, indice, name):
        self.nome = name
        self.indice = indice

jsonFile = open("graph.json","r")
text = jsonFile.read()
jsonData =json.loads(text)
print(jsonData)
graphs=[]
for iten in jsonData:
    grap= Graph(iten["indice"],iten["nome"])
    graphs.append(grap)
    print(iten["indice"])
    print(iten["nome"])
    print(iten)
print("======================")
for iten in jsonData:
    aresta = iten["aresta"]
    if(len(aresta)>0):
        ind = iten["indice"]
        pesos = iten["peso"]
        print("aresta")
        print("ind=>",ind)
        print(aresta)
        print(pesos)
        print(len(aresta))
        print(len(pesos))
        
        for i in range(len(aresta)):
            graphs[i].aresta.append(graphs[aresta[i]])
            graphs[i].peso.append(pesos[i])

        
    
for gr in graphs:
    print(gr)
    print(gr.nome)
    print(gr.indice)
    if(len(gr.aresta)>0):
        print("tem aresta")
        print(gr.aresta)
        for i in range(len(gr.aresta)):
            print()
            print("nome => ",gr.nome)
            print("eh => ",gr.peso[i])
            print("por / com =>",gr.aresta[i].nome)
