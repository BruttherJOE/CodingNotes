import filterpy
from filterpy.kalman import UnscentedKalmanFilter 
from filterpy.kalman import MerweScaledSigmaPoints
from filterpy.common import Q_discrete_white_noise
import numpy as np

import math
import matplotlib.pyplot as plt
import scipy.linalg

# state : [x,y,vx,vy]


def fx(x, dt):
    # state transition function - predict next state based
    # on constant velocity model x = vt + x_0

    # x' = x + vx*dt
    # y' = y + vy*dt
    # vx' = vx
    # vy' = vy

    F = np.array([[1, 0, dt, 0],
                  [0, 1, 0, dt],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])
    return np.dot(F, x)

def hx(x):
   # measurement function - convert state into a measurement
   # where measurements are [x_pos, y_pos]

   # x = [pos_x, pos_y, vel_x, vel_y]
   # x[0] = pos_x
   # x[1] = pos_y
   # x[2] = vel_x
   # x[3] = vel_y

   return np.array([x[0], x[1]])  # Observation x,y position covariance

dt = 0.1
# create sigma points to use in the filter. This is standard for Gaussian processes
points = MerweScaledSigmaPoints(4, alpha=.001, beta=2., kappa=0)

kf = UnscentedKalmanFilter(dim_x=4, dim_z=2, dt=dt, fx=fx, hx=hx, points=points)
kf.x = np.array([-1., 1., -1., 1]) # initial state
kf.P *= 0.2 # initial uncertainty
z_std = 0.1
kf.R = np.diag([z_std**2, z_std**2]) # 1 standard
kf.Q = Q_discrete_white_noise(dim=2, dt=dt, var=0.01**2, block_size=2)

gt = [[i, i] for ia in range(50)] # ground truth
zs = [[i+np.random.randn()*2.0, i+np.random.randn()*0.2] for i in range(50)] # measurements

for g, z in zip(gt, zs):
    kf.predict()
    kf.update(z)
    print(g, z, kf.x, 'log-likelihood', kf.log_likelihood)

