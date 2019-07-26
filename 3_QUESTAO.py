#PEDRO VICTOR VIEIRA DO NASCIMENTO
#MATRICULA:20171143000033

from time import sleep#TEMPO
#introdução
print("-"*50)
print("BEM VINDO AO JOGO!")
print("-"*50)
print("BEM VINDO AO CRIADOR DE HISTORIAS MALUCAS\n")
print("TEMAS DAS HISTORIAS\n")
print("1 - ZOEIRA COM O AMIGO.")
print("2 - UM DIA NO SAFARI.")
print("3 - RETORNO DA SERIE")

TEMA = int(input("Qual tema voce quer escolher:\n")) #Escolha do tema da historia


if TEMA == 1: # Caso escolha a primeira
	print("TEMA: ZOEIRA COM O AMIGO\n")
	A = input("DIGITE UM SUBSTANTIVO COMUM (MASCULINO): ")
	B = input("DIGITE UM SUBSTANTIVO COMUM (PLURAL): ")
	C = input("DIGITE UM SUBSTANTIVO COMUM (FEMININO): ")
	prin("Aguarde... Estamos preparando a historia.\n")
	sleep(2) #Aguarda alguns segundo
	print("Hoje, eu e meus amigos vamos aprontar uma pegadinha com nosso colega de sala."
		"Nos vamos pegar uma  e encher de {} para colocarmos em cima da porta, e" 
		"quando nosso colega abrir a porta, {} vai cari em cima dele e vai enche-lo de {} Vai ser hilario.\n".format(A,B,C))
	print("FIM DA HISTORIA.\n")

if TEMA == 2: # Caso escolha a segunda
	print("TEMA: UM DIA NO SAFARI.\n")
	A = input("DIGITE UM NOME DE UM VEICULO: ")
	B = input("DIGITE UM ADJETIVO: ")
	C = input("DIITE UM NOME ANIMAL (MASCULINO): ")
	D = input("DIGITE UM NOME ANIMAL (VEMININO):")
	E = input("DIGITE UM SUBSTANTIVO COMUM: ")
	print("Aguarde... Estamos preparando a historia.\n")
	sleep(2)
	print("Eu e meus amigos resolvemos ir no safari para nos divertir e ver uns animais legais"
		"Nos fomos de {} para lá. Quando chegamos na entrada do safari, o guarda foi avaliar"
		"nosso veiculo para ter certeza que era seguro para tal ambiente. O guarda disse que nosso veiculo"
		"era {} e que é possivel entrar no safari com ele. Bem, nos entramos e vimos dezenas de animais."
		"É algo fora do comum. Nunca tinha visto nada igual. O animal que achei mais legal foi o {} Sempre quis ter um"
		"lá em casa, mas não daria certo. Passado alguns instantes, um dos meus amigos gritou,"
		"e levamos um susto, pois havia uma {} no ombro dele. Espantei ela com o meu {} que levo sempre comigo"
		"Quem sabe se ela tinha veneno. Seria algo horrivel, mas ja passou. Bem, é hora de voltar para casa."
		" Foi um dia inesquecivel. Espero voltar mais vezes a este lugar.\n".format(A,B,C,D,E))
		
	print("FIM DA HISTORIA")

if TEMA == 3: #Caso escolha o terceiro
	print("TEMA: RETORNO DA SEIRE\n")
	A = input("DIGITE O NOME DE UMA SERIE: ")
	B = input("DIGITE UMA DATA, DIA E MES: ")
	C = input("DIGITE O NOME DE OUTR SERIE: ")
	D = input("DIITE UM NOME MASCULINO: ")
	E = input("DIGITE UM NOME E SOBRENOME MASCULINO: ")
	prin("Aguarde... Estamos preparando a historia.\n")
	sleep(2)
	print("Chegou o primeiro cartaz da quarta temporada de {}"
		"Com estreia marcada para o dia {}, a nova temporada da serie derivada de {}"
		"promete bastante mudanças. A serie trara {} ({}) e vai promover o primeiro"
		"crossover com a produção principal, e novos personagens tambem foram anunciados".format(A,B,C,D,E))

	print("FIM DA HISTORIA.")