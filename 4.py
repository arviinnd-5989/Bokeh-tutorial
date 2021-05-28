from bokeh.plotting import figure, output_file, show
fig = figure(plot_width = 400, plot_height = 200)
fig.vbar(x = [1,2,3], width = 0.5, bottom = 0, top = [2,4,6], color = "cyan")
output_file('bar2.html')
show(fig)