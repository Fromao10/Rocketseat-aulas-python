# Adicionar contato favorito
def adicionar_favoritos(agenda_favoritos, nome_favoritos, telefone_favoritos, email_favoritos):
     dados_contato_favorito= {"nome_favorito": nome_favoritos, "telefone_favorito": telefone_favoritos, "email_favorito": email_favoritos}
     agenda_favoritos.append(dados_contato_favorito)
     print(f"\nO Contato de {nome_favoritos} foi adicionado aos favoritos com sucesso!")
     return

# Adicionar contato
def adicionar_contato(agenda, nome_contato, telefone_contato, email_contato):
    dados_contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato}
    agenda.append(dados_contato)
    print(f"\nO contato de {nome_contato} foi adicionado a agenda com sucesso!")
    return
   
# Consultar agenda
def consultar_favoritos(agenda_favoritos):
     print("\nLista de contatos favoritos:")
     agenda_favoritos.sort(key=lambda x: x["nome_favorito"])
     for contato in agenda_favoritos:
        print(f"{contato["nome_favorito"]} - {contato["telefone_favorito"]} - {contato["email_favorito"]}")
     return

def consultar_agenda(agenda):
    print("\nlista de contatos:")
    agenda.sort(key=lambda x: x["nome"])
    for contato in agenda:
        print(f"{contato["nome"]} - {contato["telefone"]} - {contato["email"]}")
    return

# Atualizar contatos
def atualizar_contato(agenda, nome_atual, novo_nome, novo_telefone, novo_email):
    for contato in agenda:
        if ["nome"] == nome_atual:
            contato["nome"] == novo_nome
            contato["telefone"] = novo_telefone
            contato["email"] == novo_email
            print(f"\nO Contato de {nome_atual} foi adicionado com sucesso!")
            return
    print(f"\nContato com o nome {nome_atual} não encontrado.")
    return

# Atualizar contatos favoritos
def atualizar_favortitos(agenda_favoritos, nome_atual, novo_nome, novo_telefone, novo_email):
    for contato in agenda_favoritos:
        if contato["nome_favorito"] == nome_atual:
            contato["nome_favorito"] == novo_nome
            contato["telefone_favorito"] == novo_telefone
            contato["email_favorito"] == novo_email
            print(f"\nO contato favorito de {nome_atual} foi atualizado com sucesso!")
            return
    print(f"\nContato favorito com nome de {nome_atual} não encontrado.")
    return

# Apagar contato
def apagar_contato(agenda, nome_contato):
    for contato in agenda:
        if contato["nome"] == nome_contato:
            agenda.remove(contato)
            print(f"\nO contato de {nome_atual} foi removido com sucesso!")
            return
    print(f"\nContato com o nome {nome_contato} náo encontrado.")

# Apagar favorito    
def apagar_favorito(agenda_favoritos, nome_contato):
    for contato in agenda_favoritos:
        if contato["nome_favorito"] == nome_contato:
            agenda_favoritos.remove(contato)
            print(f"\nO contato de {nome_atual} foi pagado com sucesso!")
            return
    print(f"\nContato favorito com o {nome_contato} náo encontrado.")    
        
agenda_favoritos = []
agenda = []
while True:
    print("\nMenu gerenciador da agenda")
    print("1. Adicionar contato")    
    print("2. Consultar agenda")
    print("3. Atualizar contato")
    print("4. Deletar contato")
    print("5. Sair")

    escolha = input("\nDigite sua opração da agenda: ")

    if escolha == "1":
        nome = input("Digite o nome do contato que deseja adicionar: ")
        telefone = input("Digite o telefone que deseja adicionar: ")
        email = input("Digite o email que deseja adicionar: ")
        add_favoritos = input("Deseja adicionar esse contato aos favoritos? \nDigite S para sim ou digite N para não: ")
        if add_favoritos == "s":
            adicionar_favoritos(agenda_favoritos, nome, telefone, email)     
        elif add_favoritos == "n":  
            adicionar_contato(agenda, nome, telefone, email)
        elif add_favoritos not in ["s", "n"]:
            print("\nResposta inválida!")
        

    elif escolha == "2":
         consultar_favoritos(agenda_favoritos)
         consultar_agenda(agenda)
         
    elif escolha == "3":
        nome_atual = input(("Digite o nome que deseja atualizar: "))
        novo_nome = input(("Digite o novo nome do contato: "))
        novo_telefone = input(("Digite o novo telefone do contato: "))
        novo_email = input("Digite o novo email do contato: ")
        lista = input("Deseja atuliazar a agenda dos favoritos? \nDigite S para sim ou N para não.")
        if lista == "s":
            atualizar_favortitos(agenda_favoritos, nome_atual, novo_nome, novo_telefone, novo_email)
        elif lista not in ["s", "n"]:
            print("\nResposta inválida!")  
        else:
            atualizar_contato(agenda, nome_atual, novo_nome, novo_telefone, novo_email)  

    elif escolha == "4":
        nome_atual = input("Digite o nome do contato que deseja apagar: ")
        lista_favoritos = input("Esta em favoritos? \nDigite S para sim e N para não: ")
        if lista_favoritos == "s":
            apagar_favorito(agenda_favoritos, nome)
        elif lista_favoritos not in ["s", "n"]:
            print("\n Resposta inválida!")
        else:
            apagar_contato(agenda, nome)

    elif escolha == "5":
        break
