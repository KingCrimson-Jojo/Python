import numpy as np
import matplotlib.pyplot as plt


t = np.arange(-20*np.pi, 10*np.pi, np.pi/20)
y = 2*np.cos(t - 2) + np.sin(2*t - 4)


f, Pxx_den = plt.psd(y, Fs=20/np.pi, NFFT=len(y))


plt.xlabel('Частота (Гц)')
plt.ylabel('Спектральная плотность мощности')
plt.title('Периодограмма сигнала')
plt.show()