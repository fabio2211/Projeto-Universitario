from funcao_converter import converter

opcao = input("Escolha uma opção de conversão:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\n")

if opcao == '1':
    temperatura = input("Digite a temperatura em Celsius (ex: 25C): ")
    converter(temperatura)
elif opcao == '2':
    temperatura = input("Digite a temperatura em Fahrenheit (ex: 77F): ")
    converter(temperatura)