import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("Kamerabild")
cv2.namedWindow("ROI")


while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow("Kamerabild", frame)

    #Aufgabe! Versuche den Ausschnitt vom Fliessband als ROI zu setzen, in dem ein Lego unter  der Kamera
    #vorbeilaeuft.

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