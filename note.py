dicts = {'3': 'NA', '4' : 'NA'}

# while True:
#     x = input("x :")
#     if x in [key for key,val in dict.items()]:
#         False

    
# idInput = str(input("inp : "))
# while idInput not in dicts.keys():
#     idInput = input("inp loop : ")
# print("passed")

# for i,y in dicts.items():
#     print(i,y)

# res = {'1':{'box': [68,174,525,480],'pose': 'NA'},
#        '2':{'box': [102,267,241,442],'pose': 'NA'}
#        }

# for key,value in res.items():
#     id = key
#     x1,y1,x2,y2 = value['box']
#     print(id,x1,y1,x2,y2)


tem = {'1':'hi'}
if tem :
    print('hi')
print('yo')


# ------------BEFORE MODs------------------
# import socket
# import json
# import cv2
# from custom_socket import CustomSocket


# def list_available_cam(max_n):
#     list_cam = []
#     for n in range(max_n):
#         cap = cv2.VideoCapture(n)
#         ret, _ = cap.read()

#         if ret:
#             list_cam.append(n)
#         cap.release()
    
#     if len(list_cam) == 1:
#         return list_cam[0]
#     else:
#         print(list_cam)
#         return int(input("Cam index: "))


# cap = cv2.VideoCapture(list_available_cam(10))
# cap.set(4, 480)
# cap.set(3, 640)

# host = socket.gethostname()
# portface = 12304
# portpose = 12302
# cface = CustomSocket(host, portface)
# cface.clientConnect()

# cpose = CustomSocket(host, portpose)
# cpose.clientConnect()

# task = "pose"

# seen_index = [] #index of person sent to detect
# tracking_id = -1

# while cap.isOpened():

#     ret, frame = cap.read()
#     cv2.imshow("client_cam", frame)

#     msg = cpose.req(frame)
    
#     # Detect if new id is target
#     for id in msg.keys():
#         if id not in seen_index:
#             msg2 = cface.detect(frame)
#             x , y = msg2.items()
#             if str(y) == "target": 
#                 tracking_id = id
#             else:  
#                 # id is not the target
#         # else:
#             # * already seen id
#             # pass
    
#     # if cv2.waitKey(0) == ord("t"):
#     #     input id .. 
#     #     cface.register(crop_frame, "target")
#     #     tracking_id = input_id
        
#     if task == "recog":
#         if not ret:
#             print("Ignoring empty camera frame.")
#             continue

#         idInput = str(input("Track ID : "))
#         while idInput not in msg.keys():
#             idInput = str(input("Track ID : "))

#         id = int(input("Track ID :"))

#         #---GET POSE TO SEND THE CROPPED IMG (the same id as inputted) TO RECOG
#         # cface.register(crop_frame, "target")

#         #---RECOG NORMALLY RETURN THE NAME BUT NOW RETURN what??

#         #--NEW PERSON WALKS IN, IF NAME IN "TARGET", DETECT BY RECOG --> CHANGE TRACK ID

#         # trackId = 0
#         print(f"Tracking {trackId}")
    
#     else:
#         res = cface.detect(frame)
#         print(res)

#     # continue
#     key = cv2.waitKey(1)
#     if key == ord('r'):
#         task = "recog"
#     if key == ord('p'):
#         task = "pose"
#     if key == ord("q"):
#         cap.release()

# cv2.destroyAllWindows()
#---------------------------------------------------------------