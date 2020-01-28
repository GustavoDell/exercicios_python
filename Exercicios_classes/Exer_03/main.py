from Exer_03 import Retangulo

comprimento = float(input("Informe a comprimento do retangulo:"))
largura = float(input("Informe a largura do retangulo:"))

retangulo = Retangulo(comprimento, largura)
perimetro = retangulo.calcular_perimetro()

print("Deverá ser comprado um total de {} m²".format(perimetro))



    