import sys
from itertools import islice
email = ['123@gmail.com', '5646@yahoo.com', '555@yahoo.com', 'efeekcb@gmail.com', '44444@hotmail.com', 'trdgre@yahoo.com', 'asfdf@fiap.com.br', 'ejosejc@fiap.com.br', 'fred@hotmail.com', 'paulacelg@yahoo.com', 'jones@gmail.com', 'claudio@yahoo.com', 'dininho@gmail.com', 'tamara@yahoo.com', 'Josshua@hotmail.com', 'igdllcc@fiap.com.br', 'iakhlld@gmail.com', 'ebkfheg@fiap.com.br', 'fhldfge@yahoo.com', 'bgcihah@yahoo.com', 'ibijifk@fiap.com.br', 'leedghi@fiap.com.br', 'iacihaa@gmail.com', 'cfladcg@yahoo.com', 'eldichf@gmail.com', 'kckhbld@hotmail.com', 'iefgfec@yahoo.com', 'didcefi@hotmail.com', 'dcdjgkl@yahoo.com', 'befklgf@yahoo.com']
def print_menu():
    print("     \‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾/ ")
    print("     /  PESQUISADOR DE EMAILS VAZADOS \ ")
    print("     \________________________________/ ")
    print("")
    print("       \/ \/ Escolha uma opção \/ \/       ")
    print(" __________________________________________")
    print("| 1)                Sair                   |")
    print("| 2)      Consultar email especifico.      |" )     
    print("| 3) Verificar todos os e-mails vazados.   |")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
home = True

def bonito():
    print("===========================================")

def bonitodois():
    print("-------------------------------------------")

def checar():
    perguntadois = ""
    pergunta = ""
    buscarEmail = input("Digite um Email: ")
    if buscarEmail in email:
        print("Seu email foi vazado")
        bonitodois()
        pergunta = input("Deseja digitar outro email ?'S' Para confirmar.").upper()
        if pergunta !="S":
            negacao()
        else:
            pass
    elif buscarEmail not in email:
        bonito()
        print("Seu email nao foi vazado")
        bonito()
        pergunta = input("Deseja digitar outro email ?'S' Para confirmar.").upper()
        bonito()
        if pergunta == "S":
            checar()
        else:
            negacao()

def iteradortres():
    print("=======================================")
    print("      Listando 30 emails de", len(email))
    print("=======================================")
    print("")
    iterator = islice(email, 30)
    for mail in iterator:
        print(mail)
        bonitodois()

def iteradordois():
    print("=======================================")
    print("      Listando 20 emails de", len(email))
    print("=======================================")
    print("")
    iterator = islice(email, 20)
    for mail in iterator:
        print(mail)
        bonitodois()

def iteradorum():
    print("=======================================")
    print("      Listando 10 emails de", len(email))
    print("=======================================")
    print("")
    iterator = islice(email, 10)
    for mail in iterator:
        print(mail)
        bonitodois()
        
def todos():    
    confirmazero = ""
    confirmaum = ""
    confirmadois = ""
    if confirmazero != "N":
        iteradorum()
        confirmaum = input("Deseja visualizar mais 10 e-mails?'S' Para confirmar.").upper()
    if confirmaum == "S":
        iteradordois()
        confirmadois = input("Deseja visualizar mais 10 e-mails?'S' Para confirmar. ").upper()
    else:
        respinvalidazero()
        negacao()
    if confirmadois == "S":
        iteradortres()
        bonito()
        print("               Fim da Lista")
        bonito()
        negacao()

def volta_menu():
    print("\n"*30)
    print(" __________________________________________")
    print("| 1)                Sair                   |")
    print("| 2)      Consultar email especifico.      |" )     
    print("| 3) Verificar todos os e-mails vazados.   |")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def respinvalidaum():
    volta_menu()
    print("\n")
    print("Resposta Invalida.")
def respinvalidazero():
    bonito()
    print("Resposta Invalida.")
    bonito()
    

def negacao():
    print("1) Sair ")
    print("2) Voltar ao menu ")
    confirmasaida = input("Digite 1 ou 2: ")
    if confirmasaida == "1":
        saida()
    if confirmasaida == "2":
        volta_menu()
    else:
        print("\n"*10)
        respinvalidazero()
        negacao()

def saida():
    bonito()
    print("      Até mais, Obrigado por usar o buscador do Gian :(")
    sys.exit (bonito())

print_menu()
while home:
    bonitodois()
    escolha = input("Escolha entre [1-3]: ")
    bonitodois()

    if escolha == "1":
        print("\n"*2)
        saida()
        
    elif escolha == "2":
        print("\n"*10)
        bonito()
        print("         Consultar email específico")
        bonito()
        checar()

    elif escolha == "3":
        print("\n"*2)
        todos()
    else:
        respinvalidaum()