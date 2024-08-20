def menu():
    while True:
        print("1 - novo jogo\n0 - sair")
        opcao=input("informe a opção: ")
        if opcao=="1" or opcao=="01":
            return(opcao)
        else:
            print("opçao invalida")
        