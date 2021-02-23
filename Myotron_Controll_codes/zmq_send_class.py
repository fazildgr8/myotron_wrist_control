import zmq
import datetime
import random
import numpy as np

bind_addr = "tcp://127.0.0.1:5556"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(bind_addr)
# socket.bind("tcp://localhost:5555")

def arr_fromat(arr):
    string = str(arr[0]);
    arr2 = arr[1:]
    for e in arr2:
        string = string+' '+str(e)
    return string
def send_qpos(qpos):
    socket.send_string(arr_fromat(qpos))

while True:
    # n = random.uniform(-3.14,3.14)
    # qpos = n*np.ones(13)
    # print(qpos)
    socket.send_string(input('Send Class - '))