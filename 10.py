from bokeh.plotting import figure, output_file, show
plot = figure(plot_width=300, plot_height=300)
plot.circle(x=[1,2,3],y=[3,7,5],size=20, fill_color='red')
plot.circle_cross(x=[2,4,6],y=[5,8,9], size=20,fill_color='blue', fill_alpha=0.2,line_width=2)
plot.circle_x(x=[5,7,2],y=[2,4,9],size=20,fill_color='green',fill_alpha=0.6, line_width=2)
show(plot)