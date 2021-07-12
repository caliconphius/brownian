import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd


def main():
    # number of realisations to create
    num_runs = 10
    
    n = 10000 # number of increments to approximate axis
    t = 1 # final time
    time = np.linspace(0., t, n) # array of times the process is evaluated at
    dt = time[1] - time[0] # increments of time 

    dB = dt * rnd.randn(n, num_runs) # brownian motion is made of independent normally distributed increments with mean 0 and variance dt i.e deltaB ~ N(0,dt)

    Bt = [np.sum(dB[:i], axis = 0) for i in range(n)]

    
    plt.plot(time,Bt)
    plt.show()


if __name__ == '__main__':
    main()