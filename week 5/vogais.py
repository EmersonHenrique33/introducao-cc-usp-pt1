def vogal(letra):
  letra = letra.casefold()
  if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    return True
  else:
    return False

print(vogal("O"))