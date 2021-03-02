import zmq
import datetime
from time import sleep
import random
import numpy as np
sim_emg = np.load('sim_data/norm_emg_3m.npy')

length = sim_emg.shape[0]
delay = (1/2154)-(1/(length/4.5))
print('X Delay=',delay)
sleep(5)
print(sim_emg.shape)
bind_addr = "tcp://127.0.0.1:5559"
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
def send_array(qpos):
    socket.send_string(arr_fromat(qpos))

i = 0
# length = 100
current_time = datetime.datetime.now()
while i!=length:
    send_array(sim_emg[i])
    i=i+1
    now = datetime.datetime.now()
    elp = now - current_time
    elps = elp.total_seconds()
    print(i,elps,'s')
    if(elps>=180):
        break
    # sleep(1/100000000000000000000000000)
now_time = datetime.datetime.now()

elapsed = now_time-current_time
print(elapsed.total_seconds(),'s',i)