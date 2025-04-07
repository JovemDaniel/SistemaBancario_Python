# Sistema Bancário com Python

Este projeto implementa um sistema bancário simples utilizando Python. Ele permite simular operações básicas de um banco, como depósitos, saques, consulta de extrato, cadastro de usuários e criação de contas. O objetivo é praticar o uso de funções, controle de fluxo e manipulação de dados, além de reforçar as regras de negócio (como não permitir depósitos negativos, saques acima do limite e limitar o número diário de saques).

## Funcionalidades

- **Depósito:**  
  Permite depositar valores positivos. O valor depositado é adicionado ao saldo e registrado no extrato.
  
- **Saque:**  
  Permite sacar valores respeitando as seguintes regras:
  - O valor deve ser positivo.
  - O saque não pode ser maior que o saldo.
  - O valor não pode exceder o limite máximo de R$ 500,00 por operação.
  - São permitidos apenas 3 saques diários.

- **Extrato:**  
  Exibe todas as transações (depósitos e saques) realizadas e o saldo atual. Caso não haja transações, informa que nenhuma movimentação foi realizada.

- **Cadastro de Usuário:**  
  Permite cadastrar novos usuários, garantindo que não haja duplicidade de CPF.

- **Criação de Conta Bancária:**  
  Cria uma nova conta associada a um usuário cadastrado. Cada conta possui um número sequencial e está vinculada a um usuário.

- **Listagem de Contas:**  
  Exibe todas as contas criadas, mostrando a agência, o número da conta e o nome do titular.

## Requisitos

- Python 3.x

## Como Executar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/JovemDaniel/SistemaBancario_Python
   cd SistemaBancario_Python
   python main.py
