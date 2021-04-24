from keras.models import load_model
best_model = load_model('best_model.hdf5')
best_model.save('models/restprosup_nina_model_{}'.format(1000))