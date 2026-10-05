def deposito(saldo):
    print("===== DEPÓSITO =====")

    valor = int(input("Digite o valor que deseja depositar: "))

    if valor > 0:
        saldo = saldo + valor
        print("Deposito realizado com sucesso!")
    else:
        print("Valor Inválido")
    return saldo

def saque(saldo):
    print("===== SAQUE =====")

    valor = int(input("Digite o valor que deseja sacar: \n"))

    if valor > 0:
        if valor <= saldo:
            saldo = saldo - valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
    else:
        print("Valor invalido!")
    return saldo

def banco():

    saldo = 0
    opcao = 0

    while opcao != 4:

        print("\n===== BANCO =====")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Consultar saldo")
        print("4 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            saldo = deposito(saldo)

        elif opcao == 2:
            saldo = saque(saldo)

        elif opcao == 3:
            print(f"Seu saldo é: R$ {saldo}")

        elif opcao == 4:
            print("Saindo do banco...")

        else:
            print("Opção inválida!")


banco()