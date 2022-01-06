from datetime import date
data_atual = date.today()
data_em_texto = "0{}/0{}/{}".format(data_atual.day, data_atual.month,data_atual.year)

listaNomes      = ['aaa','bbb','ccc']
listaIdades     = [11,22,33]
listaNascimento = ['11/11/11','22/22/22','33/33/33']
listaMesMenor = ['04', '06', '09', '11']

def menu():
    m = '''
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
        if int(idade) > 0:
            return idade
        else:
            print("Digite uma maior que zero")
    except:
        print("Digite uma idade válida")

    return verificarIdade(input("Digite a idade: "))

def verificarDataNasc(data):
    try:
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

while True:
    escolha = menu() 
    if escolha == '0':
        break
    elif escolha == '1':
        cadastro()
