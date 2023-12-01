# Exercicio Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.

n1 = float(input("Digite a nota da AV1: "))
n2 = float(input("Digite a nota da AV2: "))
media = (n1 + n2) / 2

print("Sua media é: {}".format(media))

# Implementação de codigo | if-else para verificar se a média é maior ou igual a 7, e mostrar uma mensagem de aprovado ou reprovado.

if media >= 7:
    print("Parabens, você foi aprovado!")
else:
    print("Infelizmente você foi reprovado.")

