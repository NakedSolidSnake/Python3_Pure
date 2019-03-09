import random

def subtraiPontos(pontos, tentativas):
	print("pontos = {}, tentativas = {}".format(pontos, tentativas))
	novoValor = pontos - round(pontos / tentativas)
	print("novoValor = {}".format(novoValor))
	return novoValor

def adivinhacao():
	print("************************************************")
	print("*************Jogo da adivinhacao****************")
	print("************************************************")

	print("Selecione a dificuldade:")
	print("[1] - Fácil")
	print("[2] - Médio")
	print("[3] - Difícil")

	dificuldade = int(input())

	tentativas = 0
	pontos = 1000

	if (dificuldade == 1):
		tentativas = 20	
	elif (dificuldade == 2):
		tentativas = 10	
	elif (dificuldade == 3):
		tentativas = 5	
	else:
		print("Esse jogo não possui essa dificuldade. Saindo...")

	

	numero_magico = random.randrange(1, 101)

	jogadas = 1
	while(jogadas <= tentativas):
		print("Adivinhe o numero entre 1 e 100!\tpontos {}".format(pontos))

		print("Jogada {} de {} tentativas.".format(jogadas, tentativas))

		valor_escolhido = int(input())

		if (valor_escolhido < 1 and valor_escolhido > 100):
			print("Você digitou um valor fora do range solicitado.")
			print("Punição perde uma tentativa")
			print("Perde {} pontos.".format(100))
			pontos = pontos - 100
			continue


		acertou = valor_escolhido == numero_magico
		maior = valor_escolhido > numero_magico
		menor = valor_escolhido < numero_magico

		if(acertou):
			print("Você acertou! Parabéns!!!\t Você fez {} pontos\n".format(pontos))
			break
		elif(menor):
			pontos = subtraiPontos(pontos, tentativas)
			print("Valor menor do que o numero_magico\n")
		elif(maior):
			pontos = subtraiPontos(pontos, tentativas)
			print("Valor maior do que o numero_magico\n")
		
		jogadas = jogadas + 1

if __name__ == '__main__':
		adivinhacao()	
