def contaOccorrenze(s,c):
    if len(s) == 0:  # condizione di base
        return 0
    if s[0] == c:
        return 1 + contaOccorrenze(s[1:], c)
    else:
        return contaOccorrenze(s[1:], c)
