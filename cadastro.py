import csv
import json


def cadastrarJogador():
    nome = input("Digite nome do equipamento: ")
    patrimonio = input("Digite o patrimonio: ")
    valor = input("Digite o valor: ")

    # Salvar no TXT
    arquivo = open("equipamentos.txt", "a")
    arquivo.write(nome + " " + valor + "\n")
    arquivo.close()

    # Salvar no CSV
    arquivo = open("equipamentos.csv", "a", newline="")
    escritor = csv.writer(arquivo)
    escritor.writerow([nome, patrimonio, valor])
    arquivo.close()

    # Salvar no JSON
    try:
        arquivo = open("equipamentos.json", "r", encoding="utf-8")
        equipamentos = json.load(arquivo)
        arquivo.close()
    except:
        equipamentos = []

    equipamento = {
        "nome": nome,
        "idade": patrimonio,
        "pontuacao": valor
    }

    equipamentos.append(equipamento)

    arquivo = open("equipamentos.json", "w", encoding="utf-8")
    json.dump(equipamentos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

    print("Equipamento salvo nos três arquivos!")