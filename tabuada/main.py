# Pede o número para o usuário e converte para inteiro (int), já que a tabuada padrão usa números inteiros
num = int(input("Digite um número inteiro para ver a tabuada: "))

# Cria um laço que vai repetir 10 vezes. 
# O range(1, 11) começa no 1 e para antes de chegar no 11 (ou seja, vai de 1 até 10)
for i in range(1, 11):
    # Multiplica o número escolhido pelo multiplicador atual da volta do laço (i)
    resultado = num * i
    
    # Exibe a linha da tabuada formatada bonitinha (ex: 5 x 1 = 5)
    print(f"{num} x {i} = {resultado}")