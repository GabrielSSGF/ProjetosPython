import sys
import clipboard
import json

DADOS_SALVOS = "clipboard.json"

def salva_dados(filepath, dados):
    with open(filepath, "w") as f:
        json.dump(dados, f)


def carrega_dados(filepath):
    try:
        with open(filepath, "r") as f:
            dados = json.load(f)
            return dados
    except:
        return {}


if len(sys.argv) == 2:
    comando = sys.argv[1]
    dados = carrega_dados(DADOS_SALVOS)
    if comando == "salvar":
        chave = input("Entre a chave: ")
        dados[chave] = clipboard.paste()
        salva_dados(DADOS_SALVOS, dados)
        print("Dados salvos!")
    elif comando == "carregar":
        chave = input("Entre a chave: ")
        if chave in dados:
            clipboard.copy(dados[chave])
            print("Dados copiados para o clipboard.")
        else:
            print("chave não existe.")
    elif comando == "lista":
        print(dados)
    else:
        print("Comando desconhecido")
else:
    print("Por favor, insira apenas um comando.")