import numpy as np
import zmq
import datetime
import myotron_controll as ctrl 
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5555")
# socket.bind("tcp://localhost:5555")

def arr_fromat(arr):
    string = str(arr[0]);
    arr2 = arr[1:]
    for e in arr2:
        string = string+' '+str(e)
    return string
def send_qpos(qpos):
    socket.send_string(arr_fromat(qpos))


if __name__=="__main__":
    clf_array = ctrl.wrist_classifier(data)
    sorted_class = ctrl.soft_to_Sortedclass(clf_array)
    while True:
        n = random.uniform(-3.14,3.14)
        qpos = n*np.ones(13)
        print(qpos)
        socket.send_string(arr_fromat(qpos))