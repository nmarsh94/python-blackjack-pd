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

  #Si tiene blackjack (una mano con solo 2 cartas: as + 10)
  if sum(cartas) == 21 and len(cartas) == 2:
    return 21
  #Si tiene un 11 (as). Y el puntaje ya supera los 21, elimina el 11 y reemplaza con un 1
  if 11 in cartas and sum(cartas) > 21:
    cartas.remove(11)
    cartas.append(1)
  return sum(cartas)


def comparar(puntaje_usuario, puntaje_crupier, saldo_actual, saldo_objetivo, apuesta):
  """Compara los puntajes del crupier y el usuario"""

  gana_jugador = saldo_actual + apuesta
  gana_jugador_bj = saldo_actual + (apuesta / 2) + apuesta
  gana_crupier = saldo_actual - apuesta


  if puntaje_usuario > 21 and puntaje_crupier > 21:
    print("\nTe pasas de 21 puntos, has perdido")
    jugar(gana_crupier,saldo_objetivo,0)

  if puntaje_usuario == puntaje_crupier:
    print("\nEmpataste!")
    jugar(saldo_actual,saldo_objetivo,0)
  elif puntaje_crupier == 21:
    print("\nEl crupier tiene BlackJack, tu pierdes!")
    jugar(gana_crupier,saldo_objetivo,0)
  elif puntaje_usuario == 21:
    print("\nTienes BlackJack, tu ganas!")
    jugar(gana_jugador_bj,saldo_objetivo,0)
  elif puntaje_usuario > 21:
    print("\nTe pasas de 21 puntos, has perdido")
    jugar(gana_crupier,saldo_objetivo,0)
  elif puntaje_crupier > 21:
    print("\nEl crupier se pása de 21 puntos, tu ganas!")
    jugar(gana_jugador,saldo_objetivo,0)
  elif puntaje_usuario > puntaje_crupier:
    print("\nTienes mas puntos, has ganado!")
    jugar(gana_jugador,saldo_objetivo,0)
  else:
    print("\nEl crupier tiene mas puntos, has perdido!")
    jugar(gana_crupier,saldo_objetivo,0)

def jugar(saldo_actual, saldo_objetivo, apuesta):

  print ("\n\n############################################### Blackjack ###############################################\n\n")

  if (saldo_actual >= saldo_objetivo):
    print ("\n<<<< Felicidades, hiciste:  " + str(saldo_actual) + " y tu objetivo era llegar a: " + str(saldo_objetivo) + ". Ganaste todo el juego, bien hecho! >> >> \n\n\n")
    mensaje_final=input("\nFin del juego, ¿quieres volver a jugar? escriba \"Sí\" o \"No\"\n") 
    if mensaje_final == 'si':
      menu_principal()
    elif mensaje_final == 'no':
      return exit()
  elif saldo_actual <= 0:
    mensaje_final=input("\nHas, perdido, fin del juego, ¿quieres volver a jugar? escriba \"Sí\" o \"No\"\n") 
    if mensaje_final == 'si':
      menu_principal()
    elif mensaje_final == 'no':
      return exit()

  elif apuesta == 0:
    print ("\n-> Saldo actual que tienes hasta el objetivo: " + str(saldo_actual) + " / " + str(saldo_objetivo))
    cantidad_a_apostar = float(input("Ingrese la cantidad a apostar en el próximo juego: "))
    if (cantidad_a_apostar < 1 or cantidad_a_apostar > saldo_actual):
      print("<<No es un monto de apuesta válido, ingrese más de 0 y menos de su saldo restante>> \n")
      jugar(saldo_actual , saldo_objetivo, apuesta=0)
    else:
      print("\n<<Apuesta aceptada!>> \n")
      jugar(saldo_actual , saldo_objetivo, cantidad_a_apostar)

  #Reparte al usuario y al crupier 2 cartas cada uno, usando repartir_carta()
  is_game_over = False

  jugador_cartas = [repartir_carta() for x in range(2)]
  crupier_cartas = [repartir_carta() for x in range(2)]

  #El puntaje se deberá volver a verificarse con cada nueva carta extraída y las verificaciones en la deberán repetirse hasta que finalice el juego.

  while not is_game_over:
    #Si el crupier o el jugador tiene blackjack  o si la puntuación del jugador es superior a 21, el juego termina.
    puntaje_usuario = calcular_puntaje(jugador_cartas)
    puntaje_crupier = calcular_puntaje(crupier_cartas)
    print(f"\nCartas crupier: {crupier_cartas[0]}")
    print(f"Tus cartas: {jugador_cartas}      - puntaje actual: {puntaje_usuario}")

    if puntaje_usuario == 21 or puntaje_crupier == 21 or puntaje_usuario > 21:
      is_game_over = True
    else:
      #Si el juego no ha terminado, pregunta al jugador si quiere sacar otra carta. En caso afirmativo, agrega otra carta a la Lista jugador_cartas. Si no, entonces el juego ha terminado.
      jugador_nueva_carta = input(">>> Quieres pedir una carta o plantarte? (Escribe 'p' para pedir o 'pl' para plantarte): ")
      if jugador_nueva_carta == "p":
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
  print(comparar(puntaje_usuario, puntaje_crupier, saldo_actual, saldo_objetivo, apuesta))


def reglas():
  fileObject = open("reglas.txt", "r")
  data = fileObject.read()
  print(data)

def menu_principal():

  while(True):
    print ("\n\n**************************************************************************************************************\n\n")
    saldo_objetivo = 0
    try:
      saldo_objetivo = float(input("Ingrese el saldo objetivo para ganar, ( comienza con la mitad de éste saldo. Objetivo de saldo mínimo de 20:  "))
    except:
        print('Entrada incorrecta. Por favor, introduzca un número ...')

    if saldo_objetivo > 19:
      menu_blackjack(saldo_objetivo)
    else:
        print('Ingrese un saldo válido de al menos 20 para su objetivo')



def menu_blackjack(saldo_objetivo):
    loop = True
    while loop:
      print ("\n\n**************************************************************************************************************\n\n")
      
      accion = input("\nEscriba 'jugar' para comenzar, 'reglas' para ver las reglas  o 'salir'  para salir del juego: ").strip()
        
      os.system('clear')
      saldo_actual = saldo_objetivo/2
      if accion == 'jugar':
        jugar(saldo_actual, saldo_objetivo,0)
      elif accion == 'reglas':
        reglas()
      elif accion == 'salir':
        exit() 
      else:
        print("Seleccione una opcion valida")  
    

if __name__ == "__main__":
  print(logo)
  menu_principal()
    
