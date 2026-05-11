compras = []
while True:
    print("1-Adicionar | 2-Remover | 3-Vizualisar | 4-Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        item = input("Digite o item a ser adicionado: ")
        compras.append(item)
    elif opcao == "2":
        item = input("Digite o item a ser removido: ")
        if item in compras:
            compras.remove(item)
        else:
            print("Desculpe, o item não está na lista.")
    elif opcao == "3":
        print("Lista de compras:")
        for item in compras:
            print("- " + item)
    elif opcao == "4":
        print("Saindo do programa.")
        break               
