import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from queue import Queue 
fifo = Queue()
win_len = 150
n_channels = 8
model_wrist = load_model('models/wrist_150_90_40s_8semg.hdf5')
print('Loading Wrist Model...')
print(model_wrist.summary())

model_grasp = load_model('E:/Fazil/myotron_control/Myotron_Controll_codes/models/grasp_150_90_40s_8semg.hdf5')
print('Loading Grasp Model...')
print(model_grasp.summary())

def wrist_classifier(data):
    data = np.array(data) 
    data = np.reshape(data,(1,win_len,n_channels))
    pred = model_wrist.predict(data,batch_size=1)[0]
    print(pred)
    return pred

def grasp_classifier(data):
    data = np.array(data) 
    data = np.reshape(data,(1,win_len,n_channels))
    pred = model_grasp.predict(data,batch_size=1)[0]
    print(pred)
    return pred

def soft_to_Sortedclass(clf_array):
    clf_array = list(clf_array)
    n = len(clf_array)
    sorted_class = sorted(range(len(clf_array)),key=clf_array.__getitem__)
    return sorted_class

def fifo_node(clf_array,size):
    clf_array = np.array(clf_array)
    return clf_array[0:size]

def agregation_node(fifo_array): 
    List = list(fifo_array)
    counter = 0
    num = List[0] 
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
    return num 

