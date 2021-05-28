from bokeh.plotting import figure, output_file, show
fig = figure()
fig.scatter([1,4,3,2,5],[6,5,2,4,7],marker="circle", size=20, fill_color="grey")
output_file('scatter.html')
show(fig)