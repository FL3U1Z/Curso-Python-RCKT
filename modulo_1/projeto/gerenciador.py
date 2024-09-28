def adicionar_tarefa(tarefas, nome_tarefa):

    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("Lista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else ""
        nome_tarefa = tarefa["nome"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, new_nome):
    if indice_tarefa - 1 >= 0 and indice_tarefa - 1 < len(tarefas):
        tarefas[indice_tarefa - 1]["nome"] = new_nome
        print(f"Tarefa {indice_tarefa} atualizado para {new_nome}")
    else:
        print("indice indisponivel")
    return

def completar_tarefa(tarefas, indice_tarefa):
    if indice_tarefa - 1 >= 0 and indice_tarefa - 1 < len(tarefas):
        tarefas[indice_tarefa - 1]["completada"] = True
        print(f"Tarefa {indice_tarefa} marcada como completa")
    else:
        print("indice indisponivel")
    return

def deletar_tarefas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    
    print("Tarefas completadas foram removidas")
    return

tarefas = []

while True:
    print("\nMenu  do Gerenciador de Lista de tarefa:")
    print("1. Adicionar Tarefa")
    print("2. ver Tarefa")
    print("3. atualizar Tarefa")
    print("4. completar Tarefa")
    print("5. Deletar Tarefa")
    print("6. sair ")

    escolha = input("Digite a sua escolha:")
    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar!: ")
        adicionar_tarefa(tarefas, nome_tarefa)
        
    elif escolha == "2":
        ver_tarefas(tarefas)
        
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o numero da tarefa que queira editar: "))
        nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, nome_tarefa)
        
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o numero da tarefa que completar: "))
        completar_tarefa(tarefas, indice_tarefa)
        
    elif escolha == "5":
        deletar_tarefas(tarefas)
        ver_tarefas(tarefas)
    else:
        break

print("Programa finalizado")