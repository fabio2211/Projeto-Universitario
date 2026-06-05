def converter(temperatura):

    # Verifica se o texto termina com a letra 'C' (indica que está em Celsius)
    if temperatura.endswith('C'):
        # Pega o texto ignorando o último caractere (a letra 'C') e converte o número para float
        celsius = float(temperatura[:-1])
        # Aplica a fórmula matemática para converter Celsius em Fahrenheit
        fahrenheit = (celsius * 1.8) + 32

        print(f"{celsius}°C é igual a {fahrenheit}°F")

    # Verifica se o texto termina com a letra 'F' (indica que está em Fahrenheit)
    elif temperatura.endswith('F'):
        # Pega o texto ignorando o último caractere (a letra 'F') e converte para float
        fahrenheit = float(temperatura[:-1])
        # Aplica a fórmula matemática para converter Fahrenheit em Celsius
        celsius = (fahrenheit - 32) / 1.8

        print(f"{fahrenheit}°F é igual a {celsius}°C")