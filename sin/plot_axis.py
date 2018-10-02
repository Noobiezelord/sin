import numpy as np

def setup_trigo_axis(plt, subplt, xmin, xmax):
    subplt.grid()
    subplt.spines['left'].set_position(('data', 0))
    subplt.spines['bottom'].set_position(('data', 0))

    if xmax - xmin < np.pi:
        # We wouldn't see any tick if we had one tick every pi/2
        return

    if xmax - xmin > 15 * np.pi:
        # Don't compute a uselessly large number of tick
        return
    ticks = [0.]
    labels = ["$0$"]
    
    def str_or_empty(n):
        if n == 1:
            return ""
        else:
            return str(n)
    
    n = 1
    while n*np.pi < xmax:
        ticks.append((n-.5)*np.pi)
        labels.append(r"$\frac{"+str(2*n-1)+"}{2}\pi$")
    
        ticks.append(n*np.pi)
        labels.append(r"$"+str_or_empty(n)+"\pi$")
        n = n + 1
    
    n = -1
    while n*np.pi > xmin:
        ticks.append((n+.5)*np.pi)
        labels.append(r"$-\frac{"+str(-2*n-1)+"}{2}\pi$")
    
        ticks.append(n*np.pi)
        labels.append(r"-$"+str_or_empty(-n)+"\pi$")
        n = n - 1
    
    plt.setp(subplt, xticks=ticks, xticklabels=labels)

