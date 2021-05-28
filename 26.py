from bokeh.models import ColumnDataSource, CDSView, BooleanFilter
from bokeh.plotting import figure, show
from bokeh.sampledata.unemployment1948 import data
source = ColumnDataSource(data)
booleans = [True if int(year) >= 1980 else False for year in
source.data['Year']]
print (booleans)
view1 = CDSView(source = source, filters=[BooleanFilter(booleans)])
p = figure(title = "Unemployment data", x_range = (1980,2020), x_axis_label = 'Year', y_axis_label='Percentage')
p.line(x = 'Year', y = 'Annual', source = source, view = view1, color = 'red', line_width = 2)
show(p)