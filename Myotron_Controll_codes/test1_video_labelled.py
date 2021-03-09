import cv2
import numpy as np
from time import sleep
import pandas as pd

label_file = 'F:/The Stuffs/Awear/Final_Project/myotron_control/data_collection/test_1/video_labels.xlsx'
video_path = 'F:/The Stuffs/Awear/Final_Project/myotron_control/data_collection/test_1/test_3m.mp4'
sim_file = 'F:/The Stuffs/Awear/Final_Project/myotron_control/Myotron_Controll_codes/sim_data/test_windowed.npy'
test_pred_file = 'test_pred_frame.npy'

test_pred_frame = list(np.load(test_pred_file))
for i in range(22):
    test_pred_frame.insert(0,0)
print(len(test_pred_frame))

emg_data = np.load(sim_file)
print('Sim Data = ',emg_data.shape)



labels = pd.read_excel(label_file)['labels']
ts = 180

cap = cv2.VideoCapture(video_path)

property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
length = int(cv2.VideoCapture.get(cap, property_id))
print('Total Frames = ', length )
frame_number = int(ts*30)

label_frames = []
dist = int(length/labels.shape[0])

for x in labels:
    for j in range(30):
        label_frames.append(x)
diff = length - len(label_frames)
for i in range(diff):
    label_frames.insert(0,0)
print(len(label_frames))

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
while True:
    ret, frame = cap.read() # Read the frame
    print('Frame '+str(frame_number)+'/'+str(length)+' '+label_txt[label_frames[frame_number]])

    # font 
    font = cv2.FONT_HERSHEY_SIMPLEX 
    
    # org 
    org = (50, 100) 
    
    # fontScale 
    fontScale = 3
    
    # Blue color in BGR 
    color = (255, 255, 255) 
    
    # Line thickness of 2 px 
    thickness = 5
    
    # Using cv2.putText() method 
    frame = cv2.putText(frame, label_txt[label_frames[frame_number]], org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 

    frame = cv2.putText(frame, wrist_moves[test_pred_frame[frame_number]], (50,200), font,  
                   2, (0,0,255), thickness, cv2.LINE_AA) 

    cv2.imshow('Time['+str(ts)+']',ResizeWithAspectRatio(frame,width=350))
    frame_number = frame_number+1
    if frame_number==length-1:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.waitKey(0)  
cv2.destroyAllWindows() 

