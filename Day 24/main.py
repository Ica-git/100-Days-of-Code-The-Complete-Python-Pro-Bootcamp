
lista = []

with open("imena.txt") as file:
    imena = file.readlines()
    for ime in imena:
        novo = ime.strip("\n")
        lista.append(novo)


with open("Pozivnice/templejt.txt") as file_pozivnica:
    text = file_pozivnica.read()

    for i in range(0,len(lista)):
        pozivnica_spremna = text.replace("[name]", lista[i])
        with open(f"SpremneZaSlanje/{lista[i]}.txt", "w") as file:
            file.write(pozivnica_spremna)

