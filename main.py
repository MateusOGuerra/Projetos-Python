def listar_produtos():

    print("\n=== LISTA DE PRODUTOS ===")
    print("1 - Notebook Dell Inspiron")
    print("2 - Mouse Logitech")
    print("3 - Teclado Redragon")
    print("4 - Mouse sem fio")
    print("5 - Estabilizador")
    print("6 - SSD Kingston 1TB")
    print("7 - Cadeira Gamer")


def endereco():
    print("\nRua Ladeira Porto Geral, 123 - São Paulo")


def horario():
    print("\nSegunda a Sexta: 08h às 20h")


def atendente():
    nome = input("Digite seu nome: ")

    with open("clientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")

    print(f"\nOlá {nome}, um atendente entrará em contato.")


def menu():

    while True:

        print("\n=== SISTEMA DE SUPORTE AO CLIENTE ===")
        print("1 - Lista de Produtos")
        print("2 - Endereço")
        print("3 - Horário de Funcionamento")
        print("4 - Falar com Atendente")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            listar_produtos()

        elif opcao == "2":
            endereco()

        elif opcao == "3":
            horario()

        elif opcao == "4":
            atendente()

        elif opcao == "5":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida!")


menu()