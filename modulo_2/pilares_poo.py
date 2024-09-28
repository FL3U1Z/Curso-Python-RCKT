#Herança
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def andar(self):
        print(f"O animal {self.nome} andou")
    
    def emitir_som(self):
        pass
    
class Cachorro(Animal):
    def emitir_som(self):
        return "au, au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
    
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\nExemplo de polimorfismo")
animals = [dog, cat]

for animal in animals:
    print(f"{animal.nome} faz: {animal.emitir_som()}")
    

print("\nExemplo de encapsulamento")

class Conta_Bancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo
    
conta = Conta_Bancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"

    def desligar(self):
        return "Carro desligado usando a chave"

carro_amarelo = Carro()
print(carro_amarelo.desligar())
