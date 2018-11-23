import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("Kamerabild")
cv2.namedWindow("ROI")


while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow("Kamerabild", frame)

    #Hier geht es weiter mit einem neuen sehr wichtigen Thema - ROI
    #ROI bedeutet Region of Interest, ein Bereich im Bild, das uns interessiert.
    #Wenn man ein Bild analysiert, interessiert man sich oft nicht fuer das ganze Bild
    #sondern nur fuer ein Bildbereich. Zum Beispiel, eine Ueberwachungskamera kann einen Tor und ein Stueck vom
    #Garten erfassen. Nehmen wir mal an, die Software, die das Bild analysiert reagiert auf die Bewegung.
    #Wenn man das ganze Bild analysiert, wird es oft Fehlalarm geben, weil z.B. die Beume sich bewegen.
    #Wenn man zu analysierenden Bereich nur auf den Eingan beschraenkt, wird es deutlich weniger Fehler geben.

    #Hier wird ein Auschnitt von dem Kamerabild verwendet
    #Der Syntax ist: <EinBild>[<Zeile oben>:<Zeile unten>,<Spalte links>:<Spalte rechts>]
    lego_bereich=frame[200:500, 300:400]

    #Das ROI-Bild wird angezeigt
    cv2.imshow("ROI", lego_bereich)


    k = cv2.waitKey(1)

    # cv2.waitKey gibt eine Zahl zurueck. 27 steht fuer Escape-Taste
    if k == 27:
        # ESC pressed
        print("Escape gedruckt, beenden...")
        break

cam.release()

cv2.destroyAllWindows()