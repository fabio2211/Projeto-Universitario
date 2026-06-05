import pandas as pd
import matplotlib.pyplot as plt

# Montei um dicionário com os dados dos clientes para alimentar o DataFrame
informacoes = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gustavo'],
    'Idade': [28, 35, 22, 40, 30, 25, 33],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Rio de Janeiro', 'São Paulo', 'Curitiba'],
    'Renda': [5000.00, 7500.00, 3000.00, 9000.00, 6000.00, 4500.00, 8000.00]
}
# Transformando o dicionário em uma tabela do Pandas para conseguir mexer nos dados
tabela_clientes = pd.DataFrame(informacoes)

# --- PRIMEIRO GRÁFICO: CLIENTES POR CIDADE ---
# Definindo o tamanho da janela do gráfico de barras
plt.figure(figsize=(8, 5))

# Contando quantas vezes cada cidade aparece e plotando o gráfico em formato de barra
tabela_clientes['Cidade'].value_counts().plot(kind='bar', color='seagreen')

# Customizando o gráfico com títulos, nomes nos eixos e rotacionando os nomes das cidades
plt.title('Quantidade de Clientes por Município')
plt.xlabel('Municípios')
plt.ylabel('Total de Clientes')
plt.xticks(rotation=30)

# Adicionando uma linha de grade pontilhada no fundo para ajudar a ler os valores
plt.grid(axis='y', linestyle=':')
plt.tight_layout() # Ajusta as margens para o texto não cortar

# Salvando o resultado como imagem na mesma pasta do código e exibindo na tela
plt.savefig('grafico_clientes_cidade.png')
plt.show()


# --- SEGUNDO GRÁFICO: DISTRIBUIÇÃO DE IDADES ---
# Abrindo uma nova janela para desenhar o histograma
plt.figure(figsize=(8, 5))

# Criando o histograma de idades dividido em 5 blocos (faixas etárias)
plt.hist(tabela_clientes['Idade'], bins=5, color='darkorange', edgecolor='white')

# Colocando os títulos e nomes dos eixos para identificação
plt.title('Faixa Etária dos Clientes')
plt.xlabel('Idades')
plt.ylabel('Contagem')

# Colocando a mesma grade pontilhada e ajustando o layout
plt.grid(axis='y', linestyle=':')
plt.tight_layout()

# Exportando o segundo gráfico para imagem e mostrando o resultado
plt.savefig('grafico_idades.png')
plt.show()

print("Imagens 'grafico_clientes_cidade.png' e 'grafico_idades.png' exportadas com sucesso.")