def getRettangolo(b,h):
    if h <= 0 or b <= 0:
        return ""
    if h == 1:  # condizione di base
        return "+" * b
    else:
        return "+" * b + "\n" + getRettangolo(b,h-1)
