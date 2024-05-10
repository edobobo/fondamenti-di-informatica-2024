def massimo(albero):
    if albero is None or albero.getRootVal() is None:  # condizione di base
        return 0
    chiave = int(albero.getRootVal())
    return max([chiave, massimo(albero.getRightChild()), massimo(albero.getLeftChild())])
