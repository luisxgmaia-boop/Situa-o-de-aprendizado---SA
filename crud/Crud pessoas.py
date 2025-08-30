pessoas = []

#corrijido
def nome_de_cadastro():
    while True:
        nome = input("\ndigite o nome: ")

        if not nome:
            print("❗Campo Obrigatorio❗")
        elif any(char.isdigit() for char in nome):
            print("❗Nome Nao Existi Numeros❗")
        else:
            return nome
        
#corrijido
def cpf_de_cadastro():
    while True:    
        try:    
            cpf = input("★\nQual o CPF (somente números): ")

            cpf = cpf.replace('.', '').replace('-', '')

            if not cpf.isdigit():
                raise ValueError 

            if len(cpf) != 11:
                print("❗CPF deve ter exatamente 11 dígitos❗")
                continue

            if cpf == cpf[0] * 11:
                print("❗Todos os números do CPF são iguais❗")
                continue
            
            return cpf
        
        except ValueError:
            print("❗CPF inválido. Use apenas números❗")

#corrijido
def email_de_cadastro():
    
    while True:
        email = input("★\nDigite o email: ").strip()

        if not email:
            print("❗O campo de e-mail não pode estar vazio❗")
        elif '@' not in email or '.' not in email:
            print("❗Email inválido, é obrigatório ter '@' e '.'❗")
        else:
            parte1 = email.split('@')
            if len(parte1) != 2 or not parte1[0]:
                print("❗Email inválido: falta falta algo antes do'@'❗")
            else:
                usuario, dominio = parte1
                dominio_partes = dominio.split('.')
                if len(dominio_partes) < 2 or not dominio_partes[0] or len(dominio_partes[-1]) < 2:
                    print("❗Email inválido: email mal formatado❗")
                else:
                    break

#corrijido
def idade_de_cadastro():
    while True:
        try:
            idade = int(input("★\nDigite a idade: "))
            
            if idade < 18:
                print("❗Voce nao tem a idade minima❗")
                continue
            else:
                return idade
        except ValueError:
            print("❗Digite sua idade, sem letras❗")
            continue
            
#corrijido
def peso_usuario():
    while True:
        try:
            peso = int(input("★\nQual o peso: "))
            
            if peso < 46:
                print("❗Voce esta abaixo do peso❗")
            elif peso > 102:
                print("❗Voce esta acima do peso❗")
            else:
                return peso
                
        except ValueError:
            print("❗Digite seu peso apenas em numeros❗") 

#corrijido
def problema_fisico():
    while True:
        try:    
            deficiencia = input("★\nPossui problema fisico (sim/nao): ")
            
            if deficiencia not in ["sim", "nao"]:
                print("❗Digite apeans 'sim' ou 'nao'❗")
            else:
                return deficiencia
        except ValueError:
            continue

#corrijido
def escolaridade():
    while True: 
        print("\n📒--- Nivel de Escolaridade ---📒 ★\n")
        print("★ 1- Ensino Fundamental ★ ")
        print("★ 2- Ensino Médio ★ ")
        print("★ 3- superior ★ ")
        try:
            opçao = int(input("\n★ Digite uma opçao: "))
            if opçao > 3 or opçao < 1:
                print("❗ Opção Invalida ❗")
            else:
                return opçao 
        
        except ValueError:
            print("❗ Opção Invalida ❗")
        
#corrijido  
def interesse():
    while True :
        servir = input("★\nQuer Servir (sim/nao): ")
        try:    
            if servir not in ["sim", "nao"]:
                print("❗Digite 'sim' ou 'nao' apenas❗")
            else:
                return servir
        except ValueError:
            continue

#corrijido 
def historico():
    while True:
        historico = input("★\nTem passagem pelo policia ou algo similar (sim/nao): ")
        try:    
            if historico not in ["sim", "nao"]:
                print("❗Digite 'sim' ou 'nao' apenas❗")
            else:
                return historico
        except ValueError:
            continue
        
#corrijido 
def cadastro_pessoa():
    nome = nome_de_cadastro()
    cpf = cpf_de_cadastro()
    email = email_de_cadastro()
    idade = idade_de_cadastro()
    peso = peso_usuario()
    fisico = problema_fisico()
    estudo = escolaridade()
    vontade = interesse()
    passagem = historico()

    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "idade": idade,
        "peso": peso,
        "fisico": fisico,
        "estudo": estudo,
        "vontade": vontade,
        "passagem": passagem
    }
    pessoas.append(pessoa)

#corrijido
def remover():
    if not pessoas:
        print("❗Nao ha pessoas na lista❗")
        return

    nome_lista()

    while True:
        try:
            escolha = input("\nQual pessoa deseja excluir: ")

            if escolha == '':
                print("❗Campo Obrigatorio❗")
                continue

            escolha = int(escolha)

            if not 0 <= escolha < len(pessoas):
                print("❗Digite apenas o código dos nomes registrados❗")
                continue

            pessoas.pop(escolha)
            return

        except ValueError:
            print("❗Digite apenas o código dos nomes registrados❗")
            
#corrijido
def alterar_dados():
    if not pessoas:
        print("❗Não há pessoas cadastradas❗")
        return
    
    nome_lista()
    
    try:
        alternativa = input("\nQual pessoa você deseja alterar (número)? ")

        if alternativa == "":
            print("❗Você precisa digitar o número de alguém❗")
            return

        escolha = int(alternativa)

        if not 0 <= escolha < len(pessoas):
            print("❗Código inválido❗")
            return
        
        pessoa = pessoas[escolha]

        print("\n======================================================================================================")
        print(f"\n✏️ Alterando dados de: {pessoa['nome']}")
        print("★ 1 - Nome")
        print("★ 2 - CPF")
        print("★ 3 - Email")
        print("★ 4 - Idade")
        print("★ 5 - Peso")
        print("★ 6 - Problema físico")
        print("★ 7 - Escolaridade")
        print("★ 8 - Interesse em servir")
        print("★ 9 - Histórico policial")

        opcao = int(input("\nDigite o número do campo que deseja alterar: "))

        if opcao == 1:
            pessoa['nome'] = nome_de_cadastro()
        elif opcao == 2:
            pessoa['cpf'] = cpf_de_cadastro()
        elif opcao == 3:
            pessoa['email'] = email_de_cadastro()
        elif opcao == 4:
            pessoa['idade'] = idade_de_cadastro()
        elif opcao == 5:
            pessoa['peso'] = peso_usuario()
        elif opcao == 6:
            pessoa['fisico'] = problema_fisico()
        elif opcao == 7:
            pessoa['estudo'] = escolaridade()
        elif opcao == 8:
            pessoa['vontade'] = interesse()
        elif opcao == 9:
            pessoa['passagem'] = historico()
        else:
            print("❗Opção inválida❗")
    
    except ValueError:
        print("❗Entrada inválida. Digite apenas números❗")

#corrijido
def vizualizar_dados():

    if not pessoas:
        print("❗Não há pessoas cadastradas❗")
        return
    
    nome_lista()

    try:
        quem = input("\nDigite o número da pessoa que deseja visualizar: ")

        if not quem:
            return
        
        indice = int(quem)

        if not 0 <= indice < len(pessoas):
            print("❗Código inválido❗")
            return
        
        pessoa = pessoas[indice]

        print("\n======================================================================================================")
        print("\n📋 --- Dados da Pessoa --- 📋")
        print(f"★ Nome: {pessoa['nome']}")
        print(f"★ CPF: {pessoa['cpf']}")
        print(f"★ Email: {pessoa['email']}")
        print(f"★ Idade: {pessoa['idade']} anos")
        print(f"★ Peso: {pessoa['peso']} kg")
        print(f"★ Problema físico: {pessoa['fisico']}")
        print(f"★ Escolaridade: {formata_escolaridade(pessoa['estudo'])}")
        print(f"★ Quer servir: {pessoa['vontade']}")
        print(f"★ Histórico policial: {pessoa['passagem']}")

    except ValueError:
        print("❗Digite apenas números válidos❗")

#corrijido
def formata_escolaridade(nivel):
    if nivel == 1:
        return "Ensino Fundamental"
    elif nivel == 2:
        return "Ensino Médio"
    elif nivel == 3:
        return "Superior"
    else:
        return "Desconhecido"

#corrijido
def nome_lista():
    print("\n======================================================================================================")
    print("\n📅 --- Lista de Pessoas --- 📅")
    for i, pessoa in enumerate(pessoas):
        print(f"{i} - {pessoa['nome']}")

#=======================================================================================================

print("...................")
print("     ★ ★ ★ ★")
print("   ★          ★")
print("  ★  EXÉRCITO  ★")
print("  ★ BRASILEIRO ★")
print("   ★          ★")
print("     ★ ★ ★ ★")
print("...................")

while True:
    print("\n======================================================================================================")
    print("\n🗒️ --- Sentido Coronoel --- 🗒️")
    print("1- Cadastrar Pessoa")
    print("2- Listar Pessoas")
    print("3- Atualizar Dados")
    print("4- Excluir Pessoas")
    print("5- Visualizar Dados")
    print("6- Finalizar Recrutamento 🪖")

    try:
        resposta = int(input("\nQual opçao desejada: "))

        if resposta == 1:
            cadastro_pessoa()
        elif resposta == 2:
            nome_lista()
        elif resposta == 3:
            alterar_dados()
        elif resposta == 4:
            remover()
        elif resposta == 5:
            vizualizar_dados()
        elif resposta == 6:
            print("❗Programa Finalizado❗")
            break
        else:
            print("❗Opçao invalida❗")

    except ValueError:
        print("❗Opção invalida, Digite apenas as opções❗")
        
#sla
