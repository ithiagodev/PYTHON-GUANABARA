real = float(input("Quanto dinheiro você tem na carteira? R$"))

dolar = real / 5.43
euro = real / 6.07

print(f"Com R${real:.2f} você pode compra US${dolar:.2f}")
print(f"Com R${real:.2f} você pode compra €{euro:.2f}")