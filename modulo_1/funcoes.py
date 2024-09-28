#exemplo
def saudacao(nome):
    print(f"Olá, {nome}!")
print("Chamando a função")
saudacao("Alice")
saudacao("Flávio")

#Função com retorno
def quadrado(numero):
    resultado == numero ** 2 # type: ignore
    return resultado # type: ignore

print("Chamando a função quadrado")
resultado_quadrado = quadrado(8)
print("Resultado", resultado_quadrado)
