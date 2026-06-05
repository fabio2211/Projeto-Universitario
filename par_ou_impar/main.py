# Captura a entrada do usuário como texto (String)
num = input("Digite um número inteiro: ")

# Converte o texto para número inteiro e usa o operador '%' (módulo) para pegar o resto da divisão por 2.
# Se o resto for igual a 0, significa que o número é divisível por 2, logo, ele é PAR.
if int(num) % 2 == 0:
    print(f"O número {num} é par.")

# Se o resto for qualquer coisa diferente de 0 (no caso de inteiros, sobra 1), o número é ÍMPAR.
else: 
    print(f"O número {num} é ímpar.")