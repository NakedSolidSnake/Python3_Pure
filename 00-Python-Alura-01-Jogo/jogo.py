import adivinhacao

def main():
	while(True):
		print("************************************************")
		print("**************Combo Pack Games******************")
		print("************************************************")

		print("Selecione o jogo: ")
		print("[1] - Adivinhação")
		print("[2] - Forca")
		print("[0] - Sair")

		jogo = int(input())

		if(jogo == 0):
			print("Saindo do menu de jogos")
			break
		elif(jogo == 1):
			print("Adivinhação selecionado.")
			adivinhacao.adivinhacao()
		elif(jogo == 2):
			print("Não Implementado")
		else:
			print("Opção não existente. Por favor selecione uma opção válida.")

if __name__ == '__main__':
	main()
