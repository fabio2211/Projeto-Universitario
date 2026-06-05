# Classe que cuida das contas individuais e suas operações matemáticas
class CaixaEletronico:
    def __init__(self, cod_conta, nome_dono, grana_inicial=0):
        self.cod_conta = cod_conta
        self.nome_dono = nome_dono
        self.saldo_atual = grana_inicial

    # Método para colocar dinheiro na conta
    def por_dinheiro(self, quantia):
        if quantia > 0:
            self.saldo_atual += quantia
            print(f"Depósito de R$ {quantia:.2f} feito. Saldo novo: R$ {self.saldo_atual:.2f}")
        else:
            print("Erro: Não dá para depositar valores negativos ou zero.")

    # Método para retirar dinheiro, testando se o usuário tem saldo
    def tirar_dinheiro(self, quantia):
        if quantia > 0 and self.saldo_atual >= quantia:
            self.saldo_atual -= quantia
            print(f"Saque de R$ {quantia:.2f} feito. Saldo novo: R$ {self.saldo_atual:.2f}")
            return True
        elif quantia > self.saldo_atual:
            print("Erro: Você não tem saldo suficiente para esse saque.")
            return False
        else:
            print("Erro: Valor digitado para saque é inválido.")
            return False

    # Mostra na tela o quanto o usuário tem no momento
    def checar_extrato(self):
        print(f"Saldo atual na conta {self.cod_conta}: R$ {self.saldo_atual:.2f}")
        return self.saldo_atual


# Classe para cadastrar as pessoas e guardar as contas delas numa lista
class Usuario:
    def __init__(self, nome_completo, documento_cpf):
        self.nome_completo = nome_completo
        self.documento_cpf = documento_cpf
        self.minhas_contas = [] # Array/Lista que vai guardar os objetos de contas criados

    # Vincula uma conta criada diretamente ao perfil desse usuário
    def vincular_nova_conta(self, conta_criada):
        self.minhas_contas.append(conta_criada)
        print(f"Conta {conta_criada.cod_conta} vinculada ao usuário {self.nome_completo}.")

    # Varre a lista de contas do usuário e printa as informações de cada uma
    def mostrar_todas_contas(self):
        if self.minhas_contas:
            print(f"\nContas ativas de {self.nome_completo}:")
            for item in self.minhas_contas:
                print(f"  ID Conta: {item.cod_conta} | Saldo: R$ {item.saldo_atual:.2f}")
        else:
            print(f"O usuário {self.nome_completo} ainda não abriu nenhuma conta.")


# Classe central que gerencia todos os usuários e faz buscas no sistema
class SistemaBancario:
    def __init__(self, nome_da_instituicao):
        self.nome_da_instituicao = nome_da_instituicao
        self.lista_clientes = [] # Guarda todos os objetos do tipo Usuario

    # Registra um novo cliente no banco de dados geral
    def registrar_cliente(self, novo_usuario):
        self.lista_clientes.append(novo_usuario)
        print(f"Usuário {novo_usuario.nome_completo} registrado no {self.nome_da_instituicao}.")

    # Percorre os clientes cadastrados comparando o CPF até achar o correto
    def localizar_por_cpf(self, cpf_busca):
        for pessoa in self.lista_clientes:
            if pessoa.documento_cpf == cpf_busca:
                return pessoa
        return None

    # Entra em cada cliente, entra na lista de contas dele e busca pelo número digitado
    def localizar_conta_por_numero(self, numero_busca):
        for pessoa in self.lista_clientes:
            for conta_ativa in pessoa.minhas_contas:
                if conta_ativa.cod_conta == numero_busca:
                    return conta_ativa
        return None


# --- AREA DE TESTE DO SISTEMA ---
# Criando a estrutura do banco principal
banco_vanguarda = SistemaBancario("Banco Vanguarda S.A.")

# Criando dados da primeira cliente e suas respectivas contas
maria = Usuario("Maria Silva", "123.456.789-00")
conta_corrente_maria = CaixaEletronico("001-X", "Maria Silva", 1000)
conta_poupanca_maria = CaixaEletronico("002-Y", "Maria Silva", 500)

# Vinculando as contas à Maria e colocando ela no banco
maria.vincular_nova_conta(conta_corrente_maria)
maria.vincular_nova_conta(conta_poupanca_maria)
banco_vanguarda.registrar_cliente(maria)

# Criando dados do segundo cliente
joao = Usuario("João Souza", "987.654.321-00")
conta_unica_joao = CaixaEletronico("003-Z", "João Souza", 2000)

joao.vincular_nova_conta(conta_unica_joao)
banco_vanguarda.registrar_cliente(joao)

# Rodando testes de operações na tela
maria.mostrar_todas_contas()
conta_corrente_maria.por_dinheiro(200)
conta_corrente_maria.tirar_dinheiro(300)
conta_corrente_maria.checar_extrato()

# Testando os mecanismos de busca do sistema
localizado_cliente = banco_vanguarda.localizar_por_cpf("123.456.789-00")
if localizado_cliente:
    print(f"\nBusca por CPF com sucesso: {localizado_cliente.nome_completo}")

localizado_conta = banco_vanguarda.localizar_conta_por_numero("003-Z")
if localizado_conta:
    print(f"Busca por Conta com sucesso: Código {localizado_conta.cod_conta} pertence a {localizado_conta.nome_dono}")