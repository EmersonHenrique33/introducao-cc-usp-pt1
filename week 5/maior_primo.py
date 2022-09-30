def maior_primo(num):
  while num > 1:
    div = 0
    control = num

    while control >= 1:
      if num % control == 0:
        div += 1
      if div == 3:
        break
      else:
        control -= 1

    if div == 2:
      return num
    else:
      num -= 1