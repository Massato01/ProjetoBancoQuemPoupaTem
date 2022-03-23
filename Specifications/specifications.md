# ***Projeto - Banco QuemPoupaTem***

## **Especificações:**
## 3 tipos de conta:
 ## > Salário:
   * Cobra taxa de 5% a cada débito realizado
   * Não permite débitos que deixem a conta com saldo negativo
 
 ## > Comum:
   * Cobra taxa de 3% a cada débito realizado
   * Permite um saldo negativo de até R$500,00

 ## > Plus:
   * Cobra taxa de 1% a cada débito realizado
   * Permite um saldo negativo de até R$5.000,00

---

## O sistema criado deve funcionar em `loop infinito` até que se deseja sair

---

## Um menu de opções deve ser sempre apresentado ao operador, contendo as seguintes operações

---

>### 1. Novo Cliente
>### 2. Apaga Cliente
>### 3. Debita
>### 4. Deposita
>### 5. Saldo
>### 6. Extrato
>### 0. Sai

---

# ***Opção 1 - novo cliente***
## > Dados Solicitados:
  * Nome
  * Cpf
  * Tipo de conta (salário, comum, plus)
  * Valor inicial da conta
  * Senha do usuário

# ***Opção 2 - Apaga o cliente pelo CPF***

# ***Opção 3 - Debitar um valor da conta do cliente***
## > Dados Solicitados:
  * CPF
  * Senha
  * Valor
### __O débito só pode ser feito de o CPF e senha estiverem corretos__

# ***Opção 4 - Depositar valor na conta do cliente***
## > Dados Solicitados:
  * CPF
  * Valor

# ***Opção 5 - Exibe o saldo da conta do cliente***
## > Dados Solicitados:
  * CPF
  * Senha
### __O débito só pode ser feito de o CPF e senha estiverem corretos__

# ***Opção 6 - Extrato - exibe o histórico de __todas__ as operações realizadas na conta, com datas e valores, incluindo as tarifas***
## > Dados Solicitados:
  * CPF
  * Senha

| Nome: Fulano de Fulano Fulano       | CPF: 123456   | Conta: Comum     |
| ----------------------------------- |:-------------:| ----------------:|
| Data: 2018-09-13  17:08  +  600.00  | Tarifa: 0.00  |  Saldo:  600.00  |
| Data: 2018-09-13  17:13  +    5.00  | Tarifa: 0.05  |  Saldo:  594.85  |
| Data: 2018-09-13  17:15  +   10.00  | Tarifa: 0.00  |  Saldo:  604.85  |

---

# **Cada opção deve ser implementada como uma __função__!**

---

# Importante:
## O banco __não__ pode perder as informações se o programa terminar, trabalhar com arquivos

# ***POR FIM***
## Explicação do Terminal em PDF