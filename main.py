from tutorial import tutorial
from menu import menu
from jogo import iniciar_jogo
from jogo import iniciar_jogo
tutorial()
opcao=""
while opcao != '0':
    opcao=menu()
    print("opção menu",opcao)
    if opcao=="1":
        iniciar_jogo()

