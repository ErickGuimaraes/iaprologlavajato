import json
class Graph:
    indice = 0
    nome = ""
    aresta = []
    peso = []
    def __init__(self, indice, name):
        self.nome = name
        self.indice = indice
        self.aresta =[]
        self.peso =[]
def LulaTaPreso(graphs):
    for sujeito in graphs:
        if(sujeito.nome == "luiz_inacio_lula_da_silva"):
            for i in range(len(sujeito.aresta)):
                if(sujeito.peso[i]=="condenadopor" or sujeito.peso[i]=="condenadopelo"):
                    return "SIM"
            return "NAO"
def MoroCondenaCabral(graphs):
    for sujeito in graphs:
        if(sujeito.nome == "sergio_moro"):
            for i in range(len(sujeito.aresta)):
                if(sujeito.peso[i]=="condena" and sujeito.aresta[i].nome =="sergio_cabral"):
                    return "SIM"
            return "NAO"
def ListaRelacoes(nome,graphs):
    for sujeito in graphs:
        if(sujeito.nome == nome):
            for i in range(len(sujeito.aresta)):
                print(nome," -> ",sujeito.peso[i]," por/com --> ",sujeito.aresta[i].nome)
jsonFile = open("graph.json","r")
text = jsonFile.read()
jsonFile.close()
jsonData =json.loads(text)
#print(jsonData)
graphs=[]
for iten in jsonData:
    grap= Graph(iten["indice"],iten["nome"])
    graphs.append(grap)
    #print(iten["indice"])
    #print(iten["nome"])
    #print(iten)
#print("======================")
for iten in jsonData:
    aresta = iten["aresta"]
    if(len(aresta)>0):
        ind = iten["indice"]
        pesos = iten["peso"]
        for i in range(len(aresta)):
            graphs[ind].aresta.append(graphs[aresta[i]])
            graphs[ind].peso.append(pesos[i])
    pesos =[]
    aresta =[]
for sujeito in graphs:
    if(sujeito.nome == "sergio_moro"):
            for i in range(len(sujeito.aresta)):
                print("moro -> ",sujeito.peso[i]," por/com --> ",sujeito.aresta[i].nome)

print("LULA TA PRESO ? ",LulaTaPreso(graphs))
print("MORO CONDENA CABRAL ? ",MoroCondenaCabral(graphs))
ListaRelacoes("aaa")