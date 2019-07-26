#PEDRO VICTOR VIEIRA DO NASCIMENTO
#MATRICULA:20171143000033

from random import randint # gerar numeros aleatorios
from time import sleep # para o programa para os segundo que voce quiser

maquina = randint (0, 10) #Numero aleatorio de 0 a 10
#CABEÇALHO
print("="*50)
print("         BEM VINDO AO JOGO DA ADIVINHAÇÃO")
print("="*50)
print ("Sou uma maquina, e queria saber se você gostaria de participar de um jogo comigo ? ")
print("O jogo é de adivinhção, eu vou pensar em um numero entre 0 e 10 e você vai tentar adivinhar. OK?")
acertou = False
tentativa = 0

while not acertou:
	#Entrada do usuario.
	jogador = int(input("Digite o numero que você acha que estou pensando: "))
	tentativa +=1
	print("Aguarde...")
	sleep(2)
	if jogador == maquina:
		acertou = True
		
	else:
		if jogador < maquina:
			print("-=-"*15)
			print("O numero é MAIOR. Tente outra vez.")
			print("-=-"*15)
			
		elif jogador > maquina:
			print("-=-"*15)
			print("O numero é MENOR. Tente outra vez.")
			print("-=-"*15)
			
print("Acertou com {} tentativas".format(tentativa))
print("*"*50)
print("          PARABÉNS, VOCÊ ACERTOU!")
print("*"*50)

# Colocar um cabeçalho 
# Comentar
# Organizar a strutura