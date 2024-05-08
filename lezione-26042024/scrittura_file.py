percorso_file_scrittura = (
    "/Users/edoardobarba/misc/fondamenti-di-informatica-2024/lezione-26042024/test2.txt"
)

file_2 = open(percorso_file_scrittura, "w")

file_2.write("Ciao sono Edoardo\n")
file_2.write("Ciao sono Roberto")

file_2.close()
