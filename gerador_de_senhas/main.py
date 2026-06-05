import random
import string

def criar_senha_aleatoria(comprimento, usar_maiusculas=True, usar_minusculas=True, usar_digitos=True, usar_simbolos=True):
    opcoes = ''
    
    # Vai montando o "banco de caracteres" disponíveis com base nas escolhas do usuário
    if usar_maiusculas:
        opcoes += string.ascii_uppercase  # Adiciona 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if usar_minusculas:
        opcoes += string.ascii_lowercase  # Adiciona 'abcdefghijklmnopqrstuvwxyz'
    if usar_digitos:
        opcoes += string.digits           # Adiciona '0123456789'
    if usar_simbolos:
        opcoes += string.punctuation      # Adiciona os caracteres especiais (ex: !, @, #, $)

    # Validação: se o usuário disser 'não' para todas as opções, o banco fica vazio
    if not opcoes:
        return "Aviso: Selecione ao menos um tipo de caractere."

    # Sorteia caracteres aleatórios do nosso banco 'opcoes' repetindo a quantidade de vezes pedida (comprimento)
    # O .join() junta todas as letras sorteadas em uma string única
    resultado = ''.join(random.choice(opcoes) for _ in range(comprimento))
    return resultado

# --- INTERFACE COM O USUÁRIO ---

# Pede o tamanho desejado para a senha
tamanho_senha = int(input("Digite a quantidade de caracteres para a senha: "))

# Recebe as respostas, limpa espaços vazios (.strip()), transforma em minúsculo (.lower()) 
# e gera um valor Booleano (True/False) direto comparando se é igual a 's'
abc_maior = input("Trazer letras maiúsculas? (s/n): ").strip().lower() == 's'
abc_menor = input("Trazer letras minúsculas? (s/n): ").strip().lower() == 's'
com_numeros = input("Trazer números? (s/n): ").strip().lower() == 's'
com_especiais = input("Trazer caracteres especiais? (s/n): ").strip().lower() == 's'

# Chama a função passando as configurações escolhidas
nova_senha = criar_senha_aleatoria(tamanho_senha, abc_maior, abc_menor, com_numeros, com_especiais)
print(f"Sua senha é: {nova_senha}")