import random

numero = random.randrange(0, 10)

print("Tente adivinhar o número secreto." )
adivinha = int(input("Digite um número entre 0 e 10: "))


if  (adivinha == numero):
    print("Acertou!!!!")
else:
    print("Errou. O número é: %d " %numero)
    print("Perdeu!!!")

print("Aperte qualquer tecla para encerrar: ")
input()