#PEDRO VICTOR VIEIRA DO NASCIMENTO
#MATRICULA:20171143000033

print("~"*50)
print("\nBEM VINDO AO JOGO DA FORCA!\n")
print("~"*50)

palavra_secreta = "IFCE"
letras_descobertas = []
tentativas = 4
for i in range (0, len(palavra_secreta)):
	letras_descobertas.append("-")
acertou = False

while acertou == False:
	letra = str(input("Digite uma letra:")).upper().strip()
	tentativas -= 1
	if tentativas >=0:

		for i in range(0, len(palavra_secreta)):
			if letra == palavra_secreta[i]:
				letras_descobertas[i] = letra
			print(letras_descobertas[i])
			
		acertou = True


		for x in range(0, len(letras_descobertas)):
			if letras_descobertas[x] == "-":
				acertou = False
		print("\nAinda lhe restam {} tentativas\n".format(tentativas))


	else:
		print("\nInfelimente suas tentativas chegaram a zero \n")
		print("*"*50)
		print("FIM DE JOGO!")
		print("*"*50)
		break
		
if acertou == True:
	print("*"*50)
	print("PARABÉS VOCÊ ACERTOU  PALAVRA!")
	print("*"*50)