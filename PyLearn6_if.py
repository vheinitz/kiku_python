#Bedingung:
#Die 'Intelligenz' - d.h die Faehigkeit eine Entscheidung zu machen, bekommen die Programme durch die
# if-Abfragen. Die If-Abfragen verzweigen den Programmablauf
#Das untere Beispiel prueft, ob die Eingaben sinnig sind - groesser als 0
#Ansonsten wird die Flaeche nicht berechnet.

#Variablen initialisieren mit 0
L = 0
B = 0
A = 0

#Endlosschleife. Die bedingung ist imme Wahr (True) also endet die Schleife nie
while True:
   #Laenge und Breite abfragen
   L = int(input("Laenge eingeben: "))
   B = int(input("Breite eingeben: "))

   #Eingabe pruefen
   if L > 0 and B > 0:
      #Flaeche berechnen
      A=L*B

      #Ausgabe
      print("-----------------------------------")
      print("Flaeche :%d" % A)
      print("-----------------------------------")
   else:
      print("-----------------------------------")
      print("Eingabe(n) ungueltig")
      print("-----------------------------------")

