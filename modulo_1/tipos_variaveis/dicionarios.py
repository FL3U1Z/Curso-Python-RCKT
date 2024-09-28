#criando um dicionario de exemplo
pessoa = {
    "nome": "Flávio",
    "idade":30,
    "cidade":"São Paulo"
    }

print("Meu dicionário de exemplo:", pessoa)
print("Nome:", pessoa["nome"])
print("idade:", pessoa["idade"])
print("cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Barbosa"
print("sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

#removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)