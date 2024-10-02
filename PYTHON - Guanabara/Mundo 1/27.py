nome = str(input("Digite seu nome completo? ")).strip()

pn = nome.split()
un = nome.rsplit()

print('Muito prazer em te conhecer!')
print(f"Seu primeiro nome é {pn[0]}")
print(f"Seu último nome é {un[-1]}")