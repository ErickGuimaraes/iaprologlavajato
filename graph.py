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
def OdebrechtTemCorruptos(graphs):
    for sujeito in graphs:
        if(sujeito.nome == "odebrecht"):
            for i in range(len(sujeito.aresta)):
                if(sujeito.peso[i]=="funcionario"):
                    for sujeito2 in graphs:
                        if(sujeito2.nome == sujeito.aresta[i].nome):
                            for ind in range(len(sujeito2.aresta)):
                                if("condenadopor" in sujeito2.peso[ind]):
                                    if("corrupcao" in sujeito2.aresta[ind].nome ):
                                        return "SIM"
            return "NAO"
def MarceloCondenouGovernadorRio(graphs):
    for sujeito in graphs:
        if(sujeito.nome == "marcelo_bretas"):
            for i in range(len(sujeito.aresta)):
                if(sujeito.peso[i]=="condena"):
                    for sujeito2 in graphs:
                        if(sujeito2.nome == sujeito.aresta[i].nome):
                            for ind in range(len(sujeito2.peso)):
                                if("governa" == sujeito2.peso[ind] and sujeito2.aresta[ind].nome == "rio_de_janeiro_estado"):
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
graphs=[]
for iteescravizacao_de_criancas.n in jsonData:
    grap= Graph(iten["indice"],iten["nome"])
    graphs.append(grap)

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

print("LULA TA PRESO ? ",LulaTaPreso(graphs))
print("MORO CONDENA CABRAL ? ",MoroCondenaCabral(graphs))
print("ODEBRECHT TEM FUNCIONARIOS CORRUPTOS ? ",OdebrechtTemCorruptos(graphs))
print("MARCELO BRETAS CONDENOU ALGUM GOVERNADOR DO RIO ? ",MarceloCondenouGovernadorRio(graphs))
#ListaRelacoes("marcelo_odebrecht",graphs)