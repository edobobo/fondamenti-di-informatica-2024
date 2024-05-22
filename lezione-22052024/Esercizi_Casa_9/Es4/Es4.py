import BuildGraph
import Grafo
import Vertice


def bfs(g, sorgente, lista_nodi_da_evitare, target):
    coda = [sorgente]
    visitati = set()
    passi = dict()
    while len(coda) > 0:
        v = coda.pop(0)
        if v not in visitati:
            visitati.add(v)
        else:
            continue
        for vicino in g.getVertex(v).getConnections():

            if vicino == target:
                percorso = []
                nodo_corrente = target
                while nodo_corrente != sorgente:
                    step_precedente = passi[nodo_corrente]
                    percorso.insert(0, step_precedente)
                    nodo_corrente = step_precedente

            if (vicino not in visitati) and (vicino not in coda) and (vicino not in lista_nodi_da_evitare):
                coda.append(vicino)
                passi[vicino] = v
    return visitati


def evita(g, nodoA, nodoB, lista_nodi_da_evitare):
    #da completare a cura dello studente
    return None


g = BuildGraph.costruisci_grafo("file1.txt")
print("Il valore di ritorno è: ", evita(g,"1","7",["5","4","6"])) #la funzione deve ritornare True
print("Il valore di ritorno è: ", evita(g,"1","4",["3","7"])) #la funzione deve ritornare {}
