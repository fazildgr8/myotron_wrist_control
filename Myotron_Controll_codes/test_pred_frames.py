from keras.models import load_model
import numpy as np


rest_model = load_model('models/')
prosup_model = load_model('models/prosup_model_250_97') 
flexex_model = load_model('models/flexex_model_250_96')
radial_model = load_model('models/Radial_model_250_97')
grasp_model = load_model('models/grasp_model_250_92')

sim_emg = np.load('sim_data/test_window.py')


rest_pred = rest_model.predict(sim_emg)
flexex_pred = flexex_model.predict(sim_emg)
radial_pred = radial_model.predict(sim_emg)
prosup_pred = prosup_model.predict(sim_emg)
grasp_pred = grasp_model.predict(sim_emg)

    
np.save('sim_data/test_pred_prosup',np.array(pred_frame))
np.save('sim_data/test_pred_prosup',np.array(pred_frame))
np.save('sim_data/test_pred_prosup',np.array(pred_frame))
np.save('sim_data/test_pred_prosup',np.array(pred_frame))