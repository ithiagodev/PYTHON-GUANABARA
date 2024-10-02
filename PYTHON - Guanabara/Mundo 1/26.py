frase = str(input("Digite uma Frase: ")).strip().upper()

fc = frase.count("A")
fa = frase.find("A") + 1
far = frase.rfind("A") + 1

print(f"A letra A aparece {fc} vezes na frase")
print(f"A primeira letra A aparece na posição {fa}")
print(f"A última letra A aparece na posição {far}")