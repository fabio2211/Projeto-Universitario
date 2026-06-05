# Importa a função criada e salva no arquivo 'funcao_contador.py' para reutilizar o código
from funcao_contador import contar_vogais

# Recebe a string que o usuário quer analisar
frase = (input("Digite uma frase ou texto: "))

# Passa a frase como argumento para a função importada e guarda o retorno no 'resultado'
resultado = contar_vogais(frase)

# Exibe o total de vogais usando uma f-string para formatar o texto bonitinho
print(f"O número de vogais na frase é: {resultado}")