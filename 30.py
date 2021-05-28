from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
import math
x = list(range(1,11))

y1 = x
y2 =[11-i for i in x]
y3 = [i*i for i in x]
y4 = [math.log10(i) for i in x]

fig1 = figure(plot_width = 200, plot_height = 200)
fig1.line(x, y1,line_width = 2, line_color = 'blue')
fig2 = figure(plot_width = 200, plot_height = 200)
fig2.circle(x, y2,size = 10, color = 'green')
fig3 = figure(plot_width = 200, plot_height = 200)
fig3.circle(x,y3, size = 10, color = 'grey')
fig4 = figure(plot_width = 200, plot_height = 200, y_axis_type = 'log')
fig4.line(x,y4, line_width = 2, line_color = 'red')
grid = gridplot(children = [[fig1, fig2], [fig3,fig4]], sizing_mode = 'stretch_both')
show(grid)