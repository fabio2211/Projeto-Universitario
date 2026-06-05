import random
import string

def criar_senha_aleatoria(comprimento, usar_maiusculas=True, usar_minusculas=True, usar_digitos=True, usar_simbolos=True):
    opcoes = ''
    if usar_maiusculas:
        opcoes += string.ascii_uppercase
    if usar_minusculas:
        opcoes += string.ascii_lowercase
    if usar_digitos:
        opcoes += string.digits
    if usar_simbolos:
        opcoes += string.punctuation

    if not opcoes:
        return "Aviso: Selecione ao menos um tipo de caractere."

    resultado = ''.join(random.choice(opcoes) for _ in range(comprimento))
    return resultado

tamanho_senha = int(input("Digite a quantidade de caracteres para a senha: "))
abc_maior = input("Trazer letras maiúsculas? (s/n): ").strip().lower() == 's'
abc_menor = input("Trazer letras minúsculas? (s/n): ").strip().lower() == 's'
com_numeros = input("Trazer números? (s/n): ").strip().lower() == 's'
com_especiais = input("Trazer caracteres especiais? (s/n): ").strip().lower() == 's'

nova_senha = criar_senha_aleatoria(tamanho_senha, abc_maior, abc_menor, com_numeros, com_especiais)
print(f"Sua senha é: {nova_senha}")