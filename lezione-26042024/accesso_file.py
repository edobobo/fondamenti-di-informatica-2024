percorso_file = (
    "/Users/edoardobarba/misc/fondamenti-di-informatica-2024/lezione-26042024/test1.txt"
)

file_1 = open(percorso_file)

for riga in file_1:
    riga = riga.strip()
    print(riga)

print("Fine primo loop")

for riga in file_1:
    print(riga)

print("Fine secondo loop")

file_1.close()
