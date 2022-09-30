num = int(input("Digite um valor inteiro: "))

soma = 0
resto = 10
div = 1
count = num
while count > 1:
  soma += (num%resto)//div
  resto *= 10
  div *= 10
  count /= 10
print(soma)