import textwrap

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado!")
    else:
        print("Valor inválido para depósito. Digite um número maior que zero.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    if valor <= 0:
        print("Valor de saque inválido! Digite um valor maior que zero.")
    elif valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite:
        print(f"Valor de saque excede o limite de R$ {limite:.2f} por operação!")
    elif num_saques >= limite_saques:
        print("Número máximo de saques diários atingido!")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        num_saques += 1
        print("Saque realizado!")
    return saldo, extrato, num_saques

def exibir_extrato(saldo, *, extrato):
    print("\n----- EXTRATO -----")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("-------------------")

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(u["cpf"] == cpf for u in usuarios):
        print("Usuário já cadastrado!")
        return
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário cadastrado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário para vincular à conta: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado!")
        return None

def list_contas(contas):
    print("\n----- Lista de Contas -----")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")
    print("---------------------------")

def menu():
    opcoes = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Lista de Contas
[q] Sair
=> """
    return input(textwrap.dedent(opcoes))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    agencia = "0001"
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            try:
                valor = float(input("Informe o valor para depósito: "))
            except ValueError:
                print("Valor inválido!")
                continue
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            try:
                valor = float(input("Informe o valor para saque: "))
            except ValueError:
                print("Valor inválido!")
                continue
            saldo, extrato, num_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                limite_saques=limite_saques
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            novo_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            list_contas(contas)
        
        elif opcao == "q":
            print("Encerrando o sistema...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
