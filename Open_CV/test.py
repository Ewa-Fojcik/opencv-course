import cv2
import numpy as np

# Wczytaj obrazek z internetu lub uzyj swojego
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Narysuj ksztalty
cv2.rectangle(img, (100, 100), (400, 400), (0, 255, 0), 3)
cv2.circle(img, (250, 250), 100, (255, 0, 0), -1)
cv2.putText(img, "Hello CV!", (150, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Pokaz obrazek
cv2.imshow("Test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()