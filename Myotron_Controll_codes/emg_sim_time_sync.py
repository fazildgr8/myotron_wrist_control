import numpy as np
import pandas as pd
from time import sleep
from datetime import datetime
from threading import Thread
from keras.models import load_model

global prosup_clf, emg_window, curr_ts, curr_clf


win_len = 250
n_channels = 8
prosup_clf = 0
curr_ts = 0.0
emg_window = np.zeros((win_len,n_channels))

prosup_file = 'models/restprosup_model_250'
prosup_model = load_model(prosup_file)

emg_labels = ['emg1','emg2','emg3','emg4','emg5','emg6','emg7','emg8']

emg_df = pd.read_excel('F:/The Stuffs/Awear/Final_Project/myotron_control/Myotron_Controll_codes/sim_data/prosup_norm_200s_labeled.xlsx')
# emg_df.columns = ['t[s]']+emg_labels
print(emg_df.columns)

emg_data = np.array(emg_df[emg_labels])
# emg_ts = np.array(emg_df['t[s]'])
emg_True_labels = np.array(emg_df['labels'])

def classify(data,model):
    data = np.reshape(data,(1,win_len,n_channels))
    soft = model.predict(data,batch_size=1)
    clf = np.argmax(np.array(soft))
    return clf
 
def read_emg_window():
    global emg_window, curr_ts, curr_clf, emg_window
    i = 0
    while True:
        emg_window = emg_data[i:i+win_len]
        curr_ts = i
        curr_clf = emg_True_labels[i]
        # sleep(1/2000)
        i = i+1
def classify_loop():
    global prosup_clf, emg_window
    while True:
        prosup_clf = classify(emg_window,prosup_model)
        # print(curr_ts,' ',prosup_clf,' ',curr_clf)

if __name__ == '__main__':
    thread_emg_read = Thread(target=read_emg_window)
    thread_classify = Thread(target=classify_loop)
    thread_emg_read.start()
    thread_classify.start()

    start_time = datetime.now()
    while True:
        now_time = datetime.now()
        elp = now_time - start_time
        elapsed = elp.total_seconds()
        print(curr_ts,' ',prosup_clf,' ',curr_clf)
        if elapsed>10000:
            break
