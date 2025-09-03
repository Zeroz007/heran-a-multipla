class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def mostrar_tarefas(self):
        print("Faz tarefas gerais.")

class Desenvolvedor:
    def __init__(self, linguagem):
        self.linguagem = linguagem

    def programar(self):
        print(f"Programando em {self.linguagem}.")

class Testador:
    def testar(self):
        print("Testando o sistema.")

class EngenheiroDeSoftware(Funcionario, Desenvolvedor):
    def __init__(self, nome, linguagem):
        # Inicializa ambas as classes pai
        Funcionario.__init__(self, nome)
        Desenvolvedor.__init__(self, linguagem)
    
    def mostrar_tarefas(self):
        # Chama o método da classe Funcionario
        super().mostrar_tarefas()
        # Adiciona a ação de programar
        self.programar()
    
    def apresentar(self):
        print(f"Olá, sou {self.nome} e trabalho com {self.linguagem}.")

# Teste da classe
if __name__ == "__main__":
    # Criando um engenheiro de software
    eng = EngenheiroDeSoftware("Gustavo Santos", "Python")
    
    # Testando os métodos
    print("=== Apresentação ===")
    eng.apresentar()
    
    print("\n=== Tarefas ===")
    eng.mostrar_tarefas()
    
    print("\n=== Teste adicional ===")
    print(f"Nome: {eng.nome}")
    print(f"Linguagem: {eng.linguagem}")