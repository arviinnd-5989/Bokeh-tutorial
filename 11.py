from bokeh.plotting import figure, output_file, show
fig = figure(plot_width=300, plot_height=300)
fig.rect(x=10,y=10,width=100,height=50,width_units='screen',height_units='screen')
fig.square(x=2,y=3,size=80,color='red')
fig.ellipse(x=7,y=6,width=30,height=10,fill_color=None,line_width=2)
fig.oval(x=6,y=6,width=2,height=1,angle=-3.14/4)
show(fig)