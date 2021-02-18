import numpy as np
        
def soft_to_Sortedclass(clf_array):
    clf_array = list(clf_array)
    n = len(clf_array)
    sorted_class = sorted(range(len(clf_array)),key=clf_array.__getitem__)
    return sorted_class

def fifo_node(clf_array,size):
    clf_array = np.array(clf_array)
    return clf_array[0:size]

def agregation_node(fifo_array): 
    List = list(fifo_array)
    counter = 0
    num = List[0] 
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
    return num 



# class wrist:
#     def __init__(self,fifo_size):
#         self.clf_soft_array = np.zeros(10)
#         self.fifo_array = np.zeros(fifo_size)

#     def soft_to_Sortedclass(self,clf_array):
#         clf_array = list(clf_array)
#         n = len(clf_array)
#         sorted_class = sorted(range(len(clf_array)),key=clf_array.__getitem__)
#         return sorted_class

#     def fifo_node(self,clf_array,size):
#         clf_array = np.array(clf_array)
#         return clf_array[0:size]

