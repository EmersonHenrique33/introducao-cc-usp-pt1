import math
print("x² + bx + c")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
delta = b*b - 4*a*c

if delta < 0:
  print("esta equação não possui raízes reais")
else:
  x1 = (-b + math.sqrt(delta))/2/a
  x2 = (-b - math.sqrt(delta))/2/a
  if delta == 0:
    print(f"a raiz dupla desta equação é {x1}")
  else:
    if x1 < x2:
      print(f"as raízes da equação são {x1} e {x2}")
    else:
      print(f"as raízes da equação são {x2} e {x1}")
