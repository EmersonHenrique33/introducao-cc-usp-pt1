import math

x1 = int(input("Digite o valor de x-1: "))
y1 = int(input("Digite o valor de y-1: "))
x2 = int(input("Digite o valor de x-2: "))
y2 = int(input("Digite o valor de y-2: "))

distancia = math.sqrt(pow(abs(x1-x2), 2) + pow(abs(y1-y2), 2))

if distancia >= 10:
  print("longe")
else:
  print("perto")