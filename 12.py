from bokeh.plotting import figure, output_file, show
import math
fig = figure(plot_width=300, plot_height=300)
fig.arc(x=3,y=3,radius=50,radius_units='screen',start_angle=0.0, end_angle=math.pi/2)
fig.wedge(x=3,y=3,radius=30,radius_units='screen',
start_angle=0, end_angle=math.pi,direction='clock')
fig.annular_wedge(x=3,y=3,outer_radius=75,inner_radius=100, outer_radius_units='screen',
inner_radius_units='screen', start_angle=0.4, end_angle=4.5, color='green', alpha=0.6)
show(fig)