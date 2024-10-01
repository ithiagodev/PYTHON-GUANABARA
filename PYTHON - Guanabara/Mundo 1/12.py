p = float(input("Qual é o preço do produto? R$"))

d = p - (p * 5 / 100)

print(f"O produto que custava R${p}, na promoção com desconto de 5% passou a custar R${d:.2f}")