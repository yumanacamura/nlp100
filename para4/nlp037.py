from nlp036 import freq
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'AppleGothic'

param = list(zip(*freq[:10]))
plt.bar(range(10),param[1],tick_label=param[0])
plt.show()
