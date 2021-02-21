import numpy as np
import zmq
import datetime
import myotron_controll as ctrl 
import random
import pytrigno
from time import sleep
from hand_motion import wrist_moves
from hand_motion import grasp_moves
##################### ZMQ Send Qpos ##############################
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5555") # Controller to Mujoco

def arr_fromat(arr):
    string = str(arr[0]);
    arr2 = arr[1:]
    for e in arr2:
        string = string+' '+str(e)
    return string
def send_qpos(qpos):
    socket.send_string(arr_fromat(qpos))
#####################################################################



################# ZMQ Receive Current Qpos ###########################
Pcontext = zmq.Context()
Psocket  = Pcontext.socket( zmq.SUB )

Psocket.connect( "tcp://127.0.0.1:5556" ) # Mujoco to Controller

Psocket.setsockopt( zmq.LINGER,     0 )
Psocket.setsockopt_string( zmq.SUBSCRIBE,"")
Psocket.setsockopt( zmq.CONFLATE,   1 )

def str_to_array(str_arr):
     list_str = str_arr.split()
     arr = np.zeros(len(list_str))
     for i in range(len(list_str)):
          arr[i] = float(list_str[i]) 
     return arr
def recv_current_qpos():
    recv_bytes = Psocket.recv()
    current_qpos = str_to_array(recv_bytes.decode("utf-8"))
    print('Current Qpos =',current_qpos)
    return current_qpos

######################################################################


###################### EMG Trigno Functions ##########################
def multichannel_emg(channel_range, sample):
    channel_range = channel_range-1
    host = 'localhost'
    dev = pytrigno.TrignoEMG(channel_range=(0, channel_range), samples_per_read=sample,host=host)
    dev.start()

    while(True):
        data = dev.read()
        sensor_val = data
        if(sample>1):
            sensor_val = list()
            for val in data:
                sensor_val.append(np.mean(val))
        print(sensor_val)
    dev.stop()
#####################################################################



if __name__=="__main__":
    current_qpos = recv_current_qpos()
    while True:
        # Get Current Qpos from Mujoco
        clf_array = ctrl.wrist_classifier(data)
        sorted_class = ctrl.soft_to_Sortedclass(clf_array)
        motion_class = ctrl.agregation_node(sorted_class)
        qpos = wrist_moves[motion_class](current_qpos)
        socket.send_string(arr_fromat(qpos))
        current_qpos = recv_current_qpos()
        # n = random.uniform(-3.14,3.14)
        # qpos = n*np.ones(13)
        print(qpos)
        