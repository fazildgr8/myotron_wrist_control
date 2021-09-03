import mujoco_py
import os
import time
from random import choice
from hand_motion import*
import zmq
import threading
from mjremote import mjremote

########################################################
"""Unity Communication"""
global uni_context

uni_context = zmq.Context()
uni_context  = uni_context.socket( zmq.SUB )

uni_context.connect( "tcp://127.0.0.1:5557" )
# Send the Class(int) of the Move to this ZMQ Socket

uni_context.setsockopt( zmq.LINGER,     0 )
uni_context.setsockopt_string( zmq.SUBSCRIBE,"")
uni_context.setsockopt( zmq.CONFLATE,   1 )


########################################################
global Pcontext, Psocket, move_id
move_id = 0
Pcontext = zmq.Context()
Psocket  = Pcontext.socket( zmq.SUB )

Psocket.connect( "tcp://127.0.0.1:5556" )
# Send the Class(int) of the Move to this ZMQ Socket

Psocket.setsockopt( zmq.LINGER,     0 )
Psocket.setsockopt_string( zmq.SUBSCRIBE,"")
Psocket.setsockopt( zmq.CONFLATE,   1 )

def str_to_array(str_arr):
     list_str = str_arr.split()
     arr = np.zeros(len(list_str))
     for i in range(len(list_str)):
          arr[i] = float(list_str[i]) 
     return arr

def recv_qpos():
    global Psocket
    recv_bytes = Psocket.recv()
    qpos = str_to_array(recv_bytes.decode("utf-8"))
    return qpos

def recv_class():
    global Psocket
    recv_bytes = Psocket.recv()
    return int(recv_bytes.decode("utf-8"))

def assign_move():
    global move_id
    while True:
        move_id = recv_class()

########################################################
'''
Mujoco Init Part 
'''
mjr = mjremote()
mjr.connect(address='127.0.0.1',port=1050)
mj_path, _ = mujoco_py.utils.discover_mujoco()
xml_path = os.path.join(mj_path, 'model', 'humanoid.xml')
xml_path = 'F:/The Stuffs/Awear/Mujoco_work/mjhaptix150/model/MPL/MPL_Basic.xml'
model = mujoco_py.load_model_from_path(xml_path)
global sim, viewer, current_qpos
sim = mujoco_py.MjSim(model)
viewer = mujoco_py.MjViewer(sim)
current_qpos = np.zeros(13)
print('Joint Poses',sim.data.ctrl)
print('No. DOF',len(sim.data.ctrl))

def get_current_qpos(sim):
    current_qpos = np.zeros(13)
    current_qpos[0] = sim.data.ctrl[0]
    current_qpos[1] = sim.data.ctrl[1]
    current_qpos[2] = sim.data.ctrl[2]
    current_qpos[3] = sim.data.ctrl[3]
    current_qpos[4] = sim.data.ctrl[4]
    current_qpos[5] = sim.data.ctrl[5]
    current_qpos[6] = sim.data.ctrl[6]
    current_qpos[7] = sim.data.ctrl[7]
    current_qpos[8] = sim.data.ctrl[8]
    current_qpos[9] = sim.data.ctrl[9]
    current_qpos[10] = sim.data.ctrl[10]
    current_qpos[11] = sim.data.ctrl[11]
    current_qpos[12] = sim.data.ctrl[12]
    return current_qpos

def update_qpos(pos):
    global sim
    pos = np.array(pos)
    # print(pos)
    sim.data.ctrl[0] = pos[0]  
    sim.data.ctrl[1] = pos[1]
    sim.data.ctrl[2] = pos[2]
    sim.data.ctrl[3] = pos[3]
    sim.data.ctrl[4] = pos[4]
    sim.data.ctrl[5] = pos[5]
    sim.data.ctrl[6] = pos[6]
    sim.data.ctrl[7] = pos[7]
    sim.data.ctrl[8] = pos[8]
    sim.data.ctrl[9] = pos[9]
    sim.data.ctrl[10] = pos[10]
    sim.data.ctrl[11] = pos[11]
    sim.data.ctrl[12] = pos[12]

def grasp(sim,i):
    sim.data.ctrl[7] = i
    sim.data.ctrl[8] = i
    sim.data.ctrl[9] = i
    sim.data.ctrl[10] = i
    sim.data.ctrl[11] = i
    sim.data.ctrl[12] = i
    sim.data.ctrl[3] = i
    sim.data.ctrl[4] = i

def ungrasp(sim,i):
    sim.data.ctrl[7] = sim.data.ctrl[7] - i
    sim.data.ctrl[8] = sim.data.ctrl[8] - i
    sim.data.ctrl[9] = sim.data.ctrl[9] - i
    sim.data.ctrl[10] = sim.data.ctrl[10] - i
    sim.data.ctrl[11] = sim.data.ctrl[11] - i
    sim.data.ctrl[12] = sim.data.ctrl[12] - i
    sim.data.ctrl[3] = sim.data.ctrl[3] - i

def handPose_update(sim,trans,rot):
    sim.data.qpos[0] = trans[0]
    sim.data.qpos[1] = trans[1]
    sim.data.qpos[2] = trans[2]
    sim.data.qpos[3] = rot[0]
    sim.data.qpos[4] = rot[1]
    sim.data.qpos[5] = rot[2]

def rest_qpos():
    return np.zeros(13)

def sim_step_stack():
    global sim, current_qpos, viewer
    sim.step()
    current_qpos = get_current_qpos(sim)
    viewer.render()

def full_update_motion(clf_class):
    global current_qpos
    update_qpos(clf_class(current_qpos))
    sim_step_stack()
##########################################################

if __name__ == "__main__":
    thread = threading.Thread(target=assign_move)
    thread.start()
    current_qpos = rest_qpos()
    full_update_motion(class_0)
    while True:
        mjr.setqpos(sim.data.qpos)
        full_update_motion(wrist_moves[move_id])

        # full_update_motion(wrist_moves[1])


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