from bokeh.plotting import figure, output_file, show
import math
x=2
y=4
xp02=x+0.4
xp01=x+0.1
xm01 = x-0.1
yp01 = y+0.2
ym01 = y-0.2
fig = figure(plot_width=300, plot_height=300)
fig.bezier(x0=x,y0=y,x1=xp02,y1=y,cx0=xp01,cy0=yp01,
cx1=xm01,cy1=ym01,line_color="red",line_width=2)
show(fig)