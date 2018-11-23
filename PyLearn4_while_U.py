#Uebung:
#

#Variablen initialisieren mit 0
L = 0
B = 0
A = 0

#Aendere die Bedingung so, dass die Schleife beendet wird, falls die berechnete Flaeche 0 ist
#Achtung! Aendere die Flaeche bei der Initialisierung auf einen anderen Wert, ansonsten
#ist die Schleife gleich zu Ende
while True:
   # Laenge und Breite abfragen
   L = int(input("Laenge eingeben: "))
   B = int(input("Breite eingeben: "))

   if L > 0 and B > 0:
      # Flaeche berechnen
      A = L * B
      # Ausgabe
      print("-----------------------------------")
      print("Flaeche :%d" % A)
      print("-----------------------------------")

   else:
      print("-----------------------------------")
      print("Eingabe(n) ungueltig")
      print("-----------------------------------")


