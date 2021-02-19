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
sim = mujoco_py.MjSim(model)
viewer = mujoco_py.MjViewer(sim)

print('Q Pose',sim.data.qpos)
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

def update_qpos(sim,qpos):
     sim.data.ctrl[0] = qpos[0]  
     sim.data.ctrl[1] = qpos[1]
     sim.data.ctrl[2] = qpos[2]
     sim.data.ctrl[3] = qpos[3]
     sim.data.ctrl[4] = qpos[4]
     sim.data.ctrl[5] = qpos[5]
     sim.data.ctrl[6] = qpos[6]
     sim.data.ctrl[7] = qpos[7]
     sim.data.ctrl[8] = qpos[8]
     sim.data.ctrl[9] = qpos[9]
     sim.data.ctrl[10] = qpos[10]
     sim.data.ctrl[11] = qpos[11]
     sim.data.ctrl[12] = qpos[12]

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

##########################################################
if __name__ == "__main__":
    while True:
        current_qpos = get_current_qpos(sim)
        sim.step()
        viewer.render()