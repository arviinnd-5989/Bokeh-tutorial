from bokeh.plotting import figure, output_file, show
x =[0.1,0.5,1.0,1.5,2.0,2.5,3.0]
y = [10**i for i in x]
fig = figure(title='Linear scale example',plot_width=400, plot_height=400, y_axis_type="log")
fig.line(x,y,line_width=2)
show(fig)