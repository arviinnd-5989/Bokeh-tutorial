from bokeh.plotting import figure, output_file, show
fig = figure()
y = [1,2,3,4,5]
x1 = [2,6,4,3,5]
x2 = [1,4,2,2,3]
fig.harea(x1=x1,x2=x2,y=y)
output_file('area2.html')
show(fig)