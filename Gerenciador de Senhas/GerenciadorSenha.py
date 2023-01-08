from cryptography.fernet import Fernet

def escreve_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)


def carrega_chave():
    arquivo = open("chave.key", "rb")
    chave = arquivo.read()
    arquivo.close()
    return chave

chave = carrega_chave()
fer = Fernet(chave)

def view():
    with open('senhas.txt', 'r') as f:
        print("")
        for line in f.readlines():
            dados = line.rstrip()
            usuario, senha = dados.split("|")
            print("Usuário:", usuario, "| Senha:",
                  fer.decrypt(senha.encode()).decode())
        print("")

def add():
    nome = input('Nome da conta: ')
    palavrachave = input("Senha: ")

    with open('senhas.txt', 'a') as f:
        f.write(nome + "|" + fer.encrypt(palavrachave.encode()).decode() + "\n")

while True:
    modo = input("Você gostaria de 'adicionar' uma nova senha ou 'visualizar'" + 
                 " existentes (visualizar, adicionar)?\nCaso deseja sair, pressione 's': ").lower()
    
    if modo == "s":
        break

    if modo == "visualizar":
        view()
    elif modo == "adicionar":
        add()
    else:
        print("Modo inválido.")
        continue