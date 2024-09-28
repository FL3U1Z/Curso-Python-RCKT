lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)
    
print("\nFor Utilizando Tupla")
tupla = [1,2,3,4,5]
for elemento in tupla:
    print(elemento)
    
pessoa = {"nome":"João", "idade":30, "cidade":"São Paulo"}
print("\n For utilizando dicionario - chaves")
for chave in pessoa.keys():
    print(chave)

print("\n For utilizando dicionario - valores")
for valores in pessoa.values():
    print(valores)
    
print("\n For utilizando ambos - chaves:valores ")
for chave, valores in pessoa.items():
    print(f"{chave}:{valores}")
    
print("\n For utilizando range() ")
for numeros in range(5):
    print(f"Numero: {numeros}")
    
print("\nUtilizando a função range() com len()")
lista = [1,2,3,4,5]
print(f"Lista antes: {lista}")
for indice in range(0, len(lista)):
    print(f"indice: {indice}")
    print(f"N do indice: {lista[indice]}")
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(f"Lista depois: {lista}")

#enumerate()
lista_enumerate = ["a","b","c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    
#range(): intervalo de numeros
for numero in range(5):
    print("numero:", numero)