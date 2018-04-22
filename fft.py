import matplotlib.pyplot as plt
import numpy as np
import random as rnd

Fs = 550.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0.1, 1, Ts) # time vector

ff = 5;   # frequency of the signal
w = 2*np.pi*ff
y = np.sin(15*w*t)#+np.sin(2*w*t) # sin
# y = t/t # constant
l = 40*np.sin(0.2*w*t)
# l = [rnd.random()-rnd.random() for _ in xrange(len(t))] # white noise
y = y+l

# f = np.zeros
# for
# y = np.exp(-((0.5-t)**2)/0.01) # gauss
# y = np.zeros(len(t)); y[int(len(t)/2)] = 1 # delta


avg = np.sum(y)/len(t)
av = np.full(len(t), avg)
print avg

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(n/2)] # one side frequency range

g = np.fft.fft(y)/n # fft computing and normalization
g = g[range(n/2)]

fig, ax = plt.subplots(2, 1)
ax[0].plot(t, y)
ax[0].plot(t, av)
ax[0].set_xlabel(r"$t$")
ax[0].set_ylabel(r"$A$")
ax[1].plot(frq, abs(g),'r') # plotting the spectrum
ax[1].set_xlabel(r"$\omega$")
ax[1].set_ylabel(r"$g$")
plt.show()
