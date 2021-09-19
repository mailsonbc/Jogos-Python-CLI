import random
#class color:
#   PURPLE = '\033[95m'
#  CYAN = '\033[96m'
#   DARKCYAN = '\033[36m'
#   BLUE = '\033[94m'
#  GREEN = '\033[92m'
#   YELLOW = '\033[93m'
#   RED = '\033[91m'
#   BOLD = '\033[1m'
#   UNDERLINE = '\033[4m'
#   END = '\033[0m'

#print(color.UNDERLINE + 'Hello World !' + color.END)

#print("   |")
#print("   |")
#print("  " + color.UNDERLINE +"O" + color.END)
#print(" /|\\")
#print(" / \\")
#====================================================================================================

erros = 0                        #variavel para contar os erros
indice = random.randrange(0, 9)  #número aleatório para escolher a palavra aleatoriamente

#lista de palavras a ser adivinhadas
palavras = ["morango", "abacaxi", "banana", "manga", "uva", "melancia","goiaba", "cajamanga", "melao", "maracuja"]


palavra_secreta = palavras[indice]     #variavel contendo a palavra a ser adivinhada
palavra_certa = ""                     #variavel que vai receber a letras escolhidas pelo jogador
acerto = ""                            #variavel que vai receber somente as letras corretas (ainda a ser implementado a ordenação das letras)

print(indice)
print(palavra_secreta)



while erros < 5:
   palavra_certa = input("Tente adivinhar a palavra, escolha uma letra: ")
   if (palavra_certa in palavra_secreta):
      acerto = acerto + palavra_certa
      print(acerto)
      #if (acerto)
   else:        
      erros = erros + 1
   print(palavra_certa)
   print(erros)

