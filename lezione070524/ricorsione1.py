def fattoriale(numero):
    if numero == 0:
        return 1
    return numero * fattoriale(numero - 1)


def somma_lista(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + somma_lista(lista[1:])


def conta_dispari(lista):
    if len(lista) == 0:
        return 0
    if lista[0] % 2 == 1:
        return 1 + conta_dispari(lista[1:])
    else:
        return conta_dispari(lista[1:])


def check_numero_dispari(lista):
    if len(lista) == 0:
        return False
    if lista[0] % 2 == 1:
        return True
    else:
        return check_numero_dispari(lista[1:])


def ripeti_carattere_iterativo(n, c):
    acc = ""
    for i in range(n):
        acc += c
    return acc


def ripeti_carattere_ricorsivo(n, c):
    if n == 0:
        return ""
    return c + ripeti_carattere_ricorsivo(n - 1, c)


def stampa_rettangolo(a, b, c):
    if a == 0:
        return ""
    return ripeti_carattere_iterativo(b, c) + "\n" + stampa_rettangolo(a - 1, b, c)


def stampa_triangolo_iterativo(n):
    for i in range(1, n + 1):
        print(str(i) * i)


def stampa_triangolo_ricorsivo(n):
    if n == 0:
        return ""
    return stampa_triangolo_ricorsivo(n - 1) + str(n) * n + "\n"


def stringa_palindroma(stringa):
    if len(stringa) == 0 or len(stringa) == 1:
        return True
    return stringa[0] == stringa[-1] and stringa_palindroma(stringa[1:-1])


def alterna_liste(lista1, lista2):
    if len(lista1) == 0:
        return []
    return [lista1[0], lista2[0]] + alterna_liste(lista1[1:], lista2[1:])


def carattere_in_stringa(stringa, c):
    if len(stringa) == 0:
        return False
    return stringa[0] == c or carattere_in_stringa(stringa[1:], c)


def cerca_con_bisezione(lista, elem):
    if len(lista) == 0:
        return False
    centro_idx = len(lista) // 2
    if lista[centro_idx] == elem:
        return True
    elif elem > lista[centro_idx]:
        return cerca_con_bisezione(lista[centro_idx + 1 :], elem)
    else:
        return cerca_con_bisezione(lista[:centro_idx], elem)


if __name__ == "__main__":
    print(stampa_triangolo_ricorsivo(5))
