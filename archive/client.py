import socket
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
    if not ret:
        print("Can't read frame.")
        continue

    frame = cv2.resize(frame, (1280, 720))
    command = b'detect'
    framebyte = frame.tobytes()
    shape = frame.shape
    height = bytes(str(shape[0]),'utf-8')
    width = bytes(str(shape[1]),'utf-8')
    send = command + b'bytesplitter' + framebyte + b'bytesplitter' + height + b'bytesplitter' + width
    msg = c.sendMsg(c.sock, send)
    
    feedback = c.recvMsg(c.sock)
    print(feedback.decode())

    # Show client frame
    cv2.imshow("client_cam", frame)
    if cv2.waitKey(1) == ord("q"):
        cap.release()

cv2.destroyAllWindows()