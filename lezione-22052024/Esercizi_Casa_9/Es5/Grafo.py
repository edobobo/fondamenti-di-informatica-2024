from Vertice import Vertex

class Graph:

    ## Inizializza un oggetto di classe Graph vuoto 
    def __init__(self):
        self.vertList = {}

    ## Aggiunge un vertice dato il suo identificatore (una stringa)
    def addVertex(self,key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    ## Dato un identificatore, restituisce il riferimento all'oggetto Vertex
    ## corrispondente se il vertice esiste, None altrimenti
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    ## Verifica se un vertice con un specifico identificatore è contenuto nel
    ## grafo oppure no
    def __contains__(self,n):
        return n in self.vertList

    ## Dati gli identificatori f e t di due vertici, aggiunge l'arco (f, t), creando
    ## gli oggetti di classe Vertex se necessario
    def addEdge(self,f,t,cost=1):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(t, cost)

    ## Restituisce una sequenza contenente gli identificatori dei vertici
    def getVertices(self):
        return list(self.vertList.keys())

    ## Iterazione fra i vertici del grafo basata sui valori del dizionario
    ## vertList
    def __iter__(self):
        return iter(self.vertList.values())
