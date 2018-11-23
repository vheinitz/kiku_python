# Wir importieren das Modul OpenCV. In Python ist der Name der Moduls cv2.
# Das ist ein Modul fuer die Bildverarbeitung
import cv2

# Von dem Modul OpenCV benutzen wor die Klasse VideoCapture.
# VideoCapture - ist eine Klasse zum Lesen der Daten von einer Kamera.
# Die Nummer 1 bedeutet, wir benutzen die 2-te Kamera, die an das PC angeschlossen ist.
# By Python und den meisten anderen Programmiersprachen beginnt die Zaehlung immer von 0
# D.h. gibt es am PC mehrere Kameras, ist die erste cv2.VideoCapture(0)
# Die zweite cv2.VideoCapture(1) usw.
# Eine Klasse - ist eine Schablone, wie man ein Objekt erstellt.
# cam - ist das erzeugte Objekt von der Klasse cv2.VideoCapture
# Wir haben das Objekt erzeugt, und koennen es nun nutzen
cam = cv2.VideoCapture(0)

# Fuer die Anzeige underer Bilder brauchen wir ein Fenster.
# Mit dem unteren Befehl bereiten wir ein Fenster vor. Das Fenster koennen wir
# unter dem Namen "Kamerabild" weiter nutzen
cv2.namedWindow("Kamerabild")

#Variable zum inkrementieren,
n=0

# Nun beginnen wir eine Schleife, die von sich aus nie endet
while True:
    # Nun benutzen wir oben erzeugte Objekt cam und rufen eine Funktion von dem Objekt auf read()
    # Diese Funktion liefert uns zurueck zwei neue Objekte:
    #   ret - ist eine Zahl, sie sagt und ob alles in Ordnung war oder ein Fehler auftrat
    #   frame - ist ein Bild, das die Kamera gerade aufnahm.
    ret, frame = cam.read()

    # Als erstes nach dem aufruf einer Funktion pruefen wir, ob alles in ordnung war
    # Die untere Pruefung beendet die Schleife, wenn der Wert von ret nicht True ist
    if not ret:
        break  # Ein break bricht die Schleife ab, in der es aufgerufen wird


    # Wenn wir immer noch da sind, dann war ret = 0 und das Lesen des Punktes in Ordnung war
    # Wir zeigen das Bild frame im Fenster Kamerabild an
    cv2.imshow("Kamerabild", frame)

    # Damit man eine Chance hat, das Programm zu beenden, liest man die Tastatur ab und speichert das Ergebnis
    # in der Variable k ab
    k = cv2.waitKey(1)

    # cv2.waitKey gibt eine Zahl zurueck. 27 steht fuer Escape-Taste
    if k == 27:
        # ESC pressed
        print("Escape gedruckt, beenden...")
        break

    # cv2.waitKey gibt eine Zahl zurueck. 32 steht fuer die Leertaste
    elif k == 32: 
        # Wenn Leertaste gedruckt, wird das aktuelle Bild unter dem Angegebenen Pfad gespeichert
        #Die Variable n wird benutzt, damit die Bilder unterschiedliche Namen haben
        cv2.imwrite("C:/Users/KiKu Arduino/Desktop/Bilder/Camerabild_%03d.png" % n, frame)
        n += 1 #Wert von n erhoehen

# while-Schleife ist hier zu Ende, entweder weil beim LEsen der Kamera was schief ging oder
# weil der Benutzer Escape-Taste gedruckt hat
# Camera-objekt wird geloescht und die KAmera fuer andere Anwendungen frei gegeben
cam.release()

# Alle von diesem Programm erzeugten Fenster werden geschlossen
cv2.destroyAllWindows()