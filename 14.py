from bokeh.plotting import figure, output_file, show
import math
x=2
y=4
xp02=x+0.3
xp01=x+0.2
xm01 = x-0.4
yp01 = y+0.1
ym01 = y-0.2
# x=x,
# y=y,
# xp02 = x+0.4,
# xp01 = x+0.1,
# yp01 = y + 0.2,
fig = figure(plot_width=300, plot_height=300)
fig.quadratic(x0=x,y0=y,x1=x+0.4,y1=y+0.01,cx=x+0.1,
cy=y+0.2,line_color="blue",line_width=3)
show(fig)