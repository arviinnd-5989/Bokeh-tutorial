from bokeh.plotting import figure, output_file, show
p = figure(plot_width = 300, plot_height = 300)
p.patch(x = [1,3,2,4], y = [2,3,5,7], color = "green")
output_file('patch.html')
show(p)