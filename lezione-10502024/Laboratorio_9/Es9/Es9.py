def uguali(albero1,albero2):

    if albero1 is None or albero2 is None:
        return False

    condizione1 = albero1.getRootVal() == albero2.getRootVal()
    condizione2 = (albero1.getLeftChild() is None and albero2.getLeftChild() is None) or uguali(albero1.getLeftChild(), albero2.getLeftChild())
    condizione3 = (albero1.getRightChild() is None and albero2.getRightChild() is None) or uguali(albero1.getRightChild(), albero2.getRightChild())

    return condizione1 and condizione2 and condizione3
