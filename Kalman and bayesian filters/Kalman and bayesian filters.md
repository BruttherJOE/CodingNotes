# Kalman and bayesian filters

simple notes and cheat sheet

compiled by BruttherJOE



references

https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/





- use past information to predict information about the future
- its first use was on Apollo missions to the moon
- there are kalman filters in aircraft, submarines, cruise missiles, and even wall st uses it to track the marker. Kalman is manifest everywhere.



The basic equation :  
  
![\dot{\mathbf{x}} = \mathbf{Fx} + \mathbf{Gu} + w](https://render.githubusercontent.com/render/math?math=%5Cdot%7B%5Cmathbf%7Bx%7D%7D%20%3D%20%5Cmathbf%7BFx%7D%20%2B%20%5Cmathbf%7BGu%7D%20%2B%20w)


Where F is the state transition matrix

and R is the measurement noise covariance



Covariance is the tendency for two variables to **vary together**, which is a way of being correlated!



The Kalman filter assumes that both variables (position and velocity, in our case) are random and *Gaussian distributed.* Each variable has a **mean** value μ, which is the center of the random distribution (and its most likely state), and a **variance** σ2, which is the uncertainty:



