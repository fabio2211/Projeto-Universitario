import datetime

def salvar_historico_log(texto, nivel='INFO', arquivo_destino='app.log'):
    # Captura a data e hora atual do sistema e formata como "Ano-Mês-Dia Hora:Minuto:Segundo"
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Monta a string padronizada do log combinando o timestamp, a gravidade e a mensagem
    formato_log = f"[{data_hora}] [{nivel}] - {texto}\n"
    
    # Abre o arquivo no modo 'a' (append/anexar). Esse modo é crucial porque ele 
    # adiciona o novo texto no final do arquivo sem apagar os logs antigos.
    with open(arquivo_destino, 'a', encoding='utf-8') as arquivo:
        arquivo.write(formato_log)

# --- TESTES DE GRAVAÇÃO DO LOG ---

# Registra uma mensagem padrão de sucesso no fluxo do app
salvar_historico_log("Sistema inicializado com sucesso.", "INFO")

# Registra um alerta que requer atenção, mas não trava o sistema
salvar_historico_log("Tentativa de acesso não autorizada.", "WARNING")

# Registra uma falha grave que interrompeu alguma funcionalidade
salvar_historico_log("Erro crítico ao conectar ao servidor.", "ERROR")

print("Histórico atualizado no arquivo 'app.log'.")