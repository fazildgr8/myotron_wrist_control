# myotron_control
This project proposes and delivers a novel approach to train and test a Convolutional Neural Network (CNN) model for muscle synergy controlled prosthetic hands. The project is focused on providing a solution for precise control and real-time testing of prosthetic hand control used by below-elbow amputees having independent control over the prosthetic fingers. Multiple EMG sensors that are placed on the forearm will be used to control the prosthetic hand using the trained model. CNN allows us to extract features from raw EMG signals without the requirement for manual feature engineering done over raw data in traditional methods. Furthermore, the trained model will be evaluated in real-time within a Virtual Reality environment developed using the Mujoco Physics environment with the HTC Vive VR headset. The developed algorithm will be tested on ten healthy participants and their data will be analyzed to show the performance of the presented controller.

## [Ninapro Dataset](http://ninaweb.hevs.ch/)
Ninapro is a a publicly available multimodal database to foster research on robotic & prosthetic hands controlled with artificial intelligence. Ninapro includes electromyography, kinematic, inertial, eye tracking, visual, clinical and neurocognitive data. Ninapro data are used worldwide by scientific researchers in machine learning, robotics, medical and neurocognitive sciences.
## [InceptionTime Model](https://arxiv.org/abs/1909.04939)
InceptionTime is a 1D Convolution based Deep Neural Network model which is currently quoted as the state of the art TSC model from the published paper InceptionTime: Finding AlexNet for Time Series Classification.

### Dataset Preperation Notebook 
- [Ninapro Dataset Prep Pipeline](https://github.com/fazildgr8/myotron_control/blob/main/Ninapro_prep.ipynb)
### InceptionTime Model Training Notebooks 
- [Wrist Motion Classifier](https://github.com/fazildgr8/myotron_control/blob/main/emg_classification_inception_wrist.ipynb)
- [Grasp Motion Classifier](https://github.com/fazildgr8/myotron_control/blob/main/emg_classification_inception_grasp.ipynb)

## Mujoco Virtual Reality Environment
The Mujoco Virtual Reality Controller is developed with OpenVR SDK and Delsys Trigno SDK for aquiring the EMG signals. The VR environment can be found in self developed seperate repository. **[Mujoco Virtual Reality Development](https://github.com/fazildgr8/mujoco200_awear)

## Current Best Model Accuracies
| Window Length/Overlap | 25% | 50% | 80% |
|:-:|:-:|:-:|:-:|
| 100 |  |  |  |
| 150 |  | 91 |  |
| 400 |  | 88 |  |

