num = int(input("Digite um número inteiro: "))

resto = 10
div = 1
count = num
teste = False

while count > 1:
  valorPrimeiro = (num%resto)//div
  valorSecundario = (num%(resto*10))//(div*10)
  if valorPrimeiro == valorSecundario:
    teste = True
    break
  else:
    resto *= 10
    div *= 10
    count /= 10

if teste:
  print("sim")
else:
  print("não")