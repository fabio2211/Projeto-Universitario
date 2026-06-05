def checar_validade_cpf(num_cpf):
    # Remove qualquer pontuação (pontos e traço) e mantém apenas os números digitados
    num_cpf = ''.join(caractere for caractere in num_cpf if caractere.isdigit())

    # Validação inicial: o CPF precisa ter 11 dígitos e não pode ter todos os números iguais (ex: 111.111.111-11)
    # Embora a matemática deles funcione, o sistema da Receita rejeita CPFs com números repetidos
    if len(num_cpf) != 11 or num_cpf == num_cpf[0] * 11:
        return False

    # --- CÁLCULO DO PRIMEIRO DÍGITO VERIFICADOR ---
    # Multiplica os 9 primeiros dígitos por pesos decrescentes de 10 a 2 e soma os resultados
    total_primeiro = sum(int(num_cpf[i]) * (10 - i) for i in range(9))
    resto_primeiro = total_primeiro % 11
    # Regra oficial: se o resto da divisão for menor que 2, o dígito é 0. Senão, faz 11 menos o resto
    verificador_1 = 0 if resto_primeiro < 2 else 11 - resto_primeiro

    # Se o dígito calculado não bater com o primeiro dígito verificador do CPF (posição 9), o CPF é inválido
    if verificador_1 != int(num_cpf[9]):
        return False

    # --- CÁLCULO DO SEGUNDO DÍGITO VERIFICADOR ---
    # Agora inclui o primeiro dígito verificado no cálculo. Os pesos passam a ser decrescentes de 11 a 2
    total_segundo = sum(int(num_cpf[i]) * (11 - i) for i in range(10))
    resto_segundo = total_segundo % 11
    # Aplica a mesma regra do resto para o segundo dígito
    verificador_2 = 0 if resto_segundo < 2 else 11 - resto_segundo

    # Retorna True se o segundo dígito calculado bater com o último dígito do CPF (posição 10), senão False
    return verificador_2 == int(num_cpf[10])

# --- INTERFACE COM O USUÁRIO ---

entrada_usuario = input("Informe o CPF para verificação: ")

# Chama a função de validação e exibe a mensagem correspondente na tela
if checar_validade_cpf(entrada_usuario):
    print(f"Resultado: O documento {entrada_usuario} é válido.")
else:
    print(f"Resultado: O documento {entrada_usuario} é inválido.")