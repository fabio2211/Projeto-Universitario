import requests
from bs4 import BeautifulSoup

def capturar_manchetes_web(link_site, arquivo_saida='manchetes.txt'):
    try:
        # Faz a requisição para tentar acessar o site enviado por parâmetro
        conexao = requests.get(link_site)
        # Se der algum erro de página não encontrada (404) ou servidor (500), ele barra aqui
        conexao.raise_for_status() 
        
        # Pega o texto bruto do HTML do site e joga no BeautifulSoup para podermos varrer as tags
        mapeamento_html = BeautifulSoup(conexao.text, 'html.parser')
        
        # Procura por todas as tags <h2> do site (que geralmente são usadas para títulos)
        elementos_titulos = mapeamento_html.find_all('h2') 
        
        # Abre o arquivo de texto para salvar as informações capturadas
        with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
            for item in elementos_titulos:
                # Limpa os espaços em branco inúteis em volta do texto da tag
                texto_limpo = item.get_text(strip=True)
                # Se a tag não estiver vazia, grava a linha no arquivo de texto
                if texto_limpo:
                    arquivo.write(texto_limpo + '\n')
                    
        print(f"Processo concluído! Os dados foram gravados no arquivo '{arquivo_saida}'.")
        
    except requests.exceptions.RequestException as erro_conexao:
        print(f"Falha de rede ou link inválido: {erro_conexao}")
    except Exception as outro_erro:
        print(f"Ocorreu um problema inesperado: {outro_erro}")

# --- Teste de Execução ---
# Para rodar, basta colocar a URL de um portal de notícias de verdade aqui embaixo:
url_alvo = "https://g1.globo.com/" 
capturar_manchetes_web(url_alvo)