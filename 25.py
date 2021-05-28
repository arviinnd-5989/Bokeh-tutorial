from bokeh.plotting import figure, output_file, show
import pandas as pd
from bokeh.models import ColumnDataSource, CDSView, IndexFilter, BooleanFilter
source = ColumnDataSource(data=dict(x=list(range(1,11)), y=list(range(2,22,2))))
view = CDSView(source=source, filters=[IndexFilter([0,2,4,6])])
fig = figure(title='Line Plot example', x_axis_label='x',y_axis_label='y')
fig.circle(x="x", y="y", size=10, source=source, view=view, legend="filtered")
fig.line(source.data['x'], source.data['y'], legend="unfiltered")
show(fig)