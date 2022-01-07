from datetime import date
data_atual = date.today()
data_em_texto = "0{}/0{}/{}".format(data_atual.day, data_atual.month,data_atual.year)
listaMesMenor = ['04', '06', '09', '11']

######  CLASSE  #######
class Pessoa:
    def __init__(self, nome, idade, dataNasc):
        self.nome = nome
        self.idade = idade
        self.dataNasc = dataNasc

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getDataNasc(self):
        return self.dataNasc

    def setIdade(self, idade):
        self.idade = idade
    
    def setDataNasc(self, dataNasc):
        self.dataNasc = dataNasc


#####  Funcoes   ######
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
                return data
        else:
            print("Digite uma data valida")
            verificarDataNasc(input("Digite a data de nascimento no formato dd/mm/aaaa: : "))
    except:
        print("Digite uma data valida")
        verificarDataNasc(input("Digite a data de nascimento no formato dd/mm/aaaa: : "))
 
def cadastraPessoa():
    def novaPessoa():
        nome  = input("Digite o nome: ")
        idade = verificarIdade(input("Digite a idade: "))
        dataNasc = verificarDataNasc(input("Digite a data de nascimento no formato dd/mm/aaaa: : "))
        return Pessoa(nome, idade, dataNasc)

    listaPessoas.append(novaPessoa())

def listarNomes():
    for pessoa in listaPessoas:
        print("Nome: {}".format(pessoa.getNome()))

def listarDados():
    for pessoa in listaPessoas:
        printar(pessoa)

def localizarNome():
    nome = input("Digite o nome: ")
    for pessoa in listaPessoas:
        if pessoa.getNome() == nome:
            printar(pessoa)
        else:
            print("Nome não localizado")

def attDado():
    nome = input("Digite o nome: ")
    while True:
        n = input("Digite 1 para alterar a idade ou 2 para data de nascimento ou 0 para sair: ")
        if n == '1':
            for pessoa in listaPessoas:
                if pessoa.getNome() == nome:
                    pessoa.setIdade(verificarIdade(input("Digite a nova idade: ")))
            break
        elif n == '2':
            for pessoa in listaPessoas:
                if pessoa.getNome() == nome:
                    pessoa.setDataNasc(verificarDataNasc(input("Digite a data de nascimento no formato dd/mm/aaaa: : ")))
            break
        elif n == '0':
            break
        else:
            print("Digite 1 para alterar a idade ou 2 para data de nascimento ou 0 para sair: ")

def delDado():
    nome = input("Digite o nome: ")
    for pessoa in listaPessoas:
        if pessoa.getNome() == nome:
            listaPessoas.remove(pessoa)

def printar(pessoa):
    print(f"Nome: {pessoa.getNome()}, Idade: {pessoa.getIdade()}, Data de nascimento: {pessoa.getDataNasc()}\n", end="")

# Programa Principal
listaPessoas = []

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

while True:
    escolha = menu() 
    if escolha == '0':
        break
    elif escolha == '1':
        cadastraPessoa()
    elif escolha == '2':
        listarNomes()
    elif escolha == '3':
        listarDados()
    elif escolha == '4':
        localizarNome()
    elif escolha == '5':
        attDado()
    elif escolha == '6':
        delDado()