import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap

__all__ = ['colormap']

viridis = cm.get_cmap('viridis', 256)
newcolors = viridis(np.linspace(0, 1, 256))
high_points = np.array([15/255, 15/255, 35/255, 1])
basins = np.array([27/255, 27/255, 57/255, 1])
silver = np.array([153/255, 153/255, 204/255, 1])
gold = np.array([1., 1., 102/255, 1])
newcolors[:64, :] = high_points
newcolors[64:128, :] = basins
newcolors[128:191, :] = silver
newcolors[191:250, :] = gold
newcolors[250:, :] = np.array([1., 0., 0., 1])  # red
colormap = ListedColormap(newcolors)
