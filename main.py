spieler_A=int(input("Wie viel Punkt hat erste Spieler?: "))
spieler_B=int(input("Wie viel Punkt hat zweite Spieler?: "))

if spieler_A>spieler_B:
  print("Erste Spieler hat gewonnen!")
if spieler_B>spieler_A:
  print("Zweite Spieler hat gewonnen!")
else:
  print("Unentschieden!")