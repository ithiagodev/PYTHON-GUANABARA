import math

o = float(input("Comprimento do cateto oposto: "))
a = float(input("Comprimento do cateto adjecente: "))

ot = math.hypot(o, a)

print(f"hipotenusa vai medir {ot:.2f}")