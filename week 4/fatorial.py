num = int(input("Digite um número inteiro: "))
if num == 0:
  print(1)
else:
  resultado = 1
  while num > 0:
    resultado *= num
    num -= 1
  print(resultado)