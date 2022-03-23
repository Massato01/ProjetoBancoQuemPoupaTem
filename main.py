# Projeto - Banco QuemPoupaTem

# Bibliotecas
from time import sleep
import os

# Módulos
import functions


# [ TODAS AS FUNÇÕES QUE SERÃO UTILIZADAS ESTÃO EM functions ]

def main():
    # MENU INICIAL DO BANCO
    os.system('cls')

    # O programa fica rodando até que o usuário digite "0"
    while True:
        functions.print_menu(f'{functions.color.green}Banco QuemPoupaTem{functions.color.normal}')

        # Escolha de opção
        while True:
            try:
                user_option = int(input('\nEscolha uma das opções: '))
            except:
                print(f'{functions.color.red}\nValor inválido!{functions.color.normal}')
            else:

                # Restrição para que não ocorra um erro durante a execução
                if user_option < 0 or user_option > 6:
                    print(f'{functions.color.red}\nOpção inválida!{functions.color.black}')
                    sleep(2)
                break
        
        # Finalização do programa
        if user_option == 0:
            os.system('cls')
            print('\n')
            print(functions.color.green)
            print('~' * 25)
            print(f'{functions.color.normal}QuemPoupaTem{functions.color.green}'.center(33, '~'))
            print('~' * 25)
            print(f'{functions.color.cyan}ATÉ MAIS!{functions.color.green}'.center(35, '~'))
            print(f'{functions.color.cyan}VOLTE SEMPRE!{functions.color.green}'.center(35, '~'))
            print('~' * 25)
            print(functions.color.black)
            sleep(3)
            os.system('cls')
            break

        # Execução da função `new_user()`
        elif user_option == 1:

            # Opção de mostrar ou não os tipos de conta
            while True:
                see_account_types = str(input('Deseja ver os tipos de conta disponíveis? [S/N] ')).strip().upper()[0]

                # Restrição para o usuário responder apenas com "S" ou "N"
                if see_account_types in 'SN':
                    break
                print('[ERRO] Por favor, digite S ou N')
            
            # Mostra os tipos de conta
            if see_account_types == 'S':
                functions.account_types()
            
            # Executa a função para criar um novo usuário
            functions.new_user()

        # Execução da função `delete_user()`
        elif user_option == 2:

            # Executa a função para deletar um usuário
            functions.delete_user()

        # Execução da função `debit_payment`
        elif user_option == 3:

            # Executa a função para realizar o débito
            functions.debit_payment()
        
        # Execução da função `deposit_money()`
        elif user_option == 4:

            # Executa a função para depósito
            functions.deposit_money()

        # Execução da função `account_balance()`
        elif user_option == 5:

            # Executa a função para ver o saldo
            functions.account_balance()

        # Execução da função `account_statement()`
        elif user_option == 6:

            # Executa a função para ver o extrato
            functions.account_statement()


if __name__ == '__main__':
    main()
