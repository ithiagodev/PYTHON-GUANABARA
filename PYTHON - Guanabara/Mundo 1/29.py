velocidade = int(input("Qual é a velocidade atual do carro? "))

valor = (velocidade - 80) * 7

if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h")
    print(f"Você deve pagar uma multa de R${valor}!")
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print("Tenha um bom dia! Dirija com segurança")