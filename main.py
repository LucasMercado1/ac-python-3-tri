from cadastro import cadastrarJogador
from consultas import verRanking, buscarJogador, excluirJogador

while True:
    print("\n=== SISTEMA DE INVENTÁRIO DO LABORATÓRIO ===")
    print("1 - Cadastrar equipamento")
    print("2 - Ver histórico de logs/ocorrências")
    print("3 - Listar inventário completo e gerar relatório")
    print("4 - Buscar equipamento detalhado")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrarJogador()

    elif opcao == "2":
        verRanking()

    elif opcao == "3":
        buscarJogador()

    elif opcao == "4":
        excluirJogador()

    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")