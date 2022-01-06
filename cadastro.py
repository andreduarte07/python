
menu = ''' \n\n\nMenu
0-  Finalizar
1-  Cadastrar dados nas listas
2-  Listar somente os nomes
3-  Listar os dados completos das pessoas
4-  Localizar o nome de alguém e mostrar todos seus dados
5-  Alterar a idade ou a data de nascimento
6-  Excluir alguém do cadastro
Escolha: '''

escolha = ''
listaNomes      = ['aaa','bbb','ccc']
listaIdades     = [11,22,33]
listaNascimento = ['11/11/11','22/22/22','33/33/33']

while escolha != 0:
    escolha = int(input(menu))
    if escolha == 1:
        print("\nCadastro")
        nome = input("Digite o nome: ")
        idade= input("Digite a idade: ")
        data = input("Digite a data de nascimento no formato dd/mm/aaaa: ")
        listaNomes.append(nome)
        listaIdades.append(idade)
        listaNascimento.append(data)
    elif escolha == 2:
        print("\nListagem dos Nomes Cadastrados")
        for nome in listaNomes:
            print(nome)
    elif escolha == 3:
        print("\nRelatório completo")
        for i in range(len(listaNomes)):
            print(listaNomes[i],', ',listaIdades[i],', ',listaNascimento[i])

    elif escolha == 4:
        print("\nLocalizar pessoa")
        nomeAux = input("Digite o nome para localizar: ")
        if nomeAux in listaNomes:
            i = listaNomes.index(nomeAux)
            print(listaNomes[i],listaIdades[i],listaNascimento[i])
        else:
            print("Nome não localizado.")

    elif escolha == 5:
        print("\nAlterar Dados")
        nomeAux = input("Digite o nome para localizar: ")
        if nomeAux in listaNomes:
            i = listaNomes.index(nomeAux)
            escolha = input("O que desejas alterar?  1- Idade    2- Data de Nascimento: ")
            if escolha == '1':
                novaIdade = input("Digite a nova Idade: ")
                listaIdades[i] = novaIdade
                print("Ok, Idade alterada.")
            if escolha == '2':
                novaData = input("Digite a nova data de Nascimento: ")
                listaNascimento[i] = novaData
                print("Ok, Data alterada.")
        else:
            print("Nome não localizado.")

    elif escolha == 6:
        print("\nExclusão")
        nomeAux = input("Digite o nome para localizar: ")
        if nomeAux in listaNomes:
            resposta = input("Confirma Exclusão? s/n: ")
            i = listaNomes.index(nomeAux)
            if resposta == "s":
                listaNomes.pop(i)
                listaIdades.pop(i)
                listaNascimento.pop(i)
                print("Exclusão confirmada.")
        else:
            print("Nome não localizado.")
