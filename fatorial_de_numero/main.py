# Importa a função recursiva que criamos e salvamos no arquivo 'funcao_fatorial.py'
from funcao_fatorial import funcao_fatorial

# Recebe o valor do usuário e converte para inteiro (int), já que fatorial só se aplica a números inteiros
numero = int(input("Digite um número para calcular o fatorial: "))

# Passa o número digitado como argumento para a função e armazena o retorno na variável 'resultado'
resultado = funcao_fatorial(numero)

# Exibe o resultado final formatado na tela
print(f"O fatorial de {numero} é: {resultado}")