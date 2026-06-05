# Captura as três notas do usuário e já converte direto para decimal (float),
# permitindo que o usuário digite notas quebradas como 7.5 ou 8.2
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

# Calcula a média aritmética simples. Os parênteses são obrigatórios 
# para garantir que as notas sejam somadas antes de fazer a divisão por 3
media = (nota1 + nota2 + nota3) / 3

# Exibe a média final na tela usando uma f-string
print(f"A média é: {media} ")

# --- ESTRUTURA DE DECISÃO (STATUS DO ALUNO) ---

# Se a média for maior ou igual a 7, o aluno atinge o critério de aprovação
if media >= 7:
    print("Aluno aprovado")

# Caso contrário (qualquer média menor que 7), o aluno vai para a reprovação
else:
    print("Aluno reprovado")