import cv2

# Chargement du détecteur
detecteur = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Ouverture de la caméra
camera = cv2.VideoCapture(0)

while True:

    ret, image = camera.read()

    if not ret:
        break

    # Conversion en niveaux de gris
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Détection des visages
    visages = detecteur.detectMultiScale(
        gris,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Dessiner un rectangle autour des visages
    for (x, y, w, h) in visages:
        cv2.rectangle(
            image,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

    cv2.imshow("Detection des visages", image)

    # Quitter avec la touche Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()