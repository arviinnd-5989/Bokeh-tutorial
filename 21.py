from bokeh.plotting import figure, output_file, show
import numpy as np 
import math
x = np.arange(0,math.pi*2,0.05)
fig= figure()
fig.line(x,np.sin(x), line_width=2,line_color="navy", legend="sine")
fig.circle(x,np.cos(x),line_width=2,line_color="orange", legend="cosine")
fig.square(x, -np.sin(x),line_width=2,line_color="grey", legend="-sine")
show(fig)