def funcao_fatorial(n):
    if n == 0 or n ==1:
        return 1
    elif n > 1:
        return n * funcao_fatorial(n-1)
    else:
        return "Fatorial não definido para números negativos"