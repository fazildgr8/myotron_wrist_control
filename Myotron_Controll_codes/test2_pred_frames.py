from keras.models import load_model
import numpy as np



def get_evenly_spaced(data,numElems):
    idx = np.round(np.linspace(0, len(data) - 1, numElems)).astype(int)
    new = []
    for i in idx:
        new.append(data[i])
    return np.array(new)

sim_emg = np.load('sim_data/test2_mixed_windowed_200s.npy')
sim_emg = get_evenly_spaced(sim_emg,2000)

rest_model = load_model('models/rest_model_250_92')
prosup_model = load_model('models/prosup_model_250_97') 
flexex_model = load_model('models/flexex_model_250_96')
radial_model = load_model('models/Radial_model_250_97')
grasp_model = load_model('models/grasp_model_250_92')



rest_pred = rest_model.predict(sim_emg)
flexex_pred = flexex_model.predict(sim_emg)
radial_pred = radial_model.predict(sim_emg)
prosup_pred = prosup_model.predict(sim_emg)
grasp_pred = grasp_model.predict(sim_emg)

    
np.save('sim_data/test_rest_pred',np.array(rest_pred))
np.save('sim_data/test_flexex_pred',np.array(flexex_pred))
np.save('sim_data/test_radial_pred',np.array(radial_pred))
np.save('sim_data/test_prosup_pred',np.array(prosup_pred))
np.save('sim_data/test_grasp_pred',np.array(grasp_pred))