import numpy as np
from bokeh.plotting import figure, show, output_file
N = 10000
x = np.random.normal(0, np.pi, N)
y = np.sin(x) + np.random.normal(0, 0.2, N)
output_file("scatterWebGL.html")
p = figure(output_backend="webgl")
p.scatter(x, y, alpha=0.1)
show(p)