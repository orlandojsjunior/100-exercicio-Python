# Exerc�cio Python 006: Crie um algoritmo que leia um n�mero e mostre o seu dobro, triplo e raiz quadrada.

nun = int(input('Digite o numero: '))
dobro = nun * 2
triplo = nun * 3
raiz_quadrada = nun ** (1/2)

print('Esse e o seu dobro {}. \n Seu triplo {}. \n 10E sua raiz quadrada {:.2f}'.format(dobro, triplo, raiz_quadrada))