import BuildGraph
import Grafo
import Vertice


def bfs(g, sorgente):
    coda = [sorgente]
    visitati = set()
    while len(coda) > 0:
        v = coda.pop(0)
        if v not in visitati:
            visitati.add(v)
        else:
            continue
        for vicino in g.getVertex(v).getConnections():
            if (vicino not in visitati) and (vicino not in coda):
                coda.append(vicino)
    return visitati


def bidirezionale(g, nodoA, nodoB):
    visitati_da_a = bfs(g, nodoA)
    visitati_da_b = bfs(g, nodoB)
    return nodoA in visitati_da_b and nodoB in visitati_da_a




g = BuildGraph.costruisci_grafo("file1.txt")
print("Il valore di ritorno è: ", bidirezionale(g,"1","6")) #la funzione deve ritornare True
print("Il valore di ritorno è: ", bidirezionale(g,"3","5")) #la funzione deve ritornare False
