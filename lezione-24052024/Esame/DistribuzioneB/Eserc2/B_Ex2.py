def B_Ex2(m):
    if len(m) == 0 or len(m) != len(m[0]):
        return []

    nuova_matrice = []
    for i in range(len(m)):
        riga_corrente = m[i]
        nuova_riga = []
        for j in range(len(riga_corrente)):
            if j < i:
                nuova_riga.append(0)
            else:
                nuova_riga.append(riga_corrente[j])
        nuova_matrice.append(nuova_riga)
    return nuova_matrice
