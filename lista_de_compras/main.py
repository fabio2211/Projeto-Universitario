# Inicializa uma lista vazia que vai guardar os itens de compras do usuário
compras = []

# Cria um laço de repetição infinito para manter o menu ativo até que a opção 4 seja escolhida
while True:
    print("1-Adicionar | 2-Remover | 3-Vizualisar | 4-Sair")
    opcao = input("Escolha uma opção: ")
    
    # --- OPÇÃO 1: ADICIONAR ITEM ---
    if opcao == "1":
        item = input("Digite o item a ser adicionado: ")
        # O .append() insere o novo item sempre no final da lista
        compras.append(item)
        
    # --- OPÇÃO 2: REMOVER ITEM ---
    elif opcao == "2":
        item = input("Digite o item a ser removido: ")
        # Validação crucial: verifica se o item realmente existe na lista antes de tentar apagar
        if item in compras:
            # Se existir, remove a primeira ocorrência desse item na lista
            compras.remove(item)
        else:
            # Evita que o programa quebre com um erro de ValueError caso o item não exista
            print("Desculpe, o item não está na lista.")
            
    # --- OPÇÃO 3: VISUALIZAR A LISTA ---
    elif opcao == "3":
        print("Lista de compras:")
        # Passa por cada elemento da lista e exibe na tela em formato de tópicos
        for item in compras:
            print("- " + item)
            
    # --- OPÇÃO 4: ENCERRAR ---
    elif opcao == "4":
        print("Saindo do programa.")
        # Interrompe o loop 'while True' e finaliza a execução do script
        break