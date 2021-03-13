import cv2
import numpy as np
from time import sleep
import pandas as pd

video_path = 'F:/The Stuffs/Awear/Final_Project/myotron_control/data_collection/test_2/mixed_test_vid.mp4'
sim_file = 'F:/The Stuffs/Awear/Final_Project/myotron_control/Myotron_Controll_codes/sim_data/test2_mixed_windowed_200s.npy'

rest_pred = np.load('sim_data/test_rest_pred.npy')
prosup_pred = np.load('sim_data/test_prosup_pred.npy')
radial_pred = np.load('sim_data/test_radial_pred.npy')
grasp_pred = np.load('sim_data/test_grasp_pred.npy')
flexex_pred = np.load('sim_data/test_flexex_pred.npy')

pred_len = len(rest_pred)
true_labels = []

# emg_data = np.load(sim_file)
# print('Sim Data = ',emg_data.shape)

ts = 200

cap = cv2.VideoCapture(video_path)

property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
length = int(cv2.VideoCapture.get(cap, property_id))
print('Total Frames = ', length )
frame_number = int(ts*30)



rest_label = ['Rest','Motion']
prosup_label = ['Pronation','Supplination']
flexex_label = ['Flexion','Extension']
radial_label = ['Radial','Ulnar']
grasp_label = ['Rest','Grasp']


def softToBinary(data):
    new = list(np.zeros(11,dtype=int))
    acc = list(np.zeros(11,dtype=int))
    for d in data:
        idx = np.argmax(d)
        for i in range(int(length/pred_len)):
            new.append(idx)
            acc.append(d[idx])
    return new,acc



rest_pred_frame,rest_acc = softToBinary(rest_pred)
prosup_pred_frame,prosup_acc = softToBinary(prosup_pred)
radial_pred_frame,radial_acc = softToBinary(radial_pred)
grasp_pred_frame,grasp_acc = softToBinary(grasp_pred)
flexex_pred_frame,flexex_acc = softToBinary(flexex_pred)

print(len(rest_pred_frame))



def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

label_txt = ['Rest','Suplination','Pronation','Flexion','Extension','Radial','Ulnar','Closed Extended','Grasp']

wrist_moves = ['Suplination - CW (rot axis Mid finger)',
               'Pronation - CCW (rot axis Mid finger)',
               'Suplination - CW (rot axis lit finger)',
               'Pronation - CCW (rot axis lit finger)',
               'Flexion - Bend Towards',' Extension - Bend Backward',
               'Radial - Left - CCW',
               'Radial - Righ - CW',
               'Extension with closed hand']

frame_number = 0
txt = ''
while True:
    ret, frame = cap.read() # Read the frame
    print('Frame '+str(frame_number)+'/'+str(length))

    # if(rest_pred_frame[frame_number]==0):
    #     txt = rest_label[rest_pred_frame[frame_number]]
    # else:
    #     txt = rest_label[rest_pred_frame[frame_number]] + ' ' + prosup_label[prosup_pred_frame[frame_number]] + ' ' + flexex_label[flexex_pred_frame[frame_number]] + ' ' + radial_label[radial_pred_frame[frame_number]]
    # if(grasp_pred_frame[frame_number]==1):
    #     txt = txt + grasp_label[grasp_pred_frame[frame_number]]
    # if(rest_pred_frame[frame_number]==0 and rest_acc[frame_number]>0.95):
    #     txt = rest_label[rest_pred_frame[frame_number]]
    # elif(rest_pred_frame[frame_number]==1 and rest_acc[frame_number]>0.95):
    #     txt = rest_label[rest_pred_frame[frame_number]]
    #     if(prosup_acc[frame_number]>0.95):
    #         txt = txt+' '+ prosup_label[prosup_pred_frame[frame_number]]
    #     if(flexex_acc[frame_number]>0.95):
    #         txt = txt+' '+ flexex_label[flexex_pred_frame[frame_number]]
    #     if(prosup_acc[frame_number]>0.95):
    #         txt = txt+' '+ radial_label[radial_pred_frame[frame_number]]
            
    # if(grasp_pred_frame[frame_number]==1 and grasp_acc[frame_number]>0.999):
    #     txt = txt +' '+grasp_label[grasp_pred_frame[frame_number]]
    # font 
    font = cv2.FONT_HERSHEY_SIMPLEX 
    
    # org 
    org = (50, 100) 
    
    # fontScale 
    fontScale = 3
    
    # Blue color in BGR q
    color = (255, 255, 255) 
    
    # Line thickness of 2 px 
    thickness = 5
    
    # Using cv2.putText() method 
    frame = cv2.putText(frame, txt, org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 

    cv2.imshow('Time['+str(ts)+']',ResizeWithAspectRatio(frame,width=800))
    frame_number = frame_number+1
    if frame_number==length-1:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.waitKey(0)  
cv2.destroyAllWindows() 

