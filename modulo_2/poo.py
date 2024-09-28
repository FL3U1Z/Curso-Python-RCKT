#Classe de exemplo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome;
        self.idade = idade
    
    def saudacao(self):
        print(f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos!")
    
#obejto
pessoa1 = Pessoa("Flávio", 21)
mensagem = pessoa1.saudacao()
print(mensagem)


pessoa2 = Pessoa("Rodriho", 23)
mensagem = pessoa2.saudacao()