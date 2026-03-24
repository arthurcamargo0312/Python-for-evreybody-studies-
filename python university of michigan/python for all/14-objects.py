# 1. Definindo a Classe Mãe (O molde geral)
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        print(f"--- Personagem {self.nome} criado com 100 de vida! ---")

    def receber_dano(self, quantidade):
        self.vida = self.vida - quantidade
        print(f"{self.nome} recebeu {quantidade} de dano. Vida atual: {self.vida}")


# 2. Definindo a Classe Filha (Herança)
# O Guerreiro herda tudo do Personagem, mas tem 'escudo'
class Guerreiro(Personagem):
    def __init__(self, nome):
        # O super() chama o construtor do Personagem para configurar o nome e vida
        super().__init__(nome)
        self.escudo = 50
        print(f"{self.nome} também tem um escudo de {self.escudo}!")

    def usar_escudo(self):
        print(f"{self.nome} levantou o escudo! Defesa aumentada.")


# --- TESTANDO O CÓDIGO ---

# Criando uma instância da classe mãe
heroi_comum = Personagem("Arthur")
heroi_comum.receber_dano(20)

print("-" * 30)

# Criando uma instância da classe filha (Herança)
meu_guerreiro = Guerreiro("Camargo")
meu_guerreiro.receber_dano(10)  # Ele consegue usar métodos do pai!
meu_guerreiro.usar_escudo()  # Ele tem métodos próprios!
