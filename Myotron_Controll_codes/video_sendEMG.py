import cv2
import numpy as np
from time import sleep
path = 'F:/The Stuffs/Awear/Final_Project/myotron_control/data_collection/test_3m.mp4'

ts = 180

cap = cv2.VideoCapture(path)

property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
length = int(cv2.VideoCapture.get(cap, property_id))
print( length )
frame_number = int(ts*30)

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

frame_number = 0
while True:
    ret, frame = cap.read() # Read the frame
    print('Frame '+str(frame_number)+'/'+str(length))
    cv2.imshow('Time['+str(ts)+']',ResizeWithAspectRatio(frame,width=300))
    frame_number = frame_number+1
    if frame_number==length-1:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.waitKey(0)  
cv2.destroyAllWindows() 

