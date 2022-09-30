num = int(input("Digite um número natural: "))

count = 1
div = 0
while count <= num:
  if num%count == 0:
    div += 1
  if div == 3:
    break
  else:
    count += 1
if div == 2:
  print("primo")
else:
  print("não primo")