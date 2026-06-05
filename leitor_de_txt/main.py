def exibir_conteudo_arquivo(caminho_arquivo):
    try:
        # O 'with' garante que o arquivo seja fechado automaticamente pelo Python,
        # mesmo se der algum erro durante a leitura. O 'r' indica modo de leitura (read).
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            # Lê todo o texto do arquivo de uma vez e joga na variável 'dados'
            dados = arquivo.read()
            print("\n=== CONTEÚDO DO ARQUIVO ===")
            print(dados)
            
    # Tratamento de exceções específico para manipulação de arquivos
    except FileNotFoundError:
        # Disparado se o arquivo não existir na pasta ou se o nome for digitado errado
        print(f"Aviso: O arquivo '{caminho_arquivo}' não foi localizado.")
    except Exception as erro:
        # Captura qualquer outro problema (como falta de permissão para ler o arquivo)
        print(f"Falha ao abrir o arquivo: {erro}")

# --- EXECUÇÃO DO SCRIPT ---

# Pede para o usuário digitar o nome do arquivo (ex: 'notas.txt') ou o caminho dele
arquivo_usuario = input("Informe o nome ou caminho do arquivo: ")

# Passa o nome digitado para a função que vai tentar abrir e mostrar o conteúdo
exibir_conteudo_arquivo(arquivo_usuario)