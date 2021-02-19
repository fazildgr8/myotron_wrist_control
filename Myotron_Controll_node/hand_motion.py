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
step_size = 0.01
rest_qpos = np.zeros(13)

def class_0(current_qpos):
    return rest_qpos

def class_1(current_qpos):
    qpos = rest_qpos
    c_roll = current_qpos[0] 
    n_roll = roll+step_size
    if(roll<=1.57 and n_roll>=-1.57):
        qpos[0] = n_roll
    if(abs(roll-1.57)<=0.01):
        qpos[0]=1.57 
    return qpos

def class_2(current_qpos):
    qpos = rest_qpos
    c_roll = current_qpos[0] 
    n_roll = roll-step_size
    if(roll<=1.57 and n_roll>=-1.57):
        qpos[0] = n_roll
    if(abs(roll+1.57)<=0.01):
        qpos[0]=-1.57    
    return qpos

def class_3(current_qpos):
    qpos = rest_qpos
    c_roll = current_qpos[0] 
    n_roll = roll+step_size
    if(roll<=1.57 and n_roll>=-1.57):
        qpos[0] = n_roll
    if(abs(roll-1.57)<=0.01):
        qpos[0]=1.57 
    return qpos

def class_4(current_qpos):
    qpos = rest_qpos
    c_roll = current_qpos[0] 
    n_roll = roll-step_size
    if(roll<=1.57 and n_roll>=-1.57):
        qpos[0] = n_roll
    if(abs(roll+1.57)<=0.01):
        qpos[0]=-1.57    
    return qpos

def class_5(current_qpos):
    qpos = rest_qpos
    c_pitch = current_qpos[2] 
    n_pitch = pitch+step_size
    if(pitch<=1 and n_pitch>=-1):
        qpos[2] = n_pitch
    if(abs(pitch-1)<=0.01):
        qpos[2]=1
    return qpos

def class_6(current_qpos):
    qpos = rest_qpos
    c_pitch = current_qpos[2] 
    n_pitch = pitch-step_size
    if(pitch<=1 and n_pitch>=-1):
        qpos[2] = n_pitch
    if(abs(pitch+1)<=0.01):
        qpos[2]=-1
    return qpos

def class_7(current_qpos):
    qpos = rest_qpos
    c_yaw = current_qpos[0] 
    n_yaw = yaw-step_size
    if(yaw<=-0.26 and n_yaw>=0.79):
        qpos[0] = n_yaw
    if(abs(yaw+0.26)<=0.01):
        qpos[0]=-0.26
    return qpos

def class_8(current_qpos):
    qpos = rest_qpos
    c_yaw = current_qpos[0] 
    n_yaw = yaw+step_size
    if(yaw<=-0.26 and n_yaw>=0.79):
        qpos[0] = n_yaw
    if(abs(yaw-0.79)<=0.01):
        qpos[0]=0.79
    return qpos

def class_9(current_qpos):
    return qpos