from bokeh.plotting import figure, output_file, show
from bokeh.models import DataRange1d
xrange = DataRange1d(0,10)
fig = figure(plot_width=300, plot_height=300, x_range=xrange)
show(fig)