import pandas as pd

try:
    # Carrega a base de dados dos clientes a partir do arquivo CSV
    dados_clientes = pd.read_csv('dados_clientes.csv')

    # Exibe a tabela completa (ou o resumo que o Pandas gera se for muito grande)
    print("\n=== RESUMO DO BANCO DE DADOS ===")
    print(dados_clientes)

    # Calcula as médias aritméticas das colunas numéricas 'Idade' e 'Renda'
    idade_media = dados_clientes['Idade'].mean()
    faturamento_medio = dados_clientes['Renda'].mean()

    print(f"\nIdade média dos cadastrados: {idade_media:.1f} anos")
    print(f"Renda média mensal: R$ {faturamento_medio:.2f}")

    # Usa a moda (.mode()) para descobrir a cidade que mais se repete na coluna
    # O '[0]' serve para pegar o primeiro resultado caso haja empate de cidades
    local_com_mais_frequencia = dados_clientes['Cidade'].mode()[0]
    print(f"Localidade com maior volume: {local_com_mais_frequencia}")

    # Pede um valor de filtro para o usuário e converte para número decimal (float)
    corte_salarial = float(input("\nFiltrar renda maior que: "))
    
    # Aplica o filtro no DataFrame: traz apenas as linhas onde a renda supera o valor digitado
    publico_alvo = dados_clientes[dados_clientes['Renda'] > corte_salarial]

    # Mostra na tela a nova tabela filtrada com o público-alvo
    print(f"\nExibindo clientes com ganhos acima de R$ {corte_salarial}:")
    print(publico_alvo)

# Tratamento de exceções para capturar erros comuns na manipulação de dados
except FileNotFoundError:
    # Caso o arquivo CSV não esteja na mesma pasta do script ou tenha sido renomeado
    print("Aviso: A base de dados 'dados_clientes.csv' não foi encontrada.")
except KeyError as coluna_erro:
    # Acontece se o CSV estiver sem as colunas 'Idade', 'Renda' ou 'Cidade' (letras maiúsculas importam!)
    print(f"Erro: A coluna {coluna_erro} não existe no arquivo.")
except Exception as falha:
    # Qualquer outro erro inesperado (como o usuário digitar letras no input numérico da renda)
    print(f"Erro crítico detectado: {falha}")