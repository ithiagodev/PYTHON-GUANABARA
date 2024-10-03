salario = float(input("Qual é o salário do funcionário? R$"))

valor = salario * (1 + 0.10)
valor1 = salario * (1 + 0.15)

if salario >= 1250:
    print(f"Quem ganhava R${salario:.2f} passa a ganhar R${valor:.2f} agora")
else:
    print(f"Quem ganhava R${salario:.2f} passa a ganhar R${valor1:.2f} agora")