# myotron_control
This project proposes and delivers a novel approach to train and test a Convolutional Neural Network (CNN) model for muscle synergy controlled prosthetic hands. The project is focused on providing a solution for precise control and real-time testing of prosthetic hand control used by below-elbow amputees having independent control over the prosthetic fingers. Multiple EMG sensors that are placed on the forearm will be used to control the prosthetic hand using the trained model. CNN allows us to extract features from raw EMG signals without the requirement for manual feature engineering done over raw data in traditional methods. Furthermore, the trained model will be evaluated in real-time within a Virtual Reality environment developed using the Mujoco Physics environment with the HTC Vive VR headset. The developed algorithm will be tested on ten healthy participants and their data will be analyzed to show the performance of the presented controller.

The Directory Tree would look like
├───.ipynb_checkpoints
├───InceptionTime
│   ├───classifiers
│   ├───pngs
│   └───utils
├───Ninapro_DB2
└───prepared_data

