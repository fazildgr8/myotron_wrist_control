import numpy as np
import datetime
from time import sleep
import zmq
from tqdm import tqdm
import myotron_control as ctrl


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


sim_emg = np.load('sim_data/s1_raw_emg.npy')
sim_stimulus = np.load('sim_data/s1_raw_emg.npy')
print('No.Data Points =',len(sim_stimulus))

print(sim_emg.shape,sim_stimulus.shape)

length = 150
for i in tqdm(range(sim_emg.shape[0]-length)):
    data = sim_emg[i:i+length]
    wrist_classifier(data)
    sleep(0.1)
    # print(sim_emg[i:i+length].shape)
    # send_emg(sim_emg[i])