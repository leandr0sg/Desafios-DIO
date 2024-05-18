from os import system
from time import sleep


menu = """
#-----MENU------#
| d - Depósitar |
| s - SACAR     |
| e - Extrato   |
| q - Sair      |
#---------------#"""
saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3  #Constante com limite de saque

while True:
    system('cls')
    print(menu)
    opcao = input("O que deseja fazer?: ")

    if opcao == 'd':
        valor_deposito = float(input("Valor do deposito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Você depósitou R$ {valor_deposito:.2f}")

    elif opcao == 's':

        if numeros_saques < LIMITE_SAQUES:
            print("Seu saldo é: ", saldo)
            valor_saque = float(input("Valor do saque: "))

            if (valor_saque <= saldo) and (saldo > 0):
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numeros_saques += 1
                print(f"Você sacou R$ {valor_saque:.2f}")
            
            elif saldo == 0:
                print(f"Você não possui saldo suficiente\nSaldo é R$ {saldo:.2f}")
            
            elif valor_saque > saldo:
                print(f"Não foi possivel realizar seu saque\nValor saque maior que seu saldo\nSaldo é R$ {saldo:.2f}")
                sleep(2)
            
        else:
            print("Você atingiu a quantidade máxima de saques disponíveis!")

    elif opcao == 'e':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    
    elif opcao == 'q':
        print("Finalizando o atendimento! Obrigado!")
        break
    
    else:
        print("INVÁLIDO!\nPor favor, digite d - Depósitar, s - SACAR, e - Extrato ou q - Sair")

    sleep(2)