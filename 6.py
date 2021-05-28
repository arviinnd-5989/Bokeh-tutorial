from bokeh.plotting import figure, output_file, show
xs = [[5,3,4],[2,4,3],[2,3,5,4]]
ys = [[6,4,2],[3,6,7],[2,4,7,8]]
fig = figure()
fig.patches(xs,ys,fill_color=['red','blue','black'], line_color='white')
output_file('patch_plot.html')
show(fig)