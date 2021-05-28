from bokeh.plotting import figure, output_file, show
from bokeh.models import Panel, Tabs
import numpy as np
import math
x=np.arange(0, math.pi*2, 0.05)
fig1=figure(plot_width=300, plot_height=300)

fig1.line(x, np.sin(x),line_width=2, line_color='navy')

tab1 = Panel(child=fig1, title="sine")
fig2=figure(plot_width=300, plot_height=300)
fig2.line(x,np.cos(x), line_width=2, line_color='orange')
tab2 = Panel(child=fig2, title="cos")

tabs = Tabs(tabs=[ tab1, tab2 ])

show(tabs)