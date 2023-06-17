import socket
import json
import cv2
from custom_socket import CustomSocket

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

host = socket.gethostname()
port = 10011
c = CustomSocket(host, port)
c.clientConnect()

while cap.isOpened():

    ret, frame = cap.read()
    key = cv2.waitKey(1)
    if key == ord('r'):
        frame = cv2.resize(frame, (1280, 720))
        command = b'recog'
        framebyte = frame.tobytes()
        name = bytes(input(),'utf-8')
        shape = frame.shape
        height = bytes(str(shape[0]),'utf-8')
        width = bytes(str(shape[1]),'utf-8')
        send = command + b'bytesplitter' + framebyte + b'bytesplitter' + height + b'bytesplitter' + width + b'bytesplitter' + name
        msg = c.sendMsg(c.sock, send)
        
        feedback = c.recvMsg(c.sock)
        print(feedback.decode())

        continue

    cv2.imshow("client_cam", frame)
    if key == ord("q"):
        cap.release()

cv2.destroyAllWindows()