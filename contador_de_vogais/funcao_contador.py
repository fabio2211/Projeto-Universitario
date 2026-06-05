def contar_vogais(texto): 
    # Inicializa o acumulador que vai guardar o total de vogais encontradas
    contador = 0
    
    # Define uma string com todas as vogais, incluindo maiúsculas para não deixar passar nenhuma
    vogais = 'aeiouAEIOU'
    
    # Percorre o texto caractere por caractere
    for letra in texto:
        # Verifica se o caractere atual faz parte da lista de vogais válidas
        if letra in vogais:
            contador += 1  # Se for uma vogal, incrementa o contador
            
    # Retorna o total acumulado após checar todo o texto
    return contador