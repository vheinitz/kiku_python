import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("Kamerabild")


while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow("Kamerabild", frame)

    #Sehr oft, spielt die Farbe bei der Bilderkennung keine Rolle. Die Farben sind einfach nicht zuverlaessig.
    #Jede kamera nimmt die Farben etwas unterschiedlich und sogar kann die gleiche Kamera die Farben unterschiedlich
    #darstellen, wenn sie sich erwaermt.
    #Deshalb gehen die meisten Agorithmen in der Bilderkennung nach der Form. Und da wir die Farbe fuer die Formerkennung
    #nicht brauchen, wolen wir auch nicht drei R,G,B Bilder haben sondern nur ein Graubild.


    #Der Befehl split gibt drei bilder zurueck, die wir drei Variablen zuweisen b,g,r
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grey", gray_image)


    k = cv2.waitKey(1)

    # cv2.waitKey gibt eine Zahl zurueck. 27 steht fuer Escape-Taste
    if k == 27:
        # ESC pressed
        print("Escape gedruckt, beenden...")
        break

    #Mit der Taste i kann man sich hier die Dimensionen des Bildes anzeigen lassen
    if k == ord('i'):
        # Info
        print ("Farbbild: " , frame.shape)
        print ("Graubild: " , gray_image.shape)


cam.release()

cv2.destroyAllWindows()