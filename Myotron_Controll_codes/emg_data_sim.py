import numpy as np
import datetime
from time import sleep
import zmq
from tqdm import tqdm
import myotron_control as ctrl
from threading import Thread

bind_addr = "tcp://127.0.0.1:5558"
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
def send_emg(qpos):
    socket.send_string(arr_fromat(qpos))


sim_emg = np.load('sim_data/test_windowed.npy')
# sim_stimulus = np.load('sim_data/s1_raw_emg.npy')
# print('No.Data Points =',len(sim_stimulus))



length = ctrl.win_len
for data in sim_emg:
    soft_pred = ctrl.wrist_classifier(data)
    # sorted_clf = ctrl.soft_to_Sortedclass(soft_pred)
    # print(sorted_clf)
    print(data)
    print(soft_pred,np.argmax(np.array(soft_pred)))
    sleep(0.0005)
    # print(sim_emg[i:i+length].shape)
    # send_emg(sim_emg[i])