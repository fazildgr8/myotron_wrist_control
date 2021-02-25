import numpy as np
import datetime
from time import sleep
import zmq
from tqdm import tqdm
import myotron_control as ctrl
from threading import Thread
win_len = 250
n_channels = 8

global pred_class, end

end = False
pred_class = 8
wrist_moves = ['Suplination - CW (rot axis Mid finger)',
               'Pronation - CCW (rot axis Mid finger)',
               'Suplination - CW (rot axis lit finger)',
               'Pronation - CCW (rot axis lit finger)',
               'Flexion - Bend Towards',' Extension - Bend Backward',
               'Radial - Left - CCW',
               'Radial - Righ - CW',
               'Extension with closed hand']


from tensorflow.keras.models import load_model
model_wrist = load_model('models/wrist_model_250_89')
print('Loading Wrist Model...')
print(model_wrist.summary())

def wrist_classifier(data):
    data = np.array(data) 
    data = np.reshape(data,(1,win_len,n_channels))
    pred = model_wrist.predict(data,batch_size=1)[0]
    return pred

bind_addr = "tcp://127.0.0.1:5556"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(bind_addr)

def send_class():
    global pred_class, end
    while end==False:
        socket.send_string(str(pred_class))
        # print(pred_class)
        sleep(1)


sim_emg = np.load('sim_data/test_windowed.npy')
# sim_stimulus = np.load('sim_data/s1_raw_emg.npy')
# print('No.Data Points =',len(sim_stimulus))

ctrl.win_len = win_len
if __name__ == "__main__":
    length = ctrl.win_len
    thread = Thread(target=send_class)
    ts = 0
    # thread.start()
    for data in sim_emg:
        soft_pred = wrist_classifier(data)
        pred_class = np.argmax(np.array(soft_pred))
        print(wrist_moves[pred_class],' t[s] = ',ts,'/180.0')
        ts = ts+0.0005
        # sleep(0.0005)
    end = True
        # print(sim_emg[i:i+length].shape)