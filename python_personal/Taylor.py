import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def cos_taylor(x, n):
    result = 0
    for i in range(n+1):
        result += ((-1)**i) * (x**(2*i)) / np.math.factorial(2*i)
    return result

fig, ax = plt.subplots()
x = np.linspace(-np.pi, 2*np.pi, 200)
cos_line, = ax.plot(x, np.cos(x), label='cos(x)')
taylor_line, = ax.plot(x, x, label='Taylor Series')

ax.set_ylim(-2, 2)
ax.legend(loc='upper left')
ax.set_title("Cosine Taylor Series Approximation")


text = ax.text(0.05, 0.05, '', transform=ax.transAxes, verticalalignment='bottom')
def update(frame):
    taylor_line.set_ydata(cos_taylor(x, frame))
    text.set_text(f'Terms: {frame}')
    return taylor_line, text

anim = FuncAnimation(fig, update, frames=range(0, 11), interval=500, blit=True)
plt.show()