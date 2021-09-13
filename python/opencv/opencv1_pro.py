import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)
cx, cy, w, h = 100, 100, 200, 200

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # 镜像翻转相机
    lmList, img = detector.findHands(img)  # ****

    if lmList:

        l, _, _ = detector.findDistance(lmList[0]['lmList'][8], lmList[0]['lmList'][12], img) #中指和食指
        print(l)
        if l<50:
        # try:
            cursor = lmList[0]['lmList'][8]
            # except:
            #     print('chucuo')

            if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
                colorR = (0, 255, 0)
                cx, cy = cursor
            else:
                colorR = (255, 0, 255)

    cv2.rectangle(img, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)

    cv2.imshow("image", img)
    cv2.waitKey(1)
