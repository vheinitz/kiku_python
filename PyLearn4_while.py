#Es gibt in Python zwei Arten von Schleifen while und for
#Bei der While-Schleife werden die Befehle in der Schleife ausgefuehrt,
#Solange die Bedingung wahr ist.
#Durch die Einrueckung sagt man, welche Befehle zu der Schleife gehoeren
#Hier das vorherige Beispiel, was jedoch endlos laeuft

#Variablen initialisieren mit 0
L = 0
B = 0
A = 0

#Endlosschleife. Die bedingung ist imme Wahr (True) also endet die Schleife nie
while True:
   #Laenge und Breite abfragen
   L = int(input("Laenge eingeben: "))
   B = int(input("Breite eingeben: "))

   #Flaeche berechnen
   A=L*B

   #Ausgabe
   print("-----------------------------------")
   print("Flaeche :%d" % A)
   print("-----------------------------------")
