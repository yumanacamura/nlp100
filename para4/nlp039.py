from nlp036 import freq
import matplotlib.pyplot as plt

param = list(zip(*freq))
plt.plot(range(len(param[0])),param[1])
plt.xscale('log')
plt.yscale('log')
plt.show()
