# Captura os dados do usuário. O input() sempre recebe tudo como texto (String)
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

# Converte os textos para decimal (float) antes de fazer os cálculos,
# senão o Python tentaria juntar os textos em vez de somar.
soma = float(num1) + float(num2)
subtracao = float(num1) - float(num2)
multiplicacao = float(num1) * float(num2)

# Realiza a divisão. Nota: se o usuário digitar 0 no num2, isso vai gerar um erro (ZeroDivisionError)
divisao = float(num1) / float(num2)

# Exibe os resultados de cada operação na tela
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)