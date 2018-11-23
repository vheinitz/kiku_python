#Uebung:
#Aendere das Programm so, dass die Eingaben von L und B nur zwischen 1 und 10 gueltig sind.

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
   if L > 0 and B > 0 and L < 10 and B < 10 :
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
      
