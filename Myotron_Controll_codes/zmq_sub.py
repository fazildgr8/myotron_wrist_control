import zmq
import datetime
import numpy as np 

Pcontext = zmq.Context()
Psocket  = Pcontext.socket( zmq.SUB )

Psocket.connect( "tcp://127.0.0.1:5556" )

Psocket.setsockopt( zmq.LINGER,     0 )
Psocket.setsockopt_string( zmq.SUBSCRIBE,"")
Psocket.setsockopt( zmq.CONFLATE,   1 )

def str_to_array(str_arr):
     list_str = str_arr.split()
     arr = np.zeros(len(list_str))
     for i in range(len(list_str)):
          arr[i] = float(list_str[i]) 
     return arr

while True:
     recv_bytes = Psocket.recv()
     print(str_to_array(recv_bytes.decode("utf-8")))