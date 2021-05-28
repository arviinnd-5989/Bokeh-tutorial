from bokeh.plotting import figure, output_file, show
fig = figure()
x = [1,2,3,4,5]
y1 = [2,6,4,3,5]
y2 = [1,4,2,2,3]
fig.varea(x=x,y1=y1,y2=y2)
output_file('area.html')
show(fig)