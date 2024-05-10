def mischiaStringhe(s1,s2):
    if len(s1) != len(s2):
        return ""
    if len(s1) == 0:  # condizione di base
        return ""
    return s1[0] + s2[-1] + mischiaStringhe(s1[1:], s2[:-1])
