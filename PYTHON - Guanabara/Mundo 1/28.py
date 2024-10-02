import random
import time

computador = random.randint(0, 5)

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. tente adivinhar...")
print("-=-" * 20)

jogador = int(input("Em que número pensei? "))

print("PROCESSANDO...")
time.sleep(3)

if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f"GANHEI! eu pensei no número {computador} e não no {jogador}!")