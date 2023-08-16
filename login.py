import re


def verificar_forca_senha(senha):
    # Verifica se a senha atende a algumas regras básicas
    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."

    if not any(c.isdigit() for c in senha):
        return "A senha deve conter pelo menos um número."

    if not any(c.isalpha() for c in senha):
        return "A senha deve conter pelo menos uma letra."

    if not any(c.isupper() for c in senha):
        return "A senha deve conter pelo menos uma letra maiúscula."

    if not re.search("[!@#$%^&*(),.?\":{}|<>]", senha):
        return "A senha deve conter pelo menos um caractere especial."

    return "Senha forte!"


def cadastrar_usuario(database):
    usuario = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")

    if usuario in database:
        print("Usuário já cadastrado.")
    else:
        resultado = verificar_forca_senha(senha)
        if resultado == "Senha forte!":
            database[usuario] = senha
            print("Usuário cadastrado com sucesso!")
        else:
            print("Senha fraca. Tente uma senha mais forte.")


def fazer_login(database):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario in database and database[usuario] == senha:
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.")


def main():
    database = {}  # Dicionário para armazenar usuários e senhas

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar usuário")
        print("2 - Fazer login")
        print("3 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar_usuario(database)
        elif opcao == "2":
            fazer_login(database)
            if fazer_login(database):
                break
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Escolha novamente.")


if __name__ == "__main__":
    main()
