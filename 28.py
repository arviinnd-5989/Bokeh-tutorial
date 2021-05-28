from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
import numpy as np 
import math
x = np.arange(0, math.pi*2, 0.05)
y1 = np.sin(x)
y2 = np.cos(x)
fig1 = figure(plot_width=200, plot_height=200)
fig1.line(x, y1, line_width=2, line_color='blue')
fig2 = figure(plot_width=200, plot_height=200)
fig2.line(x, y2, line_width=2, line_color='red')
c = column(children=[fig1,fig2], sizing_mode='stretch_both')
show(c)
