from numpy import pi, arange, sin, linspace
x = arange(-2*pi, 2*pi, 0.1)
y = sin(x)
y2 = linspace(0,100,len(y))
from bokeh.plotting import figure, output_file, show
from bokeh.models import LinearAxis, Range1d
fig = figure(title='Twin Axis Example', y_range=(-1.1,1.1))
fig.line(x,y,color="red")
fig.extra_y_ranges={"y2":Range1d(start=0,end=100)}
fig.add_layout(LinearAxis(y_range_name="y2"),'right')
fig.line(x,y2,color="blue",y_range_name="y2")
show(fig)