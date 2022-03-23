import os
from time import sleep
import datetime


# CORES NO TERMINAL
class Colors:

    def __init__(self):
        self.normal = '\033[m'
        self.black = '\033[30m'
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.yellow = '\033[33m'
        self.blue = '\033[34m'
        self.magenta = '\033[35m'
        self.cyan = '\033[36m'
        self.gray = '\033[37m'

color = Colors()


# IMPRIME O MENU INICIAL
def print_menu(name):
    '''
    Impressão do Menu do banco
    '''
    print(name.center(30, '-'))
    print('''
| [ 1 ]  Novo Cliente
| [ 2 ]  Apagar Cliente
| [ 3 ]  Debitar
| [ 4 ]  Depositar
| [ 5 ]  Ver Saldo
| [ 6 ]  Ver Extrato
| [ 0 ]  Sair''')


# MOSTRA OS TIPOS POSSÍVEIS DE CONTA DO BANCO
def account_types():
    '''
    Função que exibirá os tipos possíveis de conta do banco QuemPoupaTem.
    '''

    print('~' * 74)
    print(f'''
    TIPOS DE CONTA
        {color.magenta}( 1 ) Salário{color.normal}
          - Cobra taxa de '5%' a cada débito realizado
          - Não permite débitos que deixem a conta com saldo negativo
        
        {color.yellow}( 2 ) Comum{color.normal}
          - Cobra taxa de '3%' a cada débito realizado
          - Permite um saldo negativo de até R$500,00
          
        {color.green}( 3 ) Plus{color.normal}
          - Cobra taxa de '1%' a cada débito realizado
          - Permite um saldo negativo de até R$5.000,00
          ''')
    print('~' * 74)


# CRIA UM NOVO USUÁRIO PARA O CLIENTE
def new_user():
    '''
    Função responsável por criar um novo usuário.
    São criadas as variáveis características de um usuário e o tipo de conta.
    A entrada dos valores é validada por um TRY, caso ocorra um erro será exibido
    o tipo primitivo exigido por cada variável.
    Por fim verificamos SE já existe um usuário com o mesmo CPF, SENÃO,
    armazenamos seus dados em um arquivo separado dentro da pasta users.
    '''

    # Verificando se as entradas são válidas
    try:
        account_type = int(input('Tipo de conta: '))
        name = str(input('Nome: ')).title()
        cpf = int(input('CPF: '))   
        initial_value = float(input('Valor inicial da conta: '))
        password = int(input('Senha da conta (PIN): '))
    
    except: # Tipos primitivos exigidos por cada variável
        print(f'\n{color.yellow}Por favor, digite um valor válido!{color.normal}')
        print('Tipo de conta: numeral')
        print('Nome: string')
        print('CPF: numeral')
        print('Valor inicial: numeral')
        print(f'{color.magenta}Senha: numeral 4 dígitos no mínimo{color.normal}\n')
        sleep(5)
        os.system('cls')
    
    else:
        # Verificando se já existe um usuário com o mesmo CPF
        if os.path.isfile(f'./users/{cpf}.txt'):

            # Se já existir, isso será executado
            print(f'\n{color.yellow}Cliente já registrado!{color.normal}\n')
            sleep(2.5)
            os.system('cls')

        else:
            # Armazenando os dados em um arquivo separado
            with open(f'./users/{cpf}.txt', 'w') as user_file:
                
                # Escrevendo o tipo de conta
                if account_type == 1:
                    user_file.write('Salario\n')

                elif account_type == 2:
                    user_file.write('Comum\n')

                elif account_type == 3:
                    user_file.write('Plus\n')

                # Dados digitados pelo cliente
                user_file.write(f'{name}\n')
                user_file.write(f'{cpf}\n')
                user_file.write(f'{initial_value}\n')
                user_file.write(f'{password}\n')
            
            # Criando arquivo de dados do usuário (extrato)
            with open(f'./users_bankstatement/{cpf}.txt', 'w'):
                pass

            os.system('cls')
            print(f'\n{color.cyan}Usuário {name} criado com sucesso!{color.normal}')
            sleep(2.5)
            os.system('cls')


# DELETA UM USUÁRIO EXISTENTE
def delete_user():
    '''
    Função responsável por excluir um usuário existente.
    Primeiro verificando se o usuário existe com a biblioteca OS.
    Se forem iguais, o conteúdo dentro do arquivo do usuário será armazenado em
    uma outra variável que será utilizada para verificar se o CPF e a Senha são iguais à do usuário.
    '''
    # Impedindo que ocorra um erro durante a execução do prorgama
    try:
        cpf = int(input('\nDigite o CPF do usuário que deseja excluir: '))
        password = int(input('Digite a senha do usuário que deseha excluir: [PIN] '))
    except:
        print(f'{color.red}\nValor inválido!{color.normal}')
        sleep(2)
        os.system('cls')
    else:
    
        # Verificando se o usuário existe
        if os.path.isfile(f'./users/{cpf}.txt'):
            with open(f'./users/{cpf}.txt', 'r') as file:
                list_filelines = file.readlines()
            
            # Verificando se a senha é igual à do usuário
            if password == int(list_filelines[4]):
                sleep(1)

                # Excluindo a conta do cliente
                print(f'\n{color.cyan}Usuário {list_filelines[1]}Excluído com sucesso{color.normal}\n')
                os.remove(f'./users/{cpf}.txt') # Excluindo o arquivo do usuário
                os.remove(f'./users_bankstatement/{cpf}.txt') # Excluindo o arquivo de dados
                
                sleep(3)
                os.system('cls')
            
            else:
                # Isso será executado caso a senha esteja incorreta
                print(f'\n{color.red}Senha ou CPF incorretos\n{color.normal}')
                
                sleep(3)
                os.system('cls')

        else:
            # Isso será executado caso o arquivo do usuário não seja encontrado
            print(f'\n{color.yellow}Usuário Inexistente{color.normal}\n')
            
            sleep(2)
            os.system('cls')


# DEBITAR
def debit_payment():
    '''
    Função responsável pelo débito.
    São necessários: um arquivo de usuário existente e CPF e senha de acordo
    Será pedido a quantidade de dinheiro que o cliente deseja debitar, e a cada execução será cobrada uma taxa de acordo com as especificações de sua conta.
    Especificações de cada tipo de conta:
    ( 1 ) Salário:
      - Cobra taxa de 5% a cada débito realizado
      - Não permite débitos que deixem a conta com saldo negativo
        
    ( 2 ) Comum:
      - Cobra taxa de 3% a cada débito realizado
      - Permite um saldo negativo de até R$500,00

    ( 3 ) Plus:
      - Cobra taxa de 1% a cada débito realizado
      - Permite um saldo negativo de até R$5.000,00    
    '''
    # Impedindo que ocorra um erro durante a execução do programa
    try:
        cpf = int(input('Digite o CPF da conta: '))
        password = int(input('Digite a senha da conta: [PIN] '))
    except:
        print(f'{color.red}\nValor inválido!{color.normal}')
        sleep(2)
        os.system('cls')
    else:

        # Verificando se o usuário existe
        if os.path.isfile(f'./users/{cpf}.txt'):

            with open(f'./users/{cpf}.txt', 'r') as file:
                list_filelines = file.readlines()
            
            # Verificando se a CPF e SENHA estão corretos
            if cpf == int(list_filelines[2]) and password == int(list_filelines[4]):

                # Valor a ser debitado
                money_amount = float(input('Valor a ser debitado: R$'))
                
                # Debitar da conta Salário
                if list_filelines[0].startswith('Sal'):
                    
                    # Descontando a taxa para contas SALARIO
                    tax = 0.05

                    account_balance = float(list_filelines[3])
                    new_account_balance = account_balance - money_amount
                    final_account_balance = new_account_balance - (new_account_balance * tax)
                    
                    # Transformando o valor final em String
                    list_filelines[3] = str(f'{final_account_balance}\n')

                    # Restrição da conta Salário -> Mínimo == 0
                    if float(list_filelines[3]) < 0:
                        os.system('cls')

                        # Será executado caso a quantidade de dinheiro supere o limite
                        print('~' * 35)
                        print(f'\n{color.red}   Impossível realizar o Débito!{color.normal}\n\n       Saldo atual: R${float(account_balance):.2f}\n\n{color.yellow}O saldo mínimo da sua conta é $-0,00{color.normal}\n')
                        print('~' * 35)
                        sleep(4)
                        os.system('cls')
                    
                    else:

                        # Alteração do do saldo no arquivo
                        with open(f'./users/{cpf}.txt', 'w') as file:
                            file.writelines(list_filelines)
                        
                        # Caso de tudo certo, isso será executado
                        os.system('cls')
                        print('~' * 32)
                        print(f'\n{color.green} Valor Debitado com sucesso!{color.normal}')
                        print(f"\n{color.cyan}    Cobrado '5%' de taxa{color.normal}")
                        print(f'\n\033[1mSaldo atual da conta: R${float(list_filelines[3]):.2f}\n{color.normal}')
                        print('~' * 32)
                        
                        # Armazenando os dados do débito
                        count_negative_statement(cpf, money_amount, final_account_balance)

                        sleep(4)
                        os.system('cls')
                
                # Debitar da conta Comum
                elif list_filelines[0].startswith('Com'):
                    
                    # Descontando a taxa para contas COMUM
                    tax = 0.03

                    account_balance = float(list_filelines[3])
                    new_account_balance = account_balance - money_amount
                    final_account_balance = new_account_balance - (new_account_balance * tax)

                    list_filelines[3] = str(f'{final_account_balance}\n')

                    # Restrição da conta Comum -> Mínimo == -500
                    if float(list_filelines[3]) < -500:
                        os.system('cls')

                        # Será executado caso a quantidade de dinheiro supere o limite
                        print('~' * 37)
                        print(f'\n{color.red}   Impossível realizar o Débito!{color.normal}\n\n     Saldo atual: R${float(account_balance):.2f}\n\n{color.yellow}O saldo mínimo da sua conta é $-500,00{color.normal}\n')
                        print('~' * 37)
                        sleep(4)

                        os.system('cls')
                    
                    else:

                        # Alteração do do saldo no arquivo
                        with open(f'./users/{cpf}.txt', 'w') as file:
                            file.writelines(list_filelines)
                        
                        # Caso de tudo certo, isso será executado
                        os.system('cls')
                        print('~' * 32)
                        print(f'\n{color.green} Valor Debitado com sucesso!{color.normal}')
                        print(f"\n{color.cyan}    Cobrado '3%' de taxa{color.normal}")
                        print(f'\n\033[1mSaldo atual da conta: R${float(list_filelines[3]):.2f}\n{color.normal}')
                        print('~' * 32)

                        # Armazenando os dados do Débito
                        count_negative_statement(cpf, money_amount, final_account_balance)

                        sleep(4)
                        os.system('cls')

                # Debitar da conta Plus
                elif list_filelines[0].startswith('Plu'):
                    
                    # Descontando a taxa para contas PLUS
                    tax = 0.01

                    account_balance = float(list_filelines[3])
                    new_account_balance = account_balance - money_amount
                    final_account_balance = new_account_balance - (new_account_balance * tax)

                    list_filelines[3] = str(f'{final_account_balance}\n')

                    # Restrição da conta Plus -> Mínimo == 5000
                    if float(list_filelines[3]) < -5000:
                        os.system('cls')

                        # Será executado caso a quantidade de dinheiro supere o limite
                        print('~' * 39)
                        print(f'\n{color.red}   Impossível realizar o Débito!{color.normal}\n\n     Saldo atual: R${float(account_balance):.2f}\n\n{color.yellow}O saldo mínimo da sua conta é $-5.000,00{color.normal}\n')
                        print('~' * 39)
                        sleep(4)

                        os.system('cls')
                    
                    else:

                        # Alteração do do saldo no arquivo
                        with open(f'./users/{cpf}.txt', 'w') as file:
                            file.writelines(list_filelines)
                        
                        # Caso de tudo certo, isso será executado
                        os.system('cls')
                        print('~' * 32)
                        print(f'\n{color.green} Valor Debitado com sucesso!{color.normal}')
                        print(f"\n{color.cyan}    Cobrado '1%' de taxa{color.normal}")
                        print(f'\n\033[1mSaldo atual da conta: R${float(list_filelines[3]):.2f}\n{color.normal}')
                        print('~' * 32)

                        # Armazenando os dados do Débito
                        count_negative_statement(cpf, money_amount, final_account_balance)

                        sleep(4)
                        os.system('cls')


            else:

                # Isso será executado caso a senha esteja incorreta
                print(f'\n{color.red}Senha ou CPF incorretos\n{color.normal}')
                
                sleep(3)
                os.system('cls')

        else:
            # Isso será executado caso o arquivo do usuário não seja encontrado
            print(f'\n{color.yellow}Usuário Inexistente{color.normal}\n')
            
            sleep(2)
            os.system('cls')


# DEPOSITAR
def deposit_money():
    '''
    Função responsável pelo depósito.
    Para o depóstivo precisamos apenas do cpf e da quantia de dinheiro.
    Será verificado se o arquivo de usuário existe e se o CPF é equivalente.
    O valor será adicionado na conta e por fim será exibido uma mensagem de sucesso ou erro.
    '''

    # Impedindo que ocorra um erro durante a execução do programa
    try:
        cpf = int(input('Digite o CPF da conta que deseja depositar: '))
    except:
        print(f'{color.red}\nValor inválido!{color.normal}')
        sleep(2)
        os.system('cls')
    else:

        # Verificando se o usuário existe
        if os.path.isfile(f'./users/{cpf}.txt'):

            with open(f'./users/{cpf}.txt', 'r') as file:
                list_filelines = file.readlines()
            
            # Verificando se a CPF e SENHA estão corretos
            if cpf == int(list_filelines[2]):
                
                # Quantidade de dinheiro que será depositado
                money_amount = int(input('Digite a quantidade de dinheiro: '))

                # Alterando o saldo do arquivo de usuário
                account_balance = float(list_filelines[3])
                new_account_balance = account_balance + money_amount

                list_filelines[3] = str(f'{float(new_account_balance):.2f}\n')
                
                # Atualizando o valor no arquivo do usuário
                with open(f'./users/{cpf}.txt', 'w') as file:
                    file.writelines(list_filelines)

                # Mensagem de SUCESSO
                print('~' * 37)
                print(f'\n{color.green}Depósito realizado com sucesso!{color.normal}')
                print(f'\nR${money_amount:.2f} depositado na conta {list_filelines[1]}')
                print('~' * 37)

                # Momento de realização do depósito para o Extrato
                count_positive_statement(cpf, money_amount, new_account_balance)
                
                sleep(4)

                os.system('cls')

            else:
                # Mensagem de ERRO

                print(f'\n{color.red}CPF incorreto\n{color.normal}')
                
                sleep(3)

                os.system('cls')

        else:
            # Isso será executado caso o arquivo do usuário não seja encontrado
            print(f'\n{color.yellow}Usuário Inexistente{color.normal}\n')
            
            sleep(2)

            os.system('cls')


# SALDO DA CONTA
def account_balance():
    '''
    Função responsável por mostrar o saldo da conta.
    Verificamos se a conta existe por meio do CPF e SENHA e se eles coincidem, se estiverem certo, o saldo da conta será exibido. Senão será exibida uma mensagem de erro.
    '''
    # Impedindo que ocorra um erro durante a execução do programa
    try:
        cpf = int(input('Digite o CPF da conta que deseja visualizar o saldo: '))
        password = int(input('Digite a senha da conta: '))
    except:
        print(f'{color.red}\nValor inválido!{color.normal}')
        sleep(2)
        os.system('cls')
    else:
        
        # Verificando se o arquivo existe
        if os.path.isfile(f'./users/{cpf}.txt'):

            with open(f'./users/{cpf}.txt', 'r') as file:
                list_filelines = file.readlines()

            # Verificando se a CPF e SENHA estão corretos
            if cpf == int(list_filelines[2]) and password == int(list_filelines[4]):
                print('~' * 30)
                print(f'{color.cyan}Saldo de {str(list_filelines[1])}{color.normal}\nR${float(list_filelines[3]):.2f}')
                print('~' * 30)

                sleep(4)

                os.system('cls')

            else:
                # Isso será executado caso o CPF ou senha estejam icorretos
                print(f'\n{color.red}CPF ou Senha incorretos\n{color.normal}')
                
                sleep(3)
                os.system('cls')

        else:
            # Isso será executado caso o arquivo do usuário não seja encontrado
            print(f'\n{color.yellow}Usuário Inexistente{color.normal}\n')
            
            sleep(2)
            os.system('cls')


# DADOS NEGATIVOS DOS EXTRATOS DA CONTA
def count_negative_statement(cpf, value, balance):
    '''
    Função responsável por armazenar os valores negativos das transações.
    cpf: cpf da conta que será acessada
    value: quantidade de dinheiro
    balance: saldo no momento da transação

    Utilizaremos o módulo datetime para pegar o ano e a hora
    '''
    # Pegando o ano atual
    current_year = datetime.date.today()

    # Pegando a hora atual
    now = datetime.datetime.now()
    hour, minute, sec = now.hour, now.minute, now.second

    current_time = f'{hour}:{minute}:{sec}'

    # Armazenando no arquivo de dados do usuário
    with open(f'./users_bankstatement/{cpf}.txt', 'a') as file:
        file.write(f'{current_year}\n')
        file.write(f'{current_time}\n')
        file.write(f'- {value}\n')

        # Taxa cobrada para cada tipo de conta
        if value < 10:
            with open(f'./users/{cpf}.txt', 'r') as file_user:
                user_filelines = file_user.readlines()
            
            if user_filelines[0].startswith('Sal'):

                file.write(f'0.05\n')
                balance = balance - (balance * 0.05)
                
                with open(f'./users/{cpf}.txt', 'r') as file_user:
                    filelines = file_user.readlines()

                filelines[3] = str(f'{float(balance):.2f}\n')

                with open(f'./users/{cpf}.txt', 'w') as file_user:
                    file_user.writelines(filelines)

            elif user_filelines[0].startswith('Com'):
                file.write(f'0.03\n')
                balance = balance - (balance * 0.03)
                
                with open(f'./users/{cpf}.txt', 'r') as file_user:
                    filelines = file_user.readlines()

                filelines[3] = str(f'{float(balance):.2f}\n')

                with open(f'./users/{cpf}.txt', 'w') as file_user:
                    file_user.writelines(filelines)
            
            elif user_filelines[0].startswith('Plu'):
                file.write(f'0.01\n')
                balance = balance - (balance * 0.01)
                
                with open(f'./users/{cpf}.txt', 'r') as file_user:
                    filelines = file_user.readlines()

                filelines[3] = str(f'{float(balance):.2f}\n')

                with open(f'./users/{cpf}.txt', 'w') as file_user:
                    file_user.writelines(filelines)

        else:
            file.write('0.00\n')
        file.write(f'{balance}\n')


# DADOS POSITIVOS DOS EXTRATOS DA CONTA
def count_positive_statement(cpf, value, balance): 
    '''
    Função responsável por armazenar os valores positivos das transações.
    cpf: cpf da conta que será acessada
    value: quantidade de dinheiro
    balance: saldo no momento da transação

    Utilizaremos o módulo datetime para pegar o ano e a hora
    '''  
    # Pegando o ano atual
    current_year = datetime.date.today()

    # Pegando a hora atual
    now = datetime.datetime.now()
    hour, minute, sec = now.hour, now.minute, now.second

    current_time = f'{hour}:{minute}:{sec}'

    # Armazenando as informações no arquivo de dados do usuário
    with open(f'./users_bankstatement/{cpf}.txt', 'a') as file:
        file.write(f'{current_year}\n')
        file.write(f'{current_time}\n')
        file.write(f'+ {value}\n')

        # Taxa cobrada para cada tipo de conta
        if value < 10:
            with open(f'./users/{cpf}.txt', 'r') as file_user:
                user_filelines = file_user.readlines()
            
            if user_filelines[0].startswith('Sal'):

                file.write(f'0.05\n')
                balance = balance - (balance * 0.05)
                
                with open(f'./users/{cpf}.txt', 'r') as file_user:
                    filelines = file_user.readlines()

                filelines[3] = str(f'{float(balance):.2f}\n')

                with open(f'./users/{cpf}.txt', 'w') as file_user:
                    file_user.writelines(filelines)

            elif user_filelines[0].startswith('Com'):
                file.write(f'0.03\n')
                balance = balance - (balance * 0.03)
                
                with open(f'./users/{cpf}.txt', 'r') as file_user:
                    filelines = file_user.readlines()

                filelines[3] = str(f'{float(balance):.2f}\n')

                with open(f'./users/{cpf}.txt', 'w') as file_user:
                    file_user.writelines(filelines)
            
            elif user_filelines[0].startswith('Plu'):
                file.write(f'0.01\n')
                balance = balance - (balance * 0.01)
                
                with open(f'./users/{cpf}.txt', 'r') as file_user:
                    filelines = file_user.readlines()

                filelines[3] = str(f'{float(balance):.2f}\n')

                with open(f'./users/{cpf}.txt', 'w') as file_user:
                    file_user.writelines(filelines)

        else:
            file.write('0.00\n')
        file.write(f'{balance}\n')


# EXTRATO
def account_statement():
    '''
    Função responsável pelo extrato.
    Verificaremos o CPF e SENHA para acessar a conta, se o arquivo existir e ambos estiverem corretos será mostrato o extrato, caso contrário, uma mensagem de erro será exibida.
    '''
    # Impedindo que ocorra um erro durante a execução do programa
    try:
        cpf = int(input('Digite o CPF da conta que deseja visualizar o extrato: '))
        password = int(input('Digite a senha da conta: [PIN] '))
    except:
        print(f'{color.red}\nValor inválido!{color.normal}')
        sleep(2)
        os.system('cls')
    else:
        
        # Verificando se o arquivo de usuário e de dados existe
        if os.path.isfile(f'./users/{cpf}.txt') and os.path.isfile(f'./users_bankstatement/{cpf}.txt'):
            
            # Acessando arquivo de usuário
            with open(f'./users/{cpf}.txt', 'r') as file:
                list_filelines = file.readlines()

            # Verificando se a CPF e SENHA estão corretos
            if cpf == int(list_filelines[2]) and password == int(list_filelines[4]):
                
                # Acessando arquivo de dados do usuário
                with open(f'./users_bankstatement/{cpf}.txt', 'r') as file_data:
                    list_filelines_data = file_data.read().splitlines()

                # Variável para a exibição do título
                name = str(list_filelines[1])
                cpf_title = str(list_filelines[2])
                conta = str(list_filelines[0])

                # Título do extrato
                print(f'\nNome:  {name}', end='')
                print(f'CPF:   {cpf_title}', end='')

                # Cor para cada tipo de conta
                if conta.startswith('Sal'):
                    print(f'Conta: {color.magenta}{conta}{color.normal}', end='')
                elif conta.startswith('Com'):
                    print(f'Conta: {color.yellow}{conta}{color.normal}', end='')
                elif conta.startswith('Plu'):
                    print(f'Conta: {color.green}{conta}{color.normal}', end='')
                print('-' * 85)
                
                # Um loop que percorre os elementos do arquivo de dados e exibe o extrato
                # Vai indo de 5 em 5 até o útlimo elemento
                cont = 0
                for data in range(len(list_filelines_data)):

                    while cont < len(list_filelines_data):
                        print(f'{color.cyan}Data:{color.normal} {list_filelines_data[cont]:<12}  {list_filelines_data[cont+1]:<10}  {list_filelines_data[cont+2]:<10}    {color.cyan}Tarifa:{color.normal} {list_filelines_data[cont+3]:<10}    {color.cyan}Saldo:{color.normal} {float(list_filelines_data[cont+4]):<10.2f}\n')
                        cont += 5
                print('-' * 85)
                
                sleep(10)

                os.system('cls')
                
            else:
                # Isso será executado caso o CPF ou senha estejam icorretos
                print(f'\n{color.red}CPF ou Senha incorretos\n{color.normal}')
                
                sleep(3)

                os.system('cls')

        else:
            # Isso será executado caso o arquivo do usuário não seja encontrado
            print(f'\n{color.yellow}Usuário Inexistente{color.normal}\n')
            
            sleep(2)

            os.system('cls')


# INFORMAÇÕES SOBRE AS FUNÇÕES
print(help(new_user))
print(help(delete_user))
print(help(debit_payment))
print(help(deposit_money))
print(help(account_balance))
print(help(count_negative_statement))
print(help(count_positive_statement))
print(help(account_statement))
