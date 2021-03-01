from tqdm import tqdm
import numpy as np

wrist_moves = ['Suplination - CW (rot axis Mid finger)',
               'Pronation - CCW (rot axis Mid finger)',
               'Suplination - CW (rot axis lit finger)',
               'Pronation - CCW (rot axis lit finger)',
               'Flexion - Bend Towards',' Extension - Bend Backward',
               'Radial - Left - CCW',
               'Radial - Righ - CW',
               'Extension with closed hand']

frame_length = 5422
def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
    return num 

i = 0
pred_array = np.load('test_3m_pred.npy')

print('Len.Total Preds =',len(pred_array))

pred_frame = [] 
for i in tqdm(range(5420)):
    pred = []
    for j in range(30):
        pred.append(np.argmax(np.array(pred_array[i+j])))
    pred_frame.append(most_frequent(pred))
    



np.save('test_pred_frame',np.array(pred_frame))