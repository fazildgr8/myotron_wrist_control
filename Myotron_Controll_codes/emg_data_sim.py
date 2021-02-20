import numpy as np
import datetime
import zmq_myotron as pub


sim_emg = np.load('sim_data/s1_raw_emg.npy')
sim_stimulus = np.load('sim_data/s1_raw_emg.npy')

print(sim_emg.shape,sim_stimulus.shape)

for i in range(sim_emg.shape[0]):
    print(sim_emg[i].shape)
    # pub.send_qpos(sim_emg[0])