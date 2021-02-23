import numpy as np
import pytrigno
from time import sleep
import numpy as np
import myotron_control as ctrl
global emg_data

win_len = 250
n_channels = 8
ctrl.win_len = win_len
ctrl.n_channels = n_channels
emg_data = np.zeros((win_len,n_channels))


def get_Single_emg(channel,sample):
    channel = channel-1
    host = 'localhost'
    dev = pytrigno.TrignoEMG(channel_range=(channel, channel), samples_per_read=sample,host=host)
    dev.start()

    while(True):
        data = dev.read()
        sensor_val = data
        # if(sample>1):
        #     sensor_val = np.mean(data[0])
        print(sensor_val)
    dev.stop()

def get_Single_accel(channel,sample):
    channel = channel-1
    t = channel*3
    host = 'localhost'
    dev = pytrigno.TrignoAccel(channel_range=(t, t+2), samples_per_read=sample,host=host)

    dev.start()
    while(True):
        data = dev.read()
        x = data[0]
        y = data[1]
        z = data[2]
        if(sample>1):
            x = np.mean(data[0])
            y = np.mean(data[1])
            z = np.mean(data[2])
        print('-----------------------')
        print([x,y,z])
    dev.stop()

def get_emg_accel(channel,sample=1):
    channel = channel-1
    t = channel*3
    host = 'localhost'
    dev_emg = pytrigno.TrignoEMG(channel_range=(channel, channel), samples_per_read=sample,host=host)
    dev_accel = pytrigno.TrignoAccel(channel_range=(t, t+2), samples_per_read=sample,host=host)

    dev_emg.start()
    dev_accel.start()
    while(True):
        data_emg = dev_emg.read()
        data_accel = dev_accel.read()
        print('Emg Val -',data_emg[0][0],' ACC -',data_accel)
    dev_emg.stop()
    dev_accel.stop()

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
    return 0
    
def multichannel_emg_window(channel_range=n_channels, sample=win_len):
    global emg_data
    channel_range = channel_range-1
    host = 'localhost'
    dev = pytrigno.TrignoEMG(channel_range=(0, channel_range), samples_per_read=sample,host=host)
    dev.start()

    while(True):
        data = dev.read()
        sensor_val = data
        emg_data = np.transpose(sensor_val)
    dev.stop()


if __name__ == '__main__':
    thread = threading.Thread(target=multichannel_emg_window)
    thread.start()
    while(True):
        print(emg_data)
        ctrl.grasp_classifier(emg_data)
    # get_Single_emg(2,1000)
    # get_Single_accel(1,20)
    # multichannel_emg_window(n_channels,win_len)