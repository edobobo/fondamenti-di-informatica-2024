import BuildGraph
import Grafo
import Vertice


def has_cycle_bfs(g, sorgente):
    coda = [sorgente]
    visitati = set()
    while len(coda) > 0:
        v = coda.pop(0)
        if v not in visitati:
            visitati.add(v)
        else:
            continue
        for vicino in g.getVertex(v).getConnections():
            if vicino == sorgente:
                return True
            if (vicino not in visitati) and (vicino not in coda):
                coda.append(vicino)
    return False


def hasCycle(g):
    for chiave_nodo in g.getVertices():
        if has_cycle_bfs(g, chiave_nodo):
            return True
    return False


g = BuildGraph.costruisci_grafo("file1.txt")
print("Il valore di ritorno è: ", hasCycle(g)) #la funzione deve ritornare True
