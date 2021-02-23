import numpy as np
import sklearn
import pandas as pd
import sys
import subprocess
import tensorflow as tf
from InceptionTime.classifiers.inception import Classifier_INCEPTION
from keras.models import load_model

X_train = np.load('prepared_data/X_train_s40.npy')
y_train = np.load('prepared_data/y_train_s40.npy')
X_test = np.load('prepared_data/X_test_s40.npy')
y_test = np.load('prepared_data/y_test_s40.npy')

print('X Train Shape =',X_train.shape)
print('Y Train Shape =',y_train.shape)
print('X Test Shape =',X_test.shape)
print('Y Test Shape =',y_test.shape)

y_true = []
for d in y_test:
    idx = list(d).index(1)
    y_true.append(idx)

clf = Classifier_INCEPTION('', (X_train.shape[1],X_train.shape[2]), nb_classes=10, verbose=True,batch_size=1000,nb_epochs=50, nb_filters=32, depth=6, kernel_size=35)

df_metrics = clf.fit(X_train, y_train, X_test, y_test, y_true,plot_test_acc=True)