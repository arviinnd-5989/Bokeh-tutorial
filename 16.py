from bokeh.plotting import figure, output_file, show
langs = ['C','C++','Java','Python','PHP']
cols = ['red','green','orange','navy','cyan']
students = [23,17,35,29,12]
fig = figure(x_range=langs,plot_width=300, plot_height=300)
fig.vbar(x=langs,top=students,color=cols,width=0.5)
show(fig)