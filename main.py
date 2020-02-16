import cv2
from mtcnn.mtcnn import MTCNN
import math
from matplotlib import pyplot as plt
import fpdf

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
detector = MTCNN()
data = list()

while True:
    ret, img = cap.read()
    faces = detector.detect_faces(img)
    i = 0
    all = len(faces)
    intrested = 0
    for face in faces:
        i += 1
        x = (face['box'][0] + face['box'][0] + face['box'][2]) // 2  # центр бокса лица
        dist_l = abs(face['keypoints']['nose'][0] - face['keypoints']['left_eye'][0])
        dist_r = abs(face['keypoints']['nose'][0] - face['keypoints']['right_eye'][0])

        if dist_l < dist_r:
            u = dist_l / dist_r * 90
        else:
            u = dist_r / dist_l * 90

        try:
            l = (1280 - face['box'][2] - face['box'][0]) * 2.5
            l2 = abs(640 - x)
            u1 = math.atan(l / l2) * 57.7
        except ZeroDivisionError:
            u1 = 0

        if u + 10 > u1 > u - 10:
            intrested += 1
    try:
        data.append(intrested / all)
    except ZeroDivisionError:
        data.append(0)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        time = [i for i in range(len(data))]
        plt.bar(time, data)
        plt.xlabel("Time")
        plt.ylabel("Intrested")
        plt.savefig('dio.png')
        break
fpdf.pdf()

cap.release()
cv2.destroyAllWindows()
