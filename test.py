import matplotlib.pyplot as plt
import numpy as np

from train import lstm

MAGIC_NUMBER = 332858

model = lstm()
model.load_weights('model.h5')

ted = np.load('ted.npy')
tel = np.load('tel.npy')

pr = model.predict(ted[:26])
pr = pr.reshape(26*14, 1)
"""
ax, f = plt.subplots(5, 1)

for i in range(len(f)):
    f[i].set_ylim(0, 1)
    f[i].plot(ted[i].reshape(26 * 14), 'r-', alpha=0.5)
    f[i].plot(tel[i].reshape(26 * 14), 'g-', alpha=0.7)
    f[i].plot(pr[i].reshape(26 * 14), 'b-')
"""
plt.plot(MAGIC_NUMBER * pr, 'r-', label='prediction')
plt.plot(MAGIC_NUMBER * tel[:26].reshape(26 * 14), 'b-', alpha=0.3, label='ground truth')
plt.title('Ayaslı GES Solar Power Prediction')
plt.ylabel('Power Generation (kWh)')
plt.xlabel('Days')
plt.legend()
plt.savefig('output.png')
plt.show()
