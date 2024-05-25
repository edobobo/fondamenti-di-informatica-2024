def B_Ex1(s):
    acc = ""
    for i in range(len(s)):
        acc += (s[i] * (i + 1))
    return acc
