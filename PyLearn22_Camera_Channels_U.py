import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("Kamerabild")


while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow("Kamerabild", frame)

    #Aufgabe!
    #Aendere den Quellcode so, dass nur ein Fenster mit dem Kanal Bau sihtbar ist

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