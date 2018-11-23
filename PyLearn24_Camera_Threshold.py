import cv2
cam = cv2.VideoCapture(0)

#Anfangs threshold
th = 127

while True:
    ret, frame = cam.read()
    if not ret:
        break

    #Neben ROI, das ein Bild in der X/Y-Dimension zuschneidet ist die Threshold-Funktion sehr wichtig.
    #Ein Threshold ist eine Heligkeitsschwelle. Damit kann man zu helle oder zu dunkle Werte abschneiden
    #So kann man z.B. ein Objekt von dem Hintergrund isolieren und somit eine der einfachsten Bilderkennungen
    #zu machen. Zum Beispiel:
    #Unser Fliessband ist Hell. Wenn wir die Helligkeitsschwelle so setzen, dass alle hellen Punkta ab einem
    #definierten Wert unsichtbar sind, dan sehen wir bei einem leeren Band nur ein Schwarzes Bild. Erscheint ein
    #Dunkleres Objekt, wird es als einziger sichtbar.

    #Fuer die threshold funktion brauchen wir ein Graubid
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grey", gray_image)

    #Bei dieser Art Schwelle erscheinen alle zu hellen punkte schwarz, alle unter der Schwelle - weiss
    ret, threshold1 = cv2.threshold(gray_image, th, 255, cv2.THRESH_BINARY_INV)

    # Bei dieser Art Schwelle erscheinen alle zu hellen punkte schwarz, alle unter der Schwelle sind ungeaendert
    ret, threshold2 = cv2.threshold(gray_image, th, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow("Threshold 1", threshold1)
    cv2.imshow("Threshold 2", threshold2)


    k = cv2.waitKey(1)

    # cv2.waitKey gibt eine Zahl zurueck. 27 steht fuer Escape-Taste
    if k == 27:
        # ESC pressed
        print("Escape gedruckt, beenden...")
        break

    #Mit der Taste + Threshod erhoehen
    elif k == ord('+'):
        th +=1

    # Mit der Taste - Threshod verkleinern
    elif k == ord('-'):
        th -= 1


cam.release()

cv2.destroyAllWindows()