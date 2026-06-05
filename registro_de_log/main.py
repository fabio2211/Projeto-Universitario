import datetime

def salvar_historico_log(texto, nivel='INFO', arquivo_destino='app.log'):
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formato_log = f"[{data_hora}] [{nivel}] - {texto}\n"
    with open(arquivo_destino, 'a', encoding='utf-8') as arquivo:
        arquivo.write(formato_log)

salvar_historico_log("Sistema inicializado com sucesso.", "INFO")
salvar_historico_log("Tentativa de acesso não autorizada.", "WARNING")
salvar_historico_log("Erro crítico ao conectar ao servidor.", "ERROR")

print("Histórico atualizado no arquivo 'app.log'.")