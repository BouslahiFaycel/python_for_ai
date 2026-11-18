import cv2

image = cv2.imread("test_visages.png")

if image is None:
   print("Erreur : test_visages.png introuvable")
else:
   cv2.imshow("Mon image", image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()