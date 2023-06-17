from deepface import DeepFace
import cv2
import os
from custom_socket import CustomSocket
import socket
import json
import numpy as np
import traceback

def main():
    HOST = socket.gethostname()
    PORT = 10011

    server = CustomSocket(HOST, PORT)
    server.startServer()

    while True:
        conn, addr = server.sock.accept()
        print("Client connected from", addr)

        while True:
            try:
                dataraw = server.recvMsg(conn)
                print("raw",type(dataraw))
                data = dataraw.split(b'bytesplitter')
                print("data",type(data))
                height = int(data[1].decode())
                width = int(data[2].decode())
               
                frame = np.frombuffer(data[0], dtype=np.uint8).reshape(height, width, 3)
                
                #recog
                registered_name = data[3].decode()
                cv2.imwrite("./people/{}.jpg".format(registered_name), frame)

                feedback = bytes("Image and name received",'utf-8')
                msg = server.sendMsg(conn, feedback)

                try:
                    os.remove("./people/representations_arcface.pkl")
                except:
                    print("No files found")
            except Exception as e:
                traceback.print_exc()
                print(e)
                print("Connection Closed")
                break
        
if __name__ == '__main__':
    main()