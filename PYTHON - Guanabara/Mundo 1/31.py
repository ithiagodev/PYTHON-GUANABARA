viagem = float(input("Qual é a distância da sua viagem? "))

valor = viagem * 0.50
valor1 = viagem * 0.45

print(f"Você está prestes a começar uma viagem de {viagem}Km")

if viagem >= 200:
    print(f"E o preço da sua passagem será de R${valor1:.2f}")
else:
    print(f"E o preço da sua passagem será de R${valor:.2f}")
