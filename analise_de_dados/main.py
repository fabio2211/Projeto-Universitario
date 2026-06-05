import csv

def processar_dados_vendas(caminho_csv):
    faturamento_total = 0.0
    contagem_produtos = {}

    try:
        with open(caminho_csv, 'r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            for registro in leitor_csv:
                nome_item = registro['produto']
                qtd = int(registro['quantidade'])
                valor_unitario = float(registro['preco'])

                faturamento_total += qtd * valor_unitario
                
                if nome_item in contagem_produtos:
                    contagem_produtos[nome_item] += qtd
                else:
                    contagem_produtos[nome_item] = qtd

            if contagem_produtos:
                item_campeao = max(contagem_produtos, key=contagem_produtos.get)
                print("\n=== RELATÓRIO DE VENDAS ===")
                print(f"Faturamento Total: R$ {faturamento_total:.2f}")
                print(f"Item mais vendido: {item_campeao} ({contagem_produtos[item_campeao]} unidades)")
            else:
                print("Aviso: O arquivo está vazio ou não possui registros válidos.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_csv}' não foi localizado.")
    except KeyError as erro:
        print(f"Erro de formatação: A coluna {erro} é obrigatória no cabeçalho do CSV.")
    except ValueError as erro:
        print(f"Erro de digitação: Dados numéricos inválidos encontrados ({erro}).")
    except Exception as erro:
        print(f"Ocorreu um imprevisto: {erro}")

processar_dados_vendas('vendas.csv')