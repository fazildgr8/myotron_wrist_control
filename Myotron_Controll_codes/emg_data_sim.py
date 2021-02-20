import numpy as np
import datetime
import zmq

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
def send_emg(qpos):
    socket.send_string(arr_fromat(qpos))


sim_emg = np.load('sim_data/s1_raw_emg.npy')
sim_stimulus = np.load('sim_data/s1_raw_emg.npy')

print(sim_emg.shape,sim_stimulus.shape)

for i in range(sim_emg.shape[0]):
    print(sim_emg[i])
    send_emg(sim_emg[i])