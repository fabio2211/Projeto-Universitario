def funcao_fatorial(n):
    # Caso base: o fatorial de 0 ou 1 é sempre 1. Evita que a recursão rode para sempre.
    if n == 0 or n == 1:
        return 1
        
    # Caso recursivo: se o número for maior que 1, a função chama ela mesma 
    # diminuindo 1 do valor atual, criando o efeito de cascata (ex: 5 * 4 * 3...)
    elif n > 1:
        return n * funcao_fatorial(n - 1)
        
    # Validação de segurança: caso tentem passar um número negativo
    else:
        return "Fatorial não definido para números negativos"