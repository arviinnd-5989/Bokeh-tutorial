from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

data = {'x':[1,4,3,2,5],
'y':[6,5,2,4,7]}
cds = ColumnDataSource(data=data)
fig = figure()
fig.scatter(x='x', y='y', source=cds,marker="circle", size=20, fill_color="grey")
show(fig)