import random
import os
from art import logo


def repartir_carta():
  """Devuelve una carta aleatoria del mazo."""

  cartas = {'A': 11, 'Dos': 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5, 'Seis': 6, 'Siete': 7, 'Ocho': 8, 'Nueve': 9, 'Diex': 10, 'J': 10, 'Q': 10, 'K': 10}
  maso_cartas = [carta for carta in cartas.values()]
  carta = random.choice(maso_cartas)
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
    return "\nEmpataste!"
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

  print(logo)

  #Reparte al usuario y al crupier 2 cartas cada uno, usando repartir_carta()
  is_game_over = False

  jugador_cartas = [repartir_carta() for x in range(2)]
  crupier_cartas = [repartir_carta() for x in range(2)]

  #El puntaje se deberá volver a verificarse con cada nueva carta extraída y las verificaciones en la deberán repetirse hasta que finalice el juego.

  while not is_game_over:
    #Si el crupier o el jugador tiene blackjack (0) o si la puntuación del jugador es superior a 21, el juego termina.
    puntaje_usuario = calcular_puntaje(jugador_cartas)
    puntaje_crupier = calcular_puntaje(crupier_cartas)
    print(f"\nCartas crupier: {crupier_cartas[0]}")
    print(f"Tus cartas: {jugador_cartas}      - puntaje actual: {puntaje_usuario}")

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
  print(f"\nCrupier mano final: {crupier_cartas}       - puntaje final: {puntaje_crupier}")
  print(f"Tu mano final: {jugador_cartas}          - puntaje final: {puntaje_usuario}")
  print(comparar(puntaje_usuario, puntaje_crupier))


def reglas():
  fileObject = open("reglas.txt", "r")
  data = fileObject.read()
  print(data)

if __name__ == "__main__":
  loop = True
  while loop:
    print ("\n\n############################################# Blackjack #############################################\n\n")
    accion = input("Escriba 'jugar' para comenzar, 'reglas' para ver las reglas  o 'salir'  para salir del juego: ")
    os.system('clear')

    if accion == 'jugar':
      jugar()
    elif accion == 'reglas':
      reglas()
    elif accion == 'salir':
      loop = False
    else:
      print("Seleccione una opcion valida")  
    
