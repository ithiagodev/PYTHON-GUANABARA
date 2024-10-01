nome = input("Digite seu nome completo: ").strip()

print("Analisando seu nome...")
print(f"Seu nome em maiuscúlas é {nome.upper()}")
print(f"Seu nome em minuscúlas é {nome.lower()}")
print(f"Seu nome tem ao todo {nome.__len__() - nome.count(" ")} letras")
print(f"Seu primeiro tem {nome.find(" ")} letras")