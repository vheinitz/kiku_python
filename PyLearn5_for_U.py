#Die for-Schleife laeuft eine definierte Anzahl der Zyklen
#In der Schleife gibt es eine interne Variable, die den Wert automatisch aendert

#Variablen initialisieren mit 0
L = 0
B = 0
A = 0

#For-Schleife
for n in range(1, 3):
   print("---Berechnung Nr: %d ---------------\n" % n)
   #Laenge und Breite abfragen
   L = int(input("Laenge eingeben: "))
   B = int(input("Breite eingeben: "))

   #Flaeche berechnen
   A=L*B

   #Ausgabe

   print("Flaeche :%d" % A)
   print("-----------------------------------\n")
