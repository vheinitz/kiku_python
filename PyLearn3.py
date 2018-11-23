#Eingabe wird mit dem Befehl input gemacht. Man wird es jedoch selten benutzen.
#Meistens bekommen die Programme heutzutage die Eingabe von der graphischen Oberflaeche,
#aus den Dateien oder als Startparameter beim Start des Programms.

#Unten ist ein Beispiel fuer die Berechnung der Flaeche, bei dem der Benutzer die
#Breite und die Laenge eingeben muss

#Variablen initialisieren mit 0
L = 0
B = 0
A = 0

#Endlosschleife
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

#Programm zu Ende
