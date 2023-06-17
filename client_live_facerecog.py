import socket
import json
import cv2
from custom_socket import CustomSocket


def list_available_cam(max_n):
    list_cam = []
    for n in range(max_n):
        cap = cv2.VideoCapture(n)
        ret, _ = cap.read()

        if ret:
            list_cam.append(n)
        cap.release()
    
    if len(list_cam) == 1:
        return list_cam[0]
    else:
        print(list_cam)
        return int(input("Cam index: "))


cap = cv2.VideoCapture(list_available_cam(10))
cap.set(4, 480)
cap.set(3, 640)

host = socket.gethostname()
port = 12304
c = CustomSocket(host, port)
c.clientConnect()

task = "detect"

while cap.isOpened():

    ret, frame = cap.read()
    cv2.imshow("client_cam", frame)

    if task == "register":
        name = input("name: ")

        res = c.register(frame, name)
        print(res)

        task = "detect"
    
    else:
        res = c.detect(frame)
        print("detect",res)
        # print("indexed", res['name'])

    # continue
    key = cv2.waitKey(1)
    if key == ord('r'):
        task = "register"
    if key == ord('d'):
        task = "detect"
    if key == ord("q"):
        cap.release()

cv2.destroyAllWindows()
