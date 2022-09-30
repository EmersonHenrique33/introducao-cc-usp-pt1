from shutil import which


num = int(input("Digite um valor inteiro: "))
count = 1
while num >= 1:
  if count % 2 != 0:
    print(count)
    num -= 1
  count += 1