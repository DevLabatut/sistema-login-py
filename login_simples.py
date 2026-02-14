import getpass

def sistema_login():

    print("")

    print("[ Cadastro ]")
    email = input("Informe seu e-mail: ")
    password = getpass.getpass("Informe sua senha: ")

    if email == "" or password == "":
        print("Campos obrigatórios não preenchidos.")
        return

    print("")

    print("[ Login ]")
    emailInput = input("Informe seu e-mail: ")
    passwordInput = getpass.getpass("Informe sua senha: ")

    if emailInput == "" or passwordInput == "":
        print("Campos obrigatórios não preenchidos.")
        return

    if emailInput == email and passwordInput == password:
        print("Login realizado com sucesso.")
        acesso_sistema()
    else:
        print("E-mail ou senha incorretos.")

def acesso_sistema():

    print("")

    print("[ Área restrita ]") 
    print("Bem-vindo! Você agora tem acesso ao sistema.")

    print("")
    
sistema_login()