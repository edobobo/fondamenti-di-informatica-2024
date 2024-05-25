def bfs(g, sorgente):
    coda = [sorgente]
    visitati = set()
    while len(coda) > 0:
        v = coda.pop(0)
        visitati.add(v)
        for vicino in g.getVertex(v).getConnections():
            if (vicino not in visitati) and (vicino not in coda):
                coda.append(vicino)
    return visitati


def B_Ex4(g, u, v):
    raggiungibili_da_u = bfs(g, u)
    raggiungibili_da_v = bfs(g, v)
    intersezione = raggiungibili_da_u.intersection(raggiungibili_da_v)
    somma = 0
    for elem in intersezione:
        somma += int(elem)
    return somma
