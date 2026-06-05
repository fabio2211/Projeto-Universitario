# Importa a função de conversão que criamos no outro arquivo
from funcao_converter import converter

# Exibe o menu na tela e captura a escolha do usuário (1 ou 2)
opcao = input("Escolha uma opção de conversão:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\n")

# Se o usuário escolheu a opção 1 (Celsius -> Fahrenheit)
if opcao == '1':
    # Pede o valor lembrando o usuário de colocar o 'C' no final (necessário para a lógica da função)
    temperatura = input("Digite a temperatura em Celsius (ex: 25C): ")
    # Chama a função passando a string digitada
    converter(temperatura)

# Se o usuário escolheu a opção 2 (Fahrenheit -> Celsius)
elif opcao == '2':
    # Pede o valor lembrando o usuário de colocar o 'F' no final
    temperatura = input("Digite a temperatura em Fahrenheit (ex: 77F): ")
    # Chama a função passando a string digitada
    converter(temperatura)