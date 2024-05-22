import BuildGraph
import Grafo
import Vertice

def hasSink(g):
    for v in g:
        if len(v.getConnectios()) == 0:
            return True
    return False


g = BuildGraph.costruisci_grafo("file1.txt")
print("Il valore di ritorno è: ", hasSink(g)) #la funzione deve ritornare False
