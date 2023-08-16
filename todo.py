tarefas = {}
tarefa_a_fazer = []
tarefas_em_andamento = []
tarefas_concluidas = []
ativo = True
while ativo == True:
    print("1- Adicionar tarefa")
    print("2 - Visualizar todas as tarefas")
    print("3 - Visualizar apenas as tarefas a fazer")
    print("4 - Visualizar apenas as tarefas que estão sendo feitas")
    print("5 - Visualizar apenas as tarefas concluídas")
    print("6 - Sair")
    opcao = int(input("Digite a opção que deseja: "))
    if opcao == 1:
        tarefa = input("Digite a tarefa: ")
        escolha_status = int(input(
            "Defina o status dessa tarde. Digite 1 para 'A fazer', 2 para 'Fazendo' e 3 para 'Concluída': "))
        if escolha_status == 1:
            status = 'A fazer'
            tarefa_a_fazer.append(tarefa)
        elif escolha_status == 2:
            status = 'Fazendo'
            tarefas_em_andamento.append(tarefa)
        elif escolha_status == 3:
            status = 'Concluída'
            tarefas_concluidas.append(tarefa)
        tarefas[tarefa] = status
    elif opcao == 2:
        print(tarefas)
    elif opcao == 3:
        print(tarefa_a_fazer)
    elif opcao == 4:
        print(tarefas_em_andamento)
    elif opcao == 5:
        print(tarefas_concluidas)
    elif opcao == 5:
        break
    else:
        print("Digite uma opçao válida")
