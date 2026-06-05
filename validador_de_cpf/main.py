def checar_validade_cpf(num_cpf):
    num_cpf = ''.join(caractere for caractere in num_cpf if caractere.isdigit())

    if len(num_cpf) != 11 or num_cpf == num_cpf[0] * 11:
        return False

    total_primeiro = sum(int(num_cpf[i]) * (10 - i) for i in range(9))
    resto_primeiro = total_primeiro % 11
    verificador_1 = 0 if resto_primeiro < 2 else 11 - resto_primeiro

    if verificador_1 != int(num_cpf[9]):
        return False

    total_segundo = sum(int(num_cpf[i]) * (11 - i) for i in range(10))
    resto_segundo = total_segundo % 11
    verificador_2 = 0 if resto_segundo < 2 else 11 - resto_segundo

    return verificador_2 == int(num_cpf[10])

entrada_usuario = input("Informe o CPF para verificação: ")
if checar_validade_cpf(entrada_usuario):
    print(f"Resultado: O documento {entrada_usuario} é válido.")
else:
    print(f"Resultado: O documento {entrada_usuario} é inválido.")