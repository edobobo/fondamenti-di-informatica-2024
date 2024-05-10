def uguali(s1,s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0 and len(s2) == 0:  # condizione di base
        return True
    return s1[0] == s2[0] and uguali(s1[1:], s2[1:])
