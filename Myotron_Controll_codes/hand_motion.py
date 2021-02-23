import numpy as np

"""
0 - Rest
1 - Suplination - CW (rot axis Mid finger)
2 - Pronation - CCW (rot axis Mid finger)
3 - Suplination - CW (rot axis lit finger)
4 - Pronation - CCW (rot axis lit finger)
5 - Flexion - Bend Towards
6 - Extension - Bend Backward
7 - Radial - Left - CCW
8 - Radial - Righ - CW
9 - Extension with closed hand
"""

step_size = 0.01
rest_qpos = np.zeros(13)

def go_towards_nb(current,limit,step_size=0.01):
    if(current<limit):
        return current+step_size
    elif(current>limit):
        return current-step_size
    else:
        return current 

def class_0(current_qpos,step_size=0.01):
    qpos = current_qpos
    j = 0
    qpos[0] = go_towards_nb(qpos[3],j)
    qpos[1] = go_towards_nb(qpos[3],j)
    qpos[2] = go_towards_nb(qpos[3],j)
    qpos[3] = go_towards_nb(qpos[3],j)
    qpos[4] = go_towards_nb(qpos[4],j)
    qpos[5] = go_towards_nb(qpos[5],j)
    qpos[6] = go_towards_nb(qpos[6],j)
    qpos[7] = go_towards_nb(qpos[7],j)
    qpos[8] = go_towards_nb(qpos[8],j)
    qpos[9] = go_towards_nb(qpos[9],j)
    qpos[10] = go_towards_nb(qpos[10],j)
    qpos[11] = go_towards_nb(qpos[11],j)
    qpos[12] = go_towards_nb(qpos[12],j)
    return qpos

def class_1(current_qpos,step_size=0.01):
    qpos = current_qpos
    roll = current_qpos[0] 
    nroll = roll+step_size
    if(nroll<=1.57 and nroll>=-1.57):
        qpos[0] = nroll
    if(abs(nroll-1.57)<=0.01):
        qpos[0]=1.57 
    return qpos

def class_2(current_qpos,step_size=0.01):
    qpos = current_qpos
    roll = current_qpos[0] 
    nroll = roll-step_size
    if(nroll<=1.57 and nroll>=-1.57):
        qpos[0] = nroll
    if(abs(nroll+1.57)<=0.01):
        qpos[0]=-1.57    
    return qpos

def class_3(current_qpos,step_size=0.01):
    qpos = current_qpos
    roll = current_qpos[0]
    yaw = 0.5
    nroll = roll+step_size
    if(nroll<=1.57 and nroll>=-1.57):
        qpos[0] = nroll
    if(abs(nroll-1.57)<=0.01):
        qpos[0]=1.57 
    qpos[1] = yaw
    return qpos

def class_4(current_qpos,step_size=0.01):
    qpos = current_qpos
    roll = current_qpos[0]
    yaw = 0.5
    nroll = roll-step_size
    if(nroll<=1.57 and nroll>=-1.57):
        qpos[0] = nroll
    if(abs(nroll+1.57)<=0.01):
        qpos[0]=-1.57   
    qpos[1] = yaw 
    return qpos

def class_5(current_qpos,step_size=0.01):
    qpos = current_qpos
    pitch = current_qpos[2] 
    npitch = pitch+step_size
    if(npitch<=1 and npitch>=-1):
        qpos[2] = npitch
    if(abs(npitch-1)<=0.01):
        qpos[2]=1
    return qpos

def class_6(current_qpos,step_size=0.01):
    qpos = current_qpos
    pitch = current_qpos[2] 
    npitch = pitch-step_size
    if(npitch<=1 and npitch>=-1):
        qpos[2] = npitch
    if(abs(npitch+1)<=0.01):
        qpos[2]=-1
    return qpos

def class_7(current_qpos,step_size=0.01):
    qpos = current_qpos
    yaw = current_qpos[1] 
    nyaw = yaw-step_size
    if(nyaw<=0.79 and nyaw>=-0.26):
        qpos[1] = nyaw
    if(abs(nyaw+0.26)<=0.01):
        qpos[1]=-0.26
    return qpos

def class_8(current_qpos,step_size=0.01):
    qpos = current_qpos
    yaw = current_qpos[1] 
    nyaw = yaw+step_size
    if(nyaw<=0.79 and nyaw>=-0.26):
        qpos[1] = nyaw
    if(abs(nyaw-0.79)<=0.01):
        qpos[1]=0.79
    return qpos

def class_9(current_qpos,step_size=0.01):
    qpos = current_qpos
    pitch = current_qpos[2] 
    npitch = pitch-step_size
    if(npitch<=1 and npitch>=-1):
        qpos[2] = npitch
    if(abs(npitch+1)<=0.01):
        qpos[2]=-1
    qpos[3] = 0
    qpos[4] = go_towards_nb(qpos[4],1)
    qpos[5] = go_towards_nb(qpos[5],1)
    qpos[6] = 0

    qpos[7] = go_towards_nb(qpos[7],0.34)
    qpos[8] = go_towards_nb(qpos[8],1.6)
    qpos[9] = go_towards_nb(qpos[9],1.6)
    qpos[10] = go_towards_nb(qpos[10],1.6)
    qpos[11] = go_towards_nb(qpos[11],0.34)
    qpos[12] = go_towards_nb(qpos[12],1.6)
    return qpos

def grasp_0(current_qpos,step_size=0.01):
    qpos = current_qpos
    qpos[3] = go_towards_nb(qpos[3],2)
    qpos[4] = go_towards_nb(qpos[4],0.5)
    qpos[5] = go_towards_nb(qpos[5],0.5)
    qpos[6] = go_towards_nb(qpos[6],1)
    j = 1.1
    qpos[7] = go_towards_nb(qpos[7],0.34)
    qpos[8] = go_towards_nb(qpos[8],j)
    qpos[9] = go_towards_nb(qpos[9],j)
    qpos[10] = go_towards_nb(qpos[10],j)
    qpos[11] = go_towards_nb(qpos[11],0.34)
    qpos[12] = go_towards_nb(qpos[12],j)

    return qpos


wrist_moves = [class_0, class_1, class_2, class_3, class_4, class_5, class_6, class_7, class_8, class_9, grasp_0]

grasp_moves = [grasp_0]
"""
pos
Pose of Hand
x = 0
y = 1
z = 2
rot_x = 5 (Pitch) 
rot_y = 4 (Roll)
rot_z = 3 (Yaw)
"""

"""
ctrl
Hand Actuator Controls
wrist
0 - Roll "-1.57 1.57"
1 - Yaw "-0.26 0.79"
2 - Pitc "-1 1"

Thumb
3 - A_thumb_ABD  "0 2.1"
4 - A_thumb_MCP "0 1.0"
5 - A_thumb_PIP "0 1.0"
6 - A_thumb_DIP "-0.82 1.3"

Fingers
7 - A_index_ABD "0 0.34"
8 - A_index_MCP "0 1.6"
9 - A_middle_MCP "0 1.6"
10 - A_ring_MCP "0 1.6"
11 - A_pinky_ABD "0 0.34"
12 - A_pinky_MCP "0 1.6"
"""