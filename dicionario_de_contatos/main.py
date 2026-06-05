# Inicializa a lista vazia que vai armazenar todos os dicionários de contatos
lista_contatos = []

# Cria um laço infinito para manter o menu rodando até que o usuário decida sair (opção 4)
while True:
    print("1-Adicionar | 2-Buscar | 3-Listar | 4-Sair")
    opcao = input("Escolha uma opção: ")
    
    # --- OPÇÃO 1: CADASTRO DE CONTATO ---
    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input(" Digite o telefone do contato:")
        email = input("Digite o email do contato: ")

        # Agrupa os dados capturados em um dicionário (estrutura de chave e valor)
        contato = {"nome": nome, "telefone": telefone, "email": email}
        # Adiciona esse novo dicionário no final da nossa lista principal
        lista_contatos.append(contato)

    # --- OPÇÃO 2: BUSCA DE CONTATO ---
    elif opcao == "2":
        nome = input("Digite o nome do contato a ser buscado: ")
        contato_encontrado = None # Flag/sinalizador para sabermos se o contato existe ou não
        
        # Percorre a lista de contatos verificando um por um
        for contato in lista_contatos:
            # Se o nome no dicionário for igual ao nome digitado pelo usuário
            if contato["nome"] == nome:
                contato_encontrado = contato
                print("Contato encontrado")
                print("Nome: " + contato["nome"])
                print("Telefone: " + contato["telefone"])
                print("Email: " + contato["email"])
                break # Para o laço for imediatamente, pois já achou o contato
                
        # Se após o loop a flag continuar vazia (None), significa que o contato não existe na lista
        if contato_encontrado is None:
            print("Contato não encontrado.")

    # --- OPÇÃO 3: EXIBIR TODOS OS CONTATOS ---
    elif opcao == "3":
        print("Lista de contatos:")
        # Passa por cada dicionário dentro da lista e exibe suas informações formatadas
        for contato in lista_contatos:
            print("Nome: " + contato["nome"])
            print("Telefone: " + contato["telefone"])
            print("Email: " + contato["email"])
            print("-" * 20) # Cria uma linha divisória para separar visualmente os contatos

    # --- OPÇÃO 4: FECHAR O PROGRAMA ---
    elif opcao == "4":
        print("Saindo do programa.")
        break # Quebra o laço 'while True', encerrando a execução do script