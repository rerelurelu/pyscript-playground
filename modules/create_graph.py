import numpy as np
from numpy import pi, sin, cos
import matplotlib.pyplot as plt

def create_graph(*ags, **kwgs):
    t = np.arange(0,2*pi,0.01)
    x = 16*sin(t)**3
    y = 13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t)
    fig, ax = plt.subplots()
    ax.fill_between(x, y, facecolor='red', alpha=0.5)

    return fig
