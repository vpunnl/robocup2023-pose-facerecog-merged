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
portface = 12304
portpose = 12302
cface = CustomSocket(host, portface)
cface.clientConnect()

cpose = CustomSocket(host, portpose)
cpose.clientConnect()

task = "pose"

seen_index = [] #index of person alrd sent to be detected
tracking_id = -1

while cap.isOpened():

    ret, frame = cap.read()
    cv2.imshow("client_cam", frame)

    if not ret:
        print("Ignoring empty camera frame.")
        continue


    # all ID presented in the camera
    msg = cpose.req(frame)
    
    # Detect if new id is target
    for key,value in msg.items():
        if cv2.waitKey(0) == ord("t"):

            idInput = str(input("Track ID : "))
            while idInput not in msg.keys():
                idInput = str(input("Track ID : "))

            tracking_id = idInput
            for key,value in msg.items():
                id = key
                if id == tracking_id:
                    x1,y1,x2,y2 = value['box']
                    #crop frame is the face of that tracking id
                    register_cropped_frame = frame[y1:y2, x1:x2]
                    out = cface.register(register_cropped_frame, "target")
                    print("out", out)
        id = key
        if id not in seen_index:
            # Those who hasnt been seen, detect whether the name is target
            
            x1,y1,x2,y2 = value['box']
            cropped_frame = frame[y1:y2, x1:x2]

            msg2 = cface.detect(cropped_frame)
            print('Msg2 : ', msg2)
            if msg2['name'] == "target":
                tracking_id = id
            else:
                pass
            print("seen index : ",seen_index)
            seen_index.append(id)
        else:
            pass

        print(f"Tracking : {tracking_id}")
    
                
    # if task == "recog":

    #     print(f"Tracking : {trackId}")
    
    # else:
    #     res = cface.detect(frame)
    #     print(res)

    # # continue
    # key = cv2.waitKey(1)
    # if key == ord('r'):
    #     task = "recog"
    # if key == ord('p'):
    #     task = "pose"
    # if key == ord("q"):
    #     cap.release()

cv2.destroyAllWindows()
