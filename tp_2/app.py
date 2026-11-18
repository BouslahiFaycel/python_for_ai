import cv2

image = cv2.imread("renard.png")

if image is None:
 print("Image introuvable")

else:
 gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 cv2.imshow("Originale", image)
 cv2.imshow("Niveaux de gris", gris)
 cv2.waitKey(0)


cv2.destroyAllWindows()