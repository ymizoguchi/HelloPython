import math
import numpy as np
from matplotlib import pyplot
pi = math.pi
x = np.linspace(0, 2*pi, 100)
y0 = np.sin(x)
y1 = np.cos(x) 
pyplot.plot(x, y0, label='sin')
pyplot.plot(x, y1, label='cos')
pyplot.title('sin(x) and cos(x) (0 < x < 2pi)')
pyplot.legend()
pyplot.show()
