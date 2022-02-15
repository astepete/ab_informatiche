import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0.0,2.0,0.01)
s=1+np.sin(s*np.pi*t)
plt.plot(t,s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, floks')
plt.grid(True)
plt.savefig("test.png")
plt.show()