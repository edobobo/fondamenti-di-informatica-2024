def checkPieno(albero):
    if albero is None or albero.getRootVal() is None:  # condizione di base
        return False
    if albero.getRightChild() is None and albero.getLeftChild() is None:  # condizione di base
        return True
    else:
        return checkPieno(albero.getRightChild()) and checkPieno(albero.getLeftChild())
