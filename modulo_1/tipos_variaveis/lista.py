#Declaração
minha_lista = [1,2,3,4,5, "rocktseat", True, False]

#Exibindo a lista
print("Minha lista de exemplo",minha_lista)

#Exibindo primeiro elemento da lista
print("minha_lista[0]", minha_lista[0])
print("minha_lista[0]", minha_lista[5])
#Fatiamento
print("minha_lista[1:7]",minha_lista[1:7])
print("minha_lista[:6]",minha_lista[:6])
print("minha_lista[2:]",minha_lista[2:])

#MÉTODOS DE LISTA
#Método append() : Adiciona um valor ao final da lista
minha_lista.append(6)
print("apos append(6):", minha_lista)


#Método index()
indice = minha_lista.index(6)
print("indice do elemento 6:", indice)


#Método insert(): inserir um elemento no indice especifico
minha_lista.insert(2, 10)
print("Apos o insert(2, 10):", minha_lista)

#Método POP
elemento_removido = minha_lista.pop(3)
print("elemento removido", elemento_removido)
print("lista apos o pop(3)", minha_lista)

#Método remove
minha_lista.remove("rocktseat")
print("Apos o remove(False):", minha_lista)

#Método sort
minha_lista.sort()
print("Após sort():", minha_lista)
