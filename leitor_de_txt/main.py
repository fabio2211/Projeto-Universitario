def exibir_conteudo_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = arquivo.read()
            print("\n=== CONTEÚDO DO ARQUIVO ===")
            print(dados)
    except FileNotFoundError:
        print(f"Aviso: O arquivo '{caminho_arquivo}' não foi localizado.")
    except Exception as erro:
        print(f"Falha ao abrir o arquivo: {erro}")

arquivo_usuario = input("Informe o nome ou caminho do arquivo: ")
exibir_conteudo_arquivo(arquivo_usuario)