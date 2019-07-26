#PEDRO VICTOR VIEIRA DO NASCIMENTO
#MATRICULA:20171143000033

import random
from time import sleep
rolar_dado = "sim"
dado = 0
#cabeçalho
print("*"*50)
print("        BEM VINDO AO JOGO DO DADO!")
print("*"*50)

print("Voce deseja jogar o dado ? sim ou não")
rolar_dado = input().lower().strip()

	
		
while rolar_dado == "sim":
	minimo = 1
	maximo = 6
	sorte = int(input("\nQual numero você acha que vai cair de 1 a 6? "))
	if (sorte <1 or sorte >6):
		print("Da proxima vez digite um numero de 1 a 6.")
	valor = random.randint(int(minimo),int(maximo))
	print("Espere só um pouco... Deixe eu ver o numero que caiu.")
	sleep(2)
	print("\nO numero que caiu foi o {}\n".format(valor))
	rolar_dado = input("Gostaria de rolar o dado novamente:").lower().strip()
			
			

print("\nOBRIGADO POR TER JOGADO!\n")
print("*"*50)
print("FIM DE JOGO!")
print("*"*50)
			# falta colocar cabeçãlho
			
			# Organizar 
		