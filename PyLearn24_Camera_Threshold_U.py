import cv2
cam = cv2.VideoCapture(0)

#Anfangs threshold
th = 127

while True:
    ret, frame = cam.read()
    if not ret:
        break

    #Aufgabe!
    #Versuche jetzt ROI und threshold zu verbinden. Schneide nur das Stueck vom Band unter der Kamera mit ROI und
    #Setze Threshold so, dass das Bid nur dann nicht schwarz ist, wenn ein Lego unter der Kamera vorbei faehrt.

    #Speichere das Bild automatisch, wenn die Variable Objektpixel einen definierten Wert ueberschreitet



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

    Objektpixel = cv2.countNonZero(threshold1)
    print (Objektpixel)

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