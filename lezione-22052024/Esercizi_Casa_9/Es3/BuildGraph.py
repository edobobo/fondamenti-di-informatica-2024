from Grafo import Graph

## Costruzione di un grafo da un file che contiene il vertice
## di partenza e quello di arrivo di ogni arco del grafo
def costruisci_grafo(file):
    g = Graph()
    f = open(file,'r')
    for riga in f:
        dati = riga.strip().split()
        g.addEdge(dati[0],dati[1])
    f.close()
    return g
