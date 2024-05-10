def contaFoglie(albero):
    if albero is None:  # condizione di base
        return 0
    if albero.getRightChild() is None and albero.getLeftChild() is None:  # condizione di base
        return 1
    else:
        return contaFoglie(albero.getRightChild()) + contaFoglie(albero.getLeftChild())
