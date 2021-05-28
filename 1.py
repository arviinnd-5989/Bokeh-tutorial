from bokeh.plotting import figure, output_file, show

import numpy as np 
import math
x = np.arange(0,math.pi*2, 0.05)
y = np.sin(x)

p = figure(title="sine wave example", x_axis_label = 'x', y_axis_label='y')
p.line(x,y,legend="sine", line_width=2)
output_file("sine.html")
show(p)
from bokeh.io import export_png
export_png(p, filename = "file.png")