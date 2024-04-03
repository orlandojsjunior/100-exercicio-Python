# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Qual a distancia em metros que deseja converter: "))
cm = medida * 100
mm = medida * 1000
print("A conversão de {}mts para centimentros é {:.0f}cm e para milimentros é {:.0f}mm".format(medida, cm, mm))

# montrar com todas a medidas de (km ate mm).