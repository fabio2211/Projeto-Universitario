import csv

def processar_dados_vendas(caminho_csv):
    # Inicializa as variáveis para acumular o faturamento e contar os produtos
    faturamento_total = 0.0
    contagem_produtos = {}  # Dicionário no formato {'nome_do_produto': quantidade_total}

    try:
        # Abre o arquivo CSV garantindo o fechamento automático e tratando caracteres especiais (UTF-8)
        with open(caminho_csv, 'r', encoding='utf-8') as arquivo:
            # Transforma cada linha do CSV em um dicionário baseado nos nomes das colunas (cabeçalho)
            leitor_csv = csv.DictReader(arquivo)
            
            for registro in leitor_csv:
                # Extrai os dados de cada coluna da linha atual
                nome_item = registro['produto']
                qtd = int(registro['quantidade'])
                valor_unitario = float(registro['preco'])

                # Calcula o valor total da linha (qtd * preço) e soma no faturamento geral
                faturamento_total += qtd * valor_unitario
                
                # Atualiza a contagem de unidades vendidas por produto
                if nome_item in contagem_produtos:
                    contagem_produtos[nome_item] += qtd  # Se já existe no dict, soma a quantidade
                else:
                    contagem_produtos[nome_item] = qtd   # Se é a primeira vez que aparece, inicializa

            # Só gera o relatório se o dicionário não estiver vazio (evita erro caso o CSV só tenha cabeçalho)
            if contagem_produtos:
                # Descobre qual chave (produto) tem o maior valor (quantidade) associado
                item_campeao = max(contagem_produtos, key=contagem_produtos.get)
                
                # Exibe os resultados formatados na tela
                print("\n=== RELATÓRIO DE VENDAS ===")
                print(f"Faturamento Total: R$ {faturamento_total:.2f}")
                print(f"Item mais vendido: {item_campeao} ({contagem_produtos[item_campeao]} unidades)")
            else:
                print("Aviso: O arquivo está vazio ou não possui registros válidos.")

    # Bloco de tratamento de erros para deixar o script robusto e não quebrar o programa
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_csv}' não foi localizado.")
    except KeyError as erro:
        # Acontece se o CSV não tiver as colunas exatas: 'produto', 'quantidade' ou 'preco'
        print(f"Erro de formatação: A coluna {erro} é obrigatória no cabeçalho do CSV.")
    except ValueError as erro:
        # Acontece se o preço ou a quantidade não puderem ser convertidos para número (ex: texto na célula)
        print(f"Erro de digitação: Dados numéricos inválidos encontrados ({erro}).")
    except Exception as erro:
        # Captura qualquer outro erro inesperado
        print(f"Ocorreu um imprevisto: {erro}")

# Executa a função passando o arquivo local 'vendas.csv'
processar_dados_vendas('vendas.csv')