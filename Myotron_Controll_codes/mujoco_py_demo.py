import mujoco_py
import os
import time
from random import choice
from hand_motion import*


########################################################
'''
Mujoco Init Part 
'''
mj_path, _ = mujoco_py.utils.discover_mujoco()
xml_path = os.path.join(mj_path, 'model', 'humanoid.xml')
xml_path = 'F:\The Stuffs\Awear\Mujoco_work\mjhaptix150\model\MPL\MPL_Power.xml'
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
    print(pos)
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
    current_qpos = rest_qpos()
    while True: 
        full_update_motion(class_4)


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