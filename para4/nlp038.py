from nlp036 import freq
import matplotlib.pyplot as plt

param = list(zip(*freq))
plt.hist(param[1],bins=max(param[1]))
plt.show()
