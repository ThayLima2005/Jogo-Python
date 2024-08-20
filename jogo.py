def iniciar_jogo():
    itens={
        "faca":False,
        "fosforos":False,
        "lampiao":False,
        "sal":False,
        "lata de querosene e uma gaiola com ossos":False,
        }
    nome_jogador=input("informe seu nome:")
    resposta=input(f"{nome_jogador} chega à mansão no seu carro, ao olhar mais de perto {nome_jogador} vê a grande mansão,\n"+
                   "ao se aproximar da grande porta de entrada a porta está trancada\n"+
                   "1 - Forçar porta\n2 - Procurar chave\n3 - Tentar porta dos fundos\n")
    print("resposta",resposta)
    if resposta == '3':
        print(f"{nome_jogador} entrou na mansão.")
        resposta=input(f"{nome_jogador} se depara com uma cozinha suja e escura, por uma ironia {nome_jogador} não havia levado uma lanterna e pensara o quanto lhe faria\n"
                       "falta naquele momento, voce resolve então procurar por alguma fonte de luz na cozinha.\n"+
                       "1 - Procurar nas gavetas\n2 - Procura nos armarios\n3 - Olhar dentro da geladeira\n")
        if resposta=="1":
            print(f"{nome_jogador} encontrou uma faca velha(que pode ser usada como arma) e uma caixinha de fosforos")
            itens['faca']=True
            itens["fosforos"]=True
        elif resposta == "2":
            print(f"{nome_jogador} achou o lampiao e um sal")
            itens["lampiao"]=True
            itens["sal"]=True
        
        if resposta!="3":
            if itens["fosforos"]==True:
                print(f"{nome_jogador} então usa os fósforos encontrados na gaveta como uma fonte de luz, {nome_jogador}vê uma porta que supostamente\n"+
                       f"daria para outro Cômodo, ao passar pela porta {nome_jogador} se vê em meio a sala,{nome_jogador} sente um calafrio, a sala começa\n"+
                         "esfriar rapidamente, então um vulto passa rapidamente por seus olhos, ao se virar se depara pela primeira vez \n"+
                         "com espírito vingativo de Chacal, seu rosto estava todo cortado como se navalhas tivessem o atingido, na cabeça\n"+
                           "ele usava uma gaiola do século passado, usava uma roupa de manicômio com cintos para ser amarrado, era uma visão\n"+
                             f"grotesca. O espírito do Chacal ataca {nome_jogador}")
                resposta=input("1 - correr\n2 - tentar usar a faca\n3 - ficar imovel\n")
            else:
                print(f"{nome_jogador} então usa os lampiao encontrados na gaveta para acender o lampião, {nome_jogador} vê uma porta que supostamente\n"+
                       f"daria para outro Cômodo, ao passar pela porta {nome_jogador} se vê em meio a sala, {nome_jogador} sente um calafrio,a sala começa\n"+
                         "esfriar rapidamente, então um vulto passa rapidamente por seus olhos, ao se virar se depara pela primeira vez \n"+
                         "com espírito vingativo de Chacal, seu rosto estava todo cortado como se navalhas tivessem o atingido, na cabeça\n"+
                           "ele usava uma gaiola do século passado, usava uma roupa de manicômio com cintos para ser amarrado, era uma visão\n"+
                             "grotesca. O espírito do Chacal ataca você")
                resposta=input("1 - correr\n2 - tentar jogar o sal\n3 - ficar imovel\n")
            if resposta=="2":
                if itens["faca"]==True:
                    print(f"{nome_jogador} usa a faca de ferro puro faz o fantasma recuar, ao usar a faca percebe que o fantasma do chacal\n"
                    "desaparece por enquando, você percebe o acontecido e se vê num jogo de gato e rato então ele decide\n")
                else:
                    print(f"{nome_jogador} joga o sal que faz o fantasma recuar, ao jogar o sal percebe que o fantasma do chacal\n"
                    "desaparece por enquando, você percebe o acontecido e se vê num jogo de gato e rato então ele decide\n")
                    
                resposta=input("1 - Ir embora\n2 - Segundo andar\n3 - porão\n")

                while resposta!="3" and resposta!="2":
                    print("Portas trancadas")
                    resposta=input("1 - Ir embora\n2 - Segundo andar\n3 - porão\n")

                if resposta=="3":
                    print(f"{nome_jogador} entra no porão\n"+
                          f"{nome_jogador} encontra anotações da famosa mansão, em uma dessas anotações você encontra uma agenda que dizia que\n"+
                          "para eliminar o espírito vingativo teria que jogar sal e pôr fogo em tudo vinculado ao fantasma ao descer\n"+
                          "a escada do porão escuro e sombrio, você percebe algo ruim ali, porém desistir não era uma opção, sua\n"+
                          "coragem de determinação eram maiores que o medo, ao adentrar o porão, feito de chão batido, contendo\n"+
                          "algumas ferramentas velhas penduradas na parede de tijolos maciços, havia alguns balcões e armário velhos\n"+
                          "usados para guardar as ferramentas e tortura também, ao procurar\n")  
                    resposta=input("1- Mexer fermentas\n2 - Verificar balcões\n3 - Verificar armario\n ")              
                    while resposta !="2" and resposta !="3":
                            print("Nada utilizavel")
                            resposta=input("1- Mexer fermentas\n2 - Verificar balcões\n3 - Verificar armario\n ")
                    if resposta=="2":
                        if itens["lata de querosene e uma gaiola com ossos"]==True:
                            print("acha lata de querosene e uma gaiola com os restos mortais\n"
                            "Então você começa sentir o calafrio no pescoço rapidamente você faz a sequência da anotação que você leu.")    
                            resposta=input("1- sal, querosene, fogo\n2- fogo, sal, querosene\n3- Tentar fugir\n  ")                                                         
                    if resposta=="2":
                        print("Rapidamente retirando a gaiola que ficará dos restos do chacal, você ateia fogo nos restos mortais\n"
                                  "do assassino e assiste aliviada pegar fogo. Lentamente a casa se iluminou com o amanhecer tudo fica\n"
                                    "claro, o pesadelo acabou..\n"
                                    f"{nome_jogador} agora retorna ao seu carro com a gaiola do chacal em sua mão,pois pensa em dar um destino mais\n"
                                    "adequado para aquele objeto, ela põe no banco traseiro do seu carro e fecha a porta, ao lembrar que já\n"
                                    "estava atrasada para seu serviço, você entra em seu carro e pega a estrada principal em direção a cidade,\n"
                                    "andando alguns metro ela olha para o retrovisor e vê chacal sentado no banco traseiro\n"
                                    "FIMM")
                    else:
                        print("VOCÊ MORREU")
                else:
                    print("Ao tentar acessar o segundo andar o velho chão de madeira da mansão cede e você cai em uma armadilha \n"+
                          "e morre pela queda")
            elif  resposta == "1":
                print("o assassino foi mais rapido e te pegou,vc morreu")
            else:
                print("vc ficou imovel e nada adiantou o assassino com seu olhar assustador te matou")
        else:
            print("voce ve sangue seco e ossos. voce da um grito de susto")
            print("com o grito voce chamou a atençao do assasino.Voce morreu")
    else:
        print("Um som de golpe, você sente uma dor atrás na cabeça. Você morreu")


        
            
        
           
