largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

count = altura
while count >= 1:
  if count == altura or count == 1:
    print("#" * largura)
  else:
    print("#" + " " * (largura-2) + "#")
  count -= 1