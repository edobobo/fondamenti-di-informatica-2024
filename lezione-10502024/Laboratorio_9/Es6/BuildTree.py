## Questo modulo contiene funzioni che servono a costruire
## un albero binario a partire da una sua rappresentazione
## su file. Si noti che il formato della rappresentazione
## potrebbe variare

from BinaryTree import BinaryTree

def costruisci_albero(file, formato):
    diz_vertici = {}
    if formato == "n_sx,dx":
        f = open(file, "r", encoding="utf8")
        ## Saltiamo la prima riga che descrive il formato
        ## e inizializziamo la radice
        f.readline()
        line = f.readline()
        if line == "":
            return None
        riga = line.split()
        nodo = riga[0].strip()
        figli = riga[1].split(',')
        albero = BinaryTree(nodo)
        radice = albero
        diz_vertici[nodo] = radice
        if figli[0] != '-':
            albero.insertLeft(figli[0])
            diz_vertici[figli[0]] = albero.getLeftChild()
        if figli[1] != '-':
            albero.insertRight(figli[1])
            diz_vertici[figli[1]] = albero.getRightChild()
        ## Ora costruiamo il resto dell'albero
        for line in f:
            riga = line.split()
            nodo = riga[0].strip()
            figli = riga[1].split(',')
            albero = diz_vertici[nodo]
            if figli[0] != '-':
                albero.insertLeft(figli[0])
                diz_vertici[figli[0]] = albero.getLeftChild()
            if figli[1] != '-':
                albero.insertRight(figli[1])
                diz_vertici[figli[1]] = albero.getRightChild()
                
        f.close()
        return radice

    else:
        print("Formato sconosciuto")
        print()
        return None