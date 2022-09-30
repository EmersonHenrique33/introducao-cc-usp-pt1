def verifica_valor(inicio, final, frase, fraseErro):
  while True:
    try:
      valor = int(input(frase))
      if inicio <= valor <= final:
        return valor
      else:
        print(fraseErro)
    except ValueError:
      print("Valor incorreto. Tente novamente")

def computador_escolhe_jogada(pecas_total, pecas_retirar):
  retira = 1
  while retira <= pecas_retirar:
    copia_total = pecas_total
    copia_total -= retira
    if copia_total%(pecas_retirar + 1) == 0:
      return retira
    else:
      retira += 1
    

def usuario_escolhe_jogada(pecas_total, pecas_retirar):
  retira = verifica_valor(1, pecas_retirar, "Quantas peças você vai tirar: ", "\nOops! Jogada inválida! Tente de novo.\n")
  return retira

def definicao_inicio(pecas_total, pecas_retirar):
  if pecas_total % (pecas_retirar + 1) == 0:
    return False
  else:
    return True

def partida():
  pecas_total = verifica_valor(1, 100, "\nQuantas peças: ", "Valores incorretos, tente novamente")
  pecas_retirar = verifica_valor(1, pecas_total, "Limite de peças por jogada: ", "Valores incorretos, tente novamente")
  inicio = definicao_inicio(pecas_total, pecas_retirar)

  if inicio:
    print("\nComputador começa!")
    while True:
      jogada_pc = computador_escolhe_jogada(pecas_total, pecas_retirar)
      pecas_total -= jogada_pc
      print(f"\nO computador tirou {jogada_pc} peça")

      if pecas_total == 0:
        return True
      else:
        print(f"Agora restam {pecas_total} peças no tabuleiro\n")
      
      jogada_usuario = usuario_escolhe_jogada(pecas_total, pecas_retirar)
      pecas_total -= jogada_usuario
      print(f"\nVocê tirou {jogada_usuario} peças")
      print(f"Agora restam {pecas_total} peças no tabuleiro")
  else:
    print("\nVocê começa!\n")
    while True:
      jogada_usuario = usuario_escolhe_jogada(pecas_total, pecas_retirar)
      pecas_total -= jogada_usuario
      print(f"\nVocê tirou {jogada_usuario} peças")
      print(f"Agora restam {pecas_total} peças no tabuleiro")

      jogada_pc = computador_escolhe_jogada(pecas_total, pecas_retirar)
      pecas_total -= jogada_pc
      print(f"\nO computador tirou {jogada_pc} peça")

      if pecas_total == 0:
        return True
      else:
        print(f"Agora restam {pecas_total} peças no tabuleiro\n")


def menu():
  while True:
    menu = verifica_valor(1, 3, """\nBem-vindo ao jogo do NIM! Escolha:

    1 - para jogar uma partida isolada
    2 - para jogar um campeonato
    3 - sair\n\n--> """, "Escolha uma opção válida")

    if menu == 1:
      if partida():
        print("Fim do jogo! O computador ganhou!")
        break
    elif menu == 2:
      print("\nVocê escolheu um campeonato!")
      count = 1
      while count <= 3:
        print(f"\n*** Rodada {count} ***")
        if partida():
          print("Fim do jogo! O computador ganhou!")
        count += 1
      print("\n*** Final do campeonato! ***")
      print("\nPlacar: Você 0 x 3 Computador")
      break
    elif menu == 3:
      break
    
menu()
