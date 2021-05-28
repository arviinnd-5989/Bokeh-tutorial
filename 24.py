from bokeh.plotting import figure, output_file, show
import pandas as pd
from bokeh.models import ColumnDataSource
df = pd.read_csv('test.csv')

cds = ColumnDataSource(df)
fig = figure(y_axis_type='log')
fig.line(x='x', y='pow', source=cds,line_color="grey")
show(fig)