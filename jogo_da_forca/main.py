import random

class PartidaDaForca:
    def __init__(self, lista_de_opcoes):
        self.lista_de_opcoes = lista_de_opcoes
        # Método interno para sortear a palavra assim que o jogo começa
        self.palavra_alvo = self._sortear_termo()
        self.acertos = []
        self.erros = []
        # O jogador começa com 6 vidas (uma para cada parte do boneco)
        self.chances_que_restam = 6 
        
        # Array com os desenhos em texto representando a evolução do boneco na forca
        self.design_da_forca = [
             """
  +---+
  |   |
      |
      |
      |
      = """,
             """
  +---+
  |   |
  O   |
      |
      |
      = """,
             """
  +---+
  |   |
  O   |
  |   |
      |
      = """,
             """
  +---+
  |   |
  O   |
 /|   |
      |
      = """,
             """
  +---+
  |   |
  O   |
 /|\\  |
      |
      = """,
             """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      = """,
             """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      = """
        ]

    # Escolhe uma palavra aleatória da lista e joga tudo para maiúsculo para evitar bug
    def _sortear_termo(self):
        return random.choice(self.lista_de_opcoes).upper()

    # Monta a palavra na tela colocando a letra se o usuário acertou ou "_" se ainda não descobriu
    def _revelar_letras(self):
        texto_visual = ""
        for caractere in self.palavra_alvo:
            if caractere in self.acertos:
                texto_visual += caractere + " "
            else:
                texto_visual += "_ "
        return texto_visual.strip()

    # Faz o cálculo matemático para printar o desenho certo do boneco com base nas vidas que restam
    def _renderizar_boneco(self):
        print(self.design_da_forca[6 - self.chances_que_restam])

    # Método principal que roda o loop do jogo enquanto o usuário tiver vidas
    def iniciar_rodada(self):
        print("\n===== DESAFIO DA FORCA =====")
        print("Tente adivinhar o termo oculto!")
        
        while self.chances_que_restam > 0:
            self._renderizar_boneco()
            print(f"Palavra atual: {self._revelar_letras()}")
            print(f"Letras descartadas: {', '.join(self.erros)}")
            print(f"Vidas restantes: {self.chances_que_restam}")
            
            # Pega o input do usuário e padroniza para maiúsculo
            palpite = input("Escolha uma letra: ").upper()
            
            # Validação para garantir que o usuário só digitou uma única letra válida
            if len(palpite) != 1 or not palpite.isalpha():
                print("\n-> Entrada inválida! Digite apenas uma letra (A-Z).")
                continue
                
            # Tratamento para o caso do usuário repetir uma letra que já jogou
            if palpite in self.acertos or palpite in self.erros:
                print(f"\n-> Você já tentou a letra '{palpite}' antes!")
                continue
                
            # Se acertar, adiciona na lista de acertos
            if palpite in self.palavra_alvo:
                self.acertos.append(palpite)
                print(f"\n[Boa!] A letra '{palpite}' faz parte da palavra.")
            # Se errar, vai para a lista de erros e perde uma vida
            else:
                self.erros.append(palpite)
                self.chances_que_restam -= 1
                print(f"\n[Erro!] A palavra não tem a letra '{palpite}'.")
                
            # Se não houver mais nenhum "_" na palavra mascarada, significa que o usuário ganhou
            if "_" not in self._revelar_letras():
                print("\n======================================")
                print("🏆 PARABÉNS! Você desvendou o mistério!")
                print(f"A palavra era: {self.palavra_alvo}")
                print("======================================")
                self._renderizar_boneco()
                break
        else:
            # Caso o loop acabe porque as vidas chegaram a zero
            self._renderizar_boneco()
            print("\n======================================")
            print("💀 GAME OVER! Suas chances acabaram.")
            print(f"A palavra secreta era: {self.palavra_alvo}")
            print("======================================")

# --- INICIALIZAÇÃO DO JOGO ---
# Banco de dados de palavras do jogo
banco_palavras = ["PYTHON", "LOGICA", "VENDAS", "DESENVOLVEDOR", "FLUTTER", "ROBOTICA"]

# Instanciando a classe e dando o start no jogo
nova_partida = PartidaDaForca(banco_palavras)
nova_partida.iniciar_rodada()