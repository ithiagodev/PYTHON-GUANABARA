numero = int(input("Digite um número inteiro: "))

print("Escolha uma das bases para conversão:")
print("[ \033[32m1\033[m ] converter para \033[32mBINÁRIO\033[m")
print("[ \033[31m2\033[m ] converter para \033[31mOCTAL\033[m")
print("[ \033[34m3\033[m ] converter para \033[34mHEXADECIMAL\033[m")

opcao = int(input("Sua Opção: "))

if opcao == 1:
    print(f"\033[36m{numero}\033[m convertido para \033[32mBINÁRIO\033[m é igual a \033[32m{bin(numero)[2:]}\033[m")
elif opcao == 2:
    print(f"\033[36m{numero}\033[m convertido para \033[31mOCTAL\033[m é igual a \033[31m{oct(numero)[2:]}\033[m")
elif opcao == 3:
    print(f"\033[36m{numero}\033[m convertido para \033[34mHEXADECIMAL\033[m é igual a \033[34m{hex(numero)[2:]}\033[m")
else:
    print("\033[31mOPÇÃO INVÁLIDA\033[m!")
