import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)

detector = FaceDetector()

while True:
    success, img = cap.read()
    img, bbox = detector.findFaces(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
