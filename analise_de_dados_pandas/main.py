import pandas as pd

try:
    dados_clientes = pd.read_csv('dados_clientes.csv')

    print("\n=== RESUMO DO BANCO DE DADOS ===")
    print(dados_clientes)

    idade_media = dados_clientes['Idade'].mean()
    faturamento_medio = dados_clientes['Renda'].mean()

    print(f"\nIdade média dos cadastrados: {idade_media:.1f} anos")
    print(f"Renda média mensal: R$ {faturamento_medio:.2f}")

    local_com_mais_frequencia = dados_clientes['Cidade'].mode()[0]
    print(f"Localidade com maior volume: {local_com_mais_frequencia}")

    corte_salarial = float(input("\nFiltrar renda maior que: "))
    publico_alvo = dados_clientes[dados_clientes['Renda'] > corte_salarial]

    print(f"\nExibindo clientes com ganhos acima de R$ {corte_salarial}:")
    print(publico_alvo)

except FileNotFoundError:
    print("Aviso: A base de dados 'dados_clientes.csv' não foi encontrada.")
except KeyError as coluna_erro:
    print(f"Erro: A coluna {coluna_erro} não existe no arquivo.")
except Exception as falha:
    print(f"Erro crítico detectado: {falha}")