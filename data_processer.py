import numpy as np
import sklearn
from keras.models import load_model
from InceptionTime.classifiers.inception import Classifier_INCEPTION

print('Loading Data....')
X_train = np.load('prepared_data/X_train.npy')
X_test = np.load('prepared_data/X_test.npy')
y_train = np.load('prepared_data/y_train.npy')
y_test = np.load('prepared_data/y_test.npy')
print('Data Loaded Successfully')

y_true = []
for d in y_test:
    idx = list(d).index(1)
    y_true.append(idx)

clf = Classifier_INCEPTION('', (X_train.shape[1],X_train.shape[2]),nb_classes=3,
                        verbose=True,batch_size=64,nb_epochs=25,nb_filters=16,
                        depth=10, kernel_size=50)

# clf.model = load_model('best_model.hdf5')
df_metrics = clf.fit(X_train, y_train, X_test, y_test, y_true,plot_test_acc=True)

# from keras.models import load_model
# best_model = load_model('best_model.hdf5')
# best_model.save('models/restprosup_nina_model_{}'.format(1000))