def B_Ex3(file):
    fi = open(file)
    dizionario = {}
    for riga in fi:
        riga = riga.strip()
        if len(riga) == 0:
            continue
        riga = riga.lower()
        parole = riga.split(" ")
        for parola in parole:
            if len(parola) != 0:
                if parola not in dizionario:
                    dizionario[parola] = 1
                else:
                    dizionario[parola] += 1
    return dizionario
