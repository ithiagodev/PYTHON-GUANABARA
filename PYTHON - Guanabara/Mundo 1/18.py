import math

a = float(input("Digite o ângulo que você deseja: "))

ar = math.radians(a)
s = math.sin(ar)
c = math.cos(ar)
t = math.tan(ar)


print(f"O ângulo de {a}° tem o seno de {s:.2f}")
print(f"O ângulo de {a}° tem o cosseno de {c:.2f}")
print(f"O ângulo de {a}° tem a tangente de {t:.2f}")