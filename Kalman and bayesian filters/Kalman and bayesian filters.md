# Kalman and bayesian filters



a knowledge dump

compiled by BruttherJOE





Kalman filters :

- use past information to predict information about the future
- its first use was on Apollo missions to the moon
- there are kalman filters in aircraft, submarines, cruise missiles, and even wall st uses it to track the marker. Kalman is manifest everywhere.



### Overview

[source : https://en.wikipedia.org/wiki/Kalman_filter]



Noisy sensor data, approximations in the equations that describe the system evolution, and external factors that are not accounted for all place limits on how well it is possible to determine the system's state. The Kalman filter deals effectively with the uncertainty due to noisy sensor data and, to some extent, with random external factors. 

The Kalman filter produces an estimate of the state of the system as an average of the system's predicted state and of the new measurement using a weighted average. The purpose of the weights is that values with better (i.e., smaller) estimated uncertainty are "trusted" more. The weights are calculated from the covariance, a measure of the estimated uncertainty of the prediction of the system's state. The result of the weighted average is a new state estimate that lies between the predicted and measured state, and has a better estimated uncertainty than either alone. This process is repeated at every time step, with the new estimate and its covariance informing the prediction used in the following iteration. 

This means that Kalman filter works recursively and requires only the last "best guess", rather than the entire history, of a system's state to calculate a new state.

The relative certainty of the measurements and current state estimate is an important consideration, and it is common to discuss the response of the filter in terms of the Kalman filter's gain. The Kalman gain is the relative weight given to the measurements and current state estimate, and can be "tuned" to achieve a particular performance. **With a high gain, the filter places more weight on the most recent measurements, and thus follows them more responsively. With a low gain, the filter follows the model predictions more closely.** 

At the extremes, a high gain close to one will result in a more jumpy estimated trajectory, while a low gain close to zero will smooth out noise but decrease the responsiveness.

When performing the actual calculations for the filter, the state estimate and covariances are coded into matrices to handle the multiple dimensions involved in a single set of calculations. This allows for a representation of linear relationships between different state variables (such as position, velocity, and acceleration) in any of the transition models or covariances.





### Effects

As one can clearly see, it reduces the noise on instruments that measure things. Like rulers, weights, lidar, sonar, gps.



![Kalman](C:\Users\uic77433\Desktop\work stuff\CodingNotes\Kalman and bayesian filters\assets\Kalman.png)



Legend : 

- Black : Truth
- Red: Observations
- Green : filtered process



I don't know why there are 2 zeroes on this x axis. If someone knows why, please tell me why.





### Details

The Kalman filter can be written as a single equation, however it is most often conceptualized as two distinct phases: "Predict" and "Update". 

The predict phase uses the state estimate from the previous timestep to produce an estimate of the state at the current timestep. This predicted state estimate is also known as the *a priori* state estimate because, although it is an estimate of the state at the current timestep, it does not include observation information from the current timestep. 

In the update phase, the current *a priori* prediction is combined with current observation information to refine the state estimate. This improved estimate is termed the *a posteriori* state estimate.





### Dead Reckoning

**Dead Reckoning** is the process of calculating one's current position by using a previously determined position, or fix, by using estimations of speed and course over elapsed time.





### The basic equation :


$$
\dot{\mathbf{x}} = \mathbf{Fx} + \mathbf{Bu} + w
$$



Where :

- F, the state-transition model that is applied to the previous state X_k-1
- H, the observation model;
- Q, the covariance of the process noise;
- R, the covariance of the observation noise;
- and sometimes B, the control-input model, for each time-step k. This is applied to the control vector u.
- w is the process noise with covariance Q



Also, whenever you see an x with a caret or a hat over it, this means that it is the estimated x.



the predict function is f, while update function is h.



### Covariance

[Source : Methyldragon]

Covariance is the tendency for two variables to **vary together**, which is a way of being correlated!



The Kalman filter assumes that both variables (position and velocity, in our case) are random and *Gaussian distributed.* Each variable has a **mean** value μ, which is the center of the random distribution (and its most likely state), and a **variance** σ2, which is the uncertainty:



UKFs are slower but more accurate for non-linear transformations



high value = high variance 
if you are certain of the accuracy of your instrument, then set a low variance







![1_3](C:\Users\uic77433\Desktop\work stuff\CodingNotes\Kalman and bayesian filters\assets\1_3.png)

​															(Image Source: University of Wisconsin)



The covariance matrix is symmetrical. This means the covariance of xy and yx is the same.



### State transition matrix

answer this first, then all will fall in place

F_k aka the transition matrix is usually a constant. F is a function that relates x_k and x_k-1



### KALMAN GAIN




$$
K_{n}= \frac{Uncertainty \quad in \quad Estimate}{Uncertainty \quad in \quad Estimate \quad + \quad Uncertainty \quad in \quad Measurement}= \frac{p_{n,n-1}}{p_{n,n-1}+r_{n}}
$$


where K_n is the Kalman gain



as such, kalman gain is limited to be between 0 and 1.

at KG = 1, measurements are accurate and estimates are unstable.

at KG = 0, the estimates are stable and the measurements are inaccurate.



x = x_0 + v_0Δt +0.5aΔt^2 = x_0 + v_0Δt + 0.5aΔt^2

Where:

x is target position

x_0 is target initial position

v_0 initial velo

a accel

Δt time interval (change in time)



in 3 dimensions:
$$
\left\{\begin{matrix}
                                        x= x_{0} + v_{x0} \Delta t+ \frac{1}{2}a_{x} \Delta t^{2}\\ 
                                        y= y_{0} + v_{y0} \Delta t+ \frac{1}{2}a_{y} \Delta t^{2}\\
                                        z= z_{0} + v_{z0} \Delta t+ \frac{1}{2}a_{z} \Delta t^{2}
                                        \end{matrix}\right.
$$


measurements will include random errors, or uncertainty. This occurs due to uncertainty in instrument precision for example lidar callibration is shit. This error is called Measurement Noise.



target is affected by drag, friction, wind, etc. This error is called Process Noise.



due to these noises, there is a need for prediction algorithm and hence a need for kalman filter.



Consider fat man on weighing scale. the true value of his weight is unknown even when u measure it, hence its a <u>hidden variable.</u>

But we can estimate his weight by averaging his weight, through measuring 5 times.



The outcome of the estimate is the expected value of the weight.

The mean is usually denoted by a Greek letter **μ**.

The expected value is usually denoted by letter **E**.





### Variance and std dev

The **Variance** is a measure of spreading of the data set from its mean.

The **Standard Deviation** is the square root of the variance.



formula for variance (sigma sqaured) :


$$
\sigma ^{2}= \frac{1}{N-1} \sum _{n=1}^{N} \left( x_{n}-  \mu  \right) ^{2}
$$


For all values on the bell curve :

68.26% of the values lie within one standard deviation of the mean.
95.44% of the values lie within two standard deviations of the mean.
99.74% of the values lie within three standard deviations of the mean.



Visualising what this means :

![statistical_view](C:\Users\uic77433\Desktop\work stuff\CodingNotes\Kalman and bayesian filters\assets\statistical_view.png)



The measurement is a **random variable**, described by the **Probability Density Function (PDF)**.

The measurements mean is the **Expected Value** of the random variable.

The offset between the measurements mean and the true value is the **measurements accuracy** also known as **bias** or **systematic measurement error**.

The dispersion of the distribution is the measurement **precision**, also known as the **measurement noise** or **random measurement error** or **measurement uncertainty**.







#### Effect of Alpha, Beta, and Kappa Parameters

[source : https://www.mathworks.com/help/control/ug/extended-and-unscented-kalman-filter-algorithms-for-online-state-estimation.html#bvgiw03]



To compute the state and its statistical properties at the next time step, the unscented Kalman filter algorithm generates a set of state values distributed around the mean state value. The algorithm uses each sigma points as an input to the state transition and measurement functions to get a new set of transformed state points. The mean and covariance of the transformed points is then used to obtain state estimates and state estimation error covariance.



The spread of the sigma points around the mean state value is controlled by two parameters *α* and *κ*. A third parameter, *β*, impacts the weights of the transformed points during state and measurement covariance calculations.

- *α* — Determines the spread of the sigma points around the mean state value. It is usually a small positive value. The spread of sigma points is proportional to *α*. Smaller values correspond to sigma points closer to the mean state.
- *κ* — A second scaling parameter that is usually set to 0. Smaller values correspond to sigma points closer to the mean state. The spread is proportional to the square-root of *κ*.
- *β* — Incorporates prior knowledge of the distribution of the state. For Gaussian distributions, *β* = 2 is optimal.

You specify these parameters in the `Alpha`, `Kappa`, and `Beta` properties of the unscented Kalman filter. If you know the distribution of state and state covariance, you can adjust these parameters to capture the transformation of higher-order moments of the distribution. The algorithm can track only a single peak in the probability distribution of the state. If there are multiple peaks in the state distribution of your system, you can adjust these parameters so that the sigma points stay around a single peak. For example, choose a small `Alpha` to generate sigma points close to the mean state value.







Measuring something multiple times

usually like ultrasonic sensor, weighing scale...

we use the aby filter


$$
\hat{x}_{N,N}= \frac{1}{N} \left( z_{1}+ z_{2}+ \ldots + z_{N-1}+ z_{N} \right) = \frac{1}{N} \sum _{n=1}^{N} \left( z_{n} \right)
$$
where

x is true value

z_n is measurement value at time n

x_hat N,N is estimate of x at time n (estimate made after taking measurement Zn-1)

x_hat_n+1,n is the estimate of future state (n+1) of x and the estimate is amde at time n right after measurement zn. In other words, this is a predicted state.











```
def fx(x, dt):
    # state transition function - predict next state based
    # on constant velocity model x = vt + x_0
    F = np.array([[1, dt, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, dt],
                  [0, 0, 0, 1]], dtype=float)
    return np.dot(F, x)

def hx(x):
   # measurement function - convert state into a measurement
   # where measurements are [x_pos, y_pos]
   return np.array([x[0], x[2]])

dt = 0.1
# create sigma points to use in the filter. This is standard for Gaussian processes
points = MerweScaledSigmaPoints(4, alpha=.1, beta=2., kappa=-1)

kf = UnscentedKalmanFilter(dim_x=4, dim_z=2, dt=dt, fx=fx, hx=hx, points=points)
kf.x = np.array([-1., 1., -1., 1]) # initial state
kf.P *= 0.2 # initial uncertainty
z_std = 0.1
kf.R = np.diag([z_std**2, z_std**2]) # 1 standard
kf.Q = Q_discrete_white_noise(dim=2, dt=dt, var=0.01**2, block_size=2)

zs = [[i+randn()*z_std, i+randn()*z_std] for i in range(50)] # measurements
for z in zs:
    kf.predict()
    kf.update(z)
    print(kf.x, 'log-likelihood', kf.log_likelihood)
```









### Filterpy

```python
from filterpy.kalman import KalmanFilter 
f = KalmanFilter (dim_x=4, dim_z=2)

f.x = np.array([2., 0.]) #position, velocity
f.F = np.array([[1.,1.],[0.,1.]]) #define state transition matrix

f.H = np.array([[1.,0.]]) #define measurement fn
 
f.P = np.array([[1000., 0.],[ 0., 1000.] ]) #define covariance matrix

f.R = np.array([[5.]]) # assign measurement noise. since dimension 1x1, can use scalar.
# Note that this must be a 2 dimensional array, as must all the matrices.

from filterpy.common import Q_discrete_white_noise
f.Q = Q_discrete_white_noise(dim=2, dt=0.1, var=0.13) #assign process noise

#while some_condition_is true :
z = get_sensor_reading()
f.predict()
f.update(z)
do_something_with_estimate (f.x) #perform standard predict/update loop

```

```python
# Covariance for UKF simulation
Q = np.diag([
    0.1,  # variance of location on x-axis
    0.1,  # variance of location on y-axis
    np.deg2rad(1.0),  # variance of yaw angle
    1.0  # variance of velocity
]) ** 2  # predict state covariance
R = np.diag([1.0, 1.0]) ** 2  # Observation x,y position covariance

#  Simulation parameter
INPUT_NOISE = np.diag([1.0, np.deg2rad(30.0)]) ** 2
GPS_NOISE = np.diag([0.5, 0.5]) ** 2

DT = 0.1  # time tick [s]
SIM_TIME = 50.0  # simulation time [s]

#  UKF Parameter
ALPHA = 0.001
BETA = 2
KAPPA = 0


# Other Parameters
H = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0]
])

F = np.array([[1.0, 0, 0, 0],
              [0, 1.0, 0, 0],
              [0, 0, 1.0, 0],
              [0, 0, 0, 0]])

B = np.array([[DT * math.cos(x[2]), 0],
              [DT * math.sin(x[2]), 0],
              [0.0, DT],
              [1.0, 0.0]])

```



from atsushisakai : 

```python
import math

import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg

# Covariance for UKF simulation
Q = np.diag([
    0.1,  # variance of location on x-axis
    0.1,  # variance of location on y-axis
    np.deg2rad(1.0),  # variance of yaw angle
    1.0  # variance of velocity
]) ** 2  # predict state covariance
R = np.diag([1.0, 1.0]) ** 2  # Observation x,y position covariance

#  Simulation parameter
INPUT_NOISE = np.diag([1.0, np.deg2rad(30.0)]) ** 2
GPS_NOISE = np.diag([0.5, 0.5]) ** 2

DT = 0.1  # time tick [s]
SIM_TIME = 50.0  # simulation time [s]

#  UKF Parameter
ALPHA = 0.001
BETA = 2
KAPPA = 0

show_animation = True


def calc_input():
    v = 1.0  # [m/s]
    yawRate = 0.1  # [rad/s]
    u = np.array([[v, yawRate]]).T
    return u


def observation(xTrue, xd, u):
    xTrue = motion_model(xTrue, u)

    # add noise to gps x-y
    z = observation_model(xTrue) + GPS_NOISE @ np.random.randn(2, 1)

    # add noise to input
    ud = u + INPUT_NOISE @ np.random.randn(2, 1)

    xd = motion_model(xd, ud)

    return xTrue, z, xd, ud


def motion_model(x, u):
    F = np.array([[1.0, 0, 0, 0],
                  [0, 1.0, 0, 0],
                  [0, 0, 1.0, 0],
                  [0, 0, 0, 0]])

    B = np.array([[DT * math.cos(x[2]), 0],
                  [DT * math.sin(x[2]), 0],
                  [0.0, DT],
                  [1.0, 0.0]])

    x = F @ x + B @ u

    return x


def observation_model(x):
    H = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0]
    ])

    z = H @ x

    return z


def generate_sigma_points(xEst, PEst, gamma):
    sigma = xEst
    Psqrt = scipy.linalg.sqrtm(PEst)
    n = len(xEst[:, 0])
    # Positive direction
    for i in range(n):
        sigma = np.hstack((sigma, xEst + gamma * Psqrt[:, i:i + 1]))

    # Negative direction
    for i in range(n):
        sigma = np.hstack((sigma, xEst - gamma * Psqrt[:, i:i + 1]))

    return sigma


def predict_sigma_motion(sigma, u):
    """
        Sigma Points prediction with motion model
    """
    for i in range(sigma.shape[1]):
        sigma[:, i:i + 1] = motion_model(sigma[:, i:i + 1], u)

    return sigma


def predict_sigma_observation(sigma):
    """
        Sigma Points prediction with observation model
    """
    for i in range(sigma.shape[1]):
        sigma[0:2, i] = observation_model(sigma[:, i])

    sigma = sigma[0:2, :]

    return sigma


def calc_sigma_covariance(x, sigma, wc, Pi):
    nSigma = sigma.shape[1]
    d = sigma - x[0:sigma.shape[0]]
    P = Pi
    for i in range(nSigma):
        P = P + wc[0, i] * d[:, i:i + 1] @ d[:, i:i + 1].T
    return P


def calc_pxz(sigma, x, z_sigma, zb, wc):
    nSigma = sigma.shape[1]
    dx = sigma - x
    dz = z_sigma - zb[0:2]
    P = np.zeros((dx.shape[0], dz.shape[0]))

    for i in range(nSigma):
        P = P + wc[0, i] * dx[:, i:i + 1] @ dz[:, i:i + 1].T

    return P


def ukf_estimation(xEst, PEst, z, u, wm, wc, gamma):
    #  Predict
    sigma = generate_sigma_points(xEst, PEst, gamma)
    sigma = predict_sigma_motion(sigma, u)
    xPred = (wm @ sigma.T).T
    PPred = calc_sigma_covariance(xPred, sigma, wc, Q)

    #  Update
    zPred = observation_model(xPred)
    y = z - zPred
    sigma = generate_sigma_points(xPred, PPred, gamma)
    zb = (wm @ sigma.T).T
    z_sigma = predict_sigma_observation(sigma)
    st = calc_sigma_covariance(zb, z_sigma, wc, R)
    Pxz = calc_pxz(sigma, xPred, z_sigma, zb, wc)
    K = Pxz @ np.linalg.inv(st)
    xEst = xPred + K @ y
    PEst = PPred - K @ st @ K.T

    return xEst, PEst


def plot_covariance_ellipse(xEst, PEst):  # pragma: no cover
    Pxy = PEst[0:2, 0:2]
    eigval, eigvec = np.linalg.eig(Pxy)

    if eigval[0] >= eigval[1]:
        bigind = 0
        smallind = 1
    else:
        bigind = 1
        smallind = 0

    t = np.arange(0, 2 * math.pi + 0.1, 0.1)
    a = math.sqrt(eigval[bigind])
    b = math.sqrt(eigval[smallind])
    x = [a * math.cos(it) for it in t]
    y = [b * math.sin(it) for it in t]
    angle = math.atan2(eigvec[bigind, 1], eigvec[bigind, 0])
    rot = np.array([[math.cos(angle), math.sin(angle)],
                    [-math.sin(angle), math.cos(angle)]])
    fx = rot @ np.array([x, y])
    px = np.array(fx[0, :] + xEst[0, 0]).flatten()
    py = np.array(fx[1, :] + xEst[1, 0]).flatten()
    plt.plot(px, py, "--r")


def setup_ukf(nx):
    lamb = ALPHA ** 2 * (nx + KAPPA) - nx
    # calculate weights
    wm = [lamb / (lamb + nx)]
    wc = [(lamb / (lamb + nx)) + (1 - ALPHA ** 2 + BETA)]
    for i in range(2 * nx):
        wm.append(1.0 / (2 * (nx + lamb)))
        wc.append(1.0 / (2 * (nx + lamb)))
    gamma = math.sqrt(nx + lamb)

    wm = np.array([wm])
    wc = np.array([wc])

    return wm, wc, gamma


def main():
    print(__file__ + " start!!")

    nx = 4  # State Vector [x y yaw v]'
    xEst = np.zeros((nx, 1))
    xTrue = np.zeros((nx, 1))
    PEst = np.eye(nx)
    xDR = np.zeros((nx, 1))  # Dead reckoning

    wm, wc, gamma = setup_ukf(nx)

    # history
    hxEst = xEst
    hxTrue = xTrue
    hxDR = xTrue
    hz = np.zeros((2, 1))

    time = 0.0

    while SIM_TIME >= time:
        time += DT
        u = calc_input()

        xTrue, z, xDR, ud = observation(xTrue, xDR, u)

        xEst, PEst = ukf_estimation(xEst, PEst, z, ud, wm, wc, gamma)

        # store data history
        hxEst = np.hstack((hxEst, xEst))
        hxDR = np.hstack((hxDR, xDR))
        hxTrue = np.hstack((hxTrue, xTrue))
        hz = np.hstack((hz, z))

        if show_animation:
            plt.cla()
            # for stopping simulation with the esc key.
            plt.gcf().canvas.mpl_connect('key_release_event',
                    lambda event: [exit(0) if event.key == 'escape' else None])
            plt.plot(hz[0, :], hz[1, :], ".g")
            plt.plot(np.array(hxTrue[0, :]).flatten(),
                     np.array(hxTrue[1, :]).flatten(), "-b")
            plt.plot(np.array(hxDR[0, :]).flatten(),
                     np.array(hxDR[1, :]).flatten(), "-k")
            plt.plot(np.array(hxEst[0, :]).flatten(),
                     np.array(hxEst[1, :]).flatten(), "-r")
            plot_covariance_ellipse(xEst, PEst)
            plt.axis("equal")
            plt.grid(True)
            plt.pause(0.001)


if __name__ == '__main__':
    main()
```















list of most useful references

1. https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/
2. https://www.kalmanfilter.net/default.aspx
3. https://en.wikipedia.org/wiki/Kalman_filter
4. [https://github.com/methylDragon/ros-sensor-fusion-tutorial/blob/master/01%20-%20ROS%20and%20Sensor%20Fusion%20Tutorial.md](https://github.com/methylDragon/ros-sensor-fusion-tutorial/blob/master/01 - ROS and Sensor Fusion Tutorial.md)



no.2 is really good and I am using it right now to understand a lot of things.

wikipedia is really good too!