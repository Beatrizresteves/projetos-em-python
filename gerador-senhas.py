from random import choice
import string

tamanho_senha = int(
    input("Informe a quantidade de caracteres que você quer na sua senha: "))

senha = ""
caractere = string.ascii_letters + string.digits + \
    string.punctuation + string.ascii_lowercase + string.ascii_uppercase
for i in range(tamanho_senha):
    senha += choice(caractere)
print(f"A sua senha segura é {senha}")
