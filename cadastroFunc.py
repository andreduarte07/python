from datetime import date
data_atual = date.today()
data_em_texto = "0{}/0{}/{}".format(data_atual.day, data_atual.month,data_atual.year)

listaNomes      = ['Andre','Joao','Luccas']
listaIdades     = [23,21,25]
listaNascimento = ['23/11/1998','05/07/2000','18/01/1996']
listaMesMenor = ['04', '06', '09', '11']

def menu():
    m = ''' \n
            0-  Finalizar
            1-  Cadastrar dados nas listas
            2-  Listar somente os nomes
            3-  Listar os dados completos das pessoas
            4-  Localizar o nome de alguém e mostrar todos seus dados
            5-  Alterar a idade ou a data de nascimento
            6-  Excluir alguém do cadastro
            Escolha: '''
    return input(m)

def verificarIdade(idade):
    try:
        if int(idade) > 0 and int(idade) < 115:
            return idade
        else:
            print("Digite uma maior que zero")
    except:
        print("Digite uma idade válida")

    return verificarIdade(input("Digite a idade: "))

def verificarDataNasc(data):
    try:
        if data[2:3] == '/' and data[5:6] == '/':
            if int(data[:2]) > 00 and int(data[:2]) <= 31:
                if int(data[3:5]) > 00 and int(data[3:5]) < 12:
                    if data[3:5] in listaMesMenor and int(data[:2]) <= 30:
                        pass
                    elif data[3:5] == '02' and int(data[:2]) <= 28:
                        pass
                    elif data[3:5] not in listaMesMenor:
                        pass
            if data[6:] <= data_em_texto[6:]:
                listaNascimento.append(data)
        else:
            print("Digite uma data valida")
            verificarDataNasc(input("Digite a data de nascimento no formato dd/mm/aaaa: : "))
    except:
        print("Digite uma data valida")
        verificarDataNasc(input("Digite a data de nascimento no formato dd/mm/aaaa: : "))
 
def cadastro():
    listaNomes.append(input("Digite o nome: "))
    listaIdades.append(verificarIdade(input("Digite a idade: ")))
    listaNascimento.append(verificarDataNasc(input("Digite a data de nascimento no formato dd/mm/aaaa: : ")))

def listarNomes():
    for nome in range(len(listaNomes)):     
        print("Nome: %s"%listaNomes[nome])

def listarDados():
    for i in range(len(listaNomes)):     
        printar(i)

def localizarDados():
    while True:
        nome = input("Digite o nome que deseja buscar ou 0 para sair: ")
        if nome in listaNomes:
            i = listaNomes.index(nome)
            printar(i)
        elif nome == '0':
            break
        print("Nome não encontrado")    
        
def attDado():
    nome = input("Digite o nome de quem deseja alterar: ")
    if nome in listaNomes:
        i = listaNomes.index(nome)
        while True:   
            n = input("Digite 1 para alterar a idade ou 2 para data de nascimento ou 0 para sair: ")
            if n == '1':
                novaIdade = verificarIdade(input("Digite a nova idade: "))
                listaIdades[i] = novaIdade
                break
            elif n == '2':
                novaData = verificarDataNasc(input("Digite a data de nascimento no formato dd/mm/aaaa: : "))
                listaNascimento[i] = novaData
                break
            elif n == '0':
                break
            else:
                print("Digite 1 para alterar a idade ou 2 para data de nascimento ou 0 para sair: ")

def excluir():
    nome = input("Digite o nome de quem deseja excluir: ")
    if nome in listaNomes:
        
        i = listaNomes.index(nome)
        printar(i),
        print("\n     ---------Excluido com sucesso---------\n")
        listaNomes.pop(i)
        listaIdades.pop(i)
        listaNascimento.pop(i)    
    else:
        print("Nome nao localizado")

#Funçao para printar dados completos
def printar(i):
    print(f"Nome: {listaNomes[i]}, Idade: {listaIdades[i]}, Data de nascimento: {listaNascimento[i]}\n", end="")


#PROGRAMA PRINCIPAL

while True:
    escolha = menu() 
    if escolha == '0':
        break
    elif escolha == '1':
        cadastro()
    elif escolha == '2':
        listarNomes()
    elif escolha == '3':
        listarDados()
    elif escolha == '4':
        localizarDados()
    elif escolha == '5':
        attDado()
    elif escolha == '6':
        excluir()