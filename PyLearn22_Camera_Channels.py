import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("Kamerabild")


while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow("Kamerabild", frame)

    #Ein Farbbild beim Computer ist immer eine Zusammensetzung von drei Bildern Rot Gruen und Blau - RGB
    #Mit einem Split Befehl kann man ein Farbbild in drei Kanaele zerlegen
    #Wofuer? Nun es gibt sehr viele Anwengungen. Zum Beispiel so kann der Computer die Farbe bestimmen.
    #Angenommen, wir interessieren uns nur fuer die roten Legos. Ein rotes lego wird im Kanal 'rot' viel deutlicher
    #sichtbar as in den beiden anderen. Wenn man den Mittelwert aller Pixel in jedem der Bilder ausrechnet,
    #Kann man durch einen einfachen Vergleich die Farbe bestimmen.

    #Der Befehl split gibt drei bilder zurueck, die wir drei Variablen zuweisen b,g,r
    b, g, r = cv2.split(frame)

    cv2.imshow("Rot", r)
    cv2.imshow("Gruen", g)
    cv2.imshow("Blau", b)

    k = cv2.waitKey(1)

    # cv2.waitKey gibt eine Zahl zurueck. 27 steht fuer Escape-Taste
    if k == 27:
        # ESC pressed
        print("Escape gedruckt, beenden...")
        break

cam.release()

cv2.destroyAllWindows()