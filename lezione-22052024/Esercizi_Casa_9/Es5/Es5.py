import BuildGraph
import Grafo
import Vertice


def raggiungibili(g, u, l):
    nodo_corrente = u
    while len(l) != 0:
        prossimo_nodo = l.pop(0)
        if prossimo_nodo in g.getVertex(u).getConnections():
            nodo_corrente = prossimo_nodo
        else:
            return False
    return True


g = BuildGraph.costruisci_grafo("file1.txt")
print("Il valore di ritorno è: ", raggiungibili(g, "1", ["2","3","4"])) #la funzione deve ritornare True
