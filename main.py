import random
import os


def repartir_carta():
  """Devuelve una carta aleatoria del mazo."""
  cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  carta = random.choice(cartas)
  return carta


def calcular_puntaje(cartas):
  """Toma una lista de cartas y devuelve la puntuación calculada a partir de las cartas"""

  #Si tiene blackjack (una mano con solo 2 cartas: as + 10), devuelve 0 en lugar del puntaje real. 0 representará blackjack en nuestro juego.
  if sum(cartas) == 21 and len(cartas) == 2:
    return 0
  #Si tiene un 11 (as). Y el puntaje ya supera los 21, elimina el 11 y reemplaza con un 1
  if 11 in cartas and sum(cartas) > 21:
    cartas.remove(11)
    cartas.append(1)
  return sum(cartas)


def comparar(puntaje_usuario, puntaje_crupier):
  """Compara los puntajes del crupier y el usuario"""

  if puntaje_usuario > 21 and puntaje_crupier > 21:
    return "\nTe pasas de 21 puntos, has perdido"


  if puntaje_usuario == puntaje_crupier:
    return "\nEmpataste, no ganas ni pierdes dinero esta vez!"
  elif puntaje_crupier == 0:
    return "\nEl crupier tiene BlackJack, tu pierdes!"
  elif puntaje_usuario == 0:
    return "\nTienes BlackJack, tu ganas!"
  elif puntaje_usuario > 21:
    return "\nTe pasas de 21 puntos, has perdido"
  elif puntaje_crupier > 21:
    return "\nEl crupier se pása de 21 puntos, tu ganas!"
  elif puntaje_usuario > puntaje_crupier:
    return "\nTienes mas puntos, has ganado!"
  else:
    return "\nEl crupier tiene mas puntos, has perdido!"

def jugar():


  #Reparte al usuario y al crupier 2 cartas cada uno, usando repartir_carta()
  jugador_cartas = []
  crupier_cartas = []
  is_game_over = False

  for _ in range(2):
    jugador_cartas.append(repartir_carta())
    crupier_cartas.append(repartir_carta())

  #El puntaje se deberá volver a verificarse con cada nueva carta extraída y las verificaciones en la deberán repetirse hasta que finalice el juego.

  while not is_game_over:
    #Si el crupier o el jugador tiene blackjack (0) o si la puntuación del jugador es superior a 21, el juego termina.
    puntaje_usuario = calcular_puntaje(jugador_cartas)
    puntaje_crupier = calcular_puntaje(crupier_cartas)
    print(f"\nTus cartas: {jugador_cartas}      - puntaje actual: {puntaje_usuario}")
    print(f"Cartas crupier: {crupier_cartas}    - puntaje actual: {puntaje_crupier}")

    if puntaje_usuario == 0 or puntaje_crupier == 0 or puntaje_usuario > 21:
      is_game_over = True
    else:
      #Si el juego no ha terminado, pregunta al jugador si quiere sacar otra carta. En caso afirmativo, agrega otra carta a la Lista jugador_cartas. Si no, entonces el juego ha terminado.
      jugador_nueva_carta = input(">>> Quieres pedir una carta o plantarte? (Escribe 'pedir' o 'plantarme'): ")
      if jugador_nueva_carta == "pedir":
        jugador_cartas.append(repartir_carta())
      else:
        is_game_over = True

  #El crupier debe seguir sacando cartas mientras tenga una puntuación inferior a 17.
  while puntaje_crupier != 0 and puntaje_crupier < 17:
    crupier_cartas.append(repartir_carta())
    puntaje_crupier = calcular_puntaje(crupier_cartas)

  print('\n                          << RESULTADOS FINALES >>')
  print(f"\nTu mano final: {jugador_cartas}          - puntaje final: {puntaje_usuario}")
  print(f"Crupier mano final: {crupier_cartas}       - puntaje final: {puntaje_crupier}")
  print(comparar(puntaje_usuario, puntaje_crupier))


if __name__ == "__main__":
  while input("\n\n############################################# Blackjack #############################################\n\nEscriba 'jugar' para comenzar o 'salir'  para salir del juego: ") == "jugar":
    os.system('clear')
    jugar()
