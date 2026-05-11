lista_contatos = []
while True:
    print("1-Adicionar | 2-Buscar | 3-Listar | 4-Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input(" Digite o telefone do contato:")
        email = input("Digite o email do contato: ")

        contato = {"nome": nome, "telefone": telefone, "email": email}
        lista_contatos.append(contato)

    elif opcao == "2":
        nome = input("Digite o nome do contato a ser buscado: ")
        contato_encontrado = None
        for contato in lista_contatos:
            if contato["nome"] == nome:
                contato_encontrado = contato
                print("Contato encontrado")
                print("Nome: " + contato["nome"])
                print("Telefone: " + contato["telefone"])
                print("Email: " + contato["email"])
                break
        if contato_encontrado is None:
            print("Contato não encontrado.")

    elif opcao == "3":
        print("Lista de contatos:")
        for contato in lista_contatos:
            print("Nome: " + contato["nome"])
            print("Telefone: " + contato["telefone"])
            print("Email: " + contato["email"])
            print("-" * 20)

    elif opcao == "4":
        print("Saindo do programa.")
        break                