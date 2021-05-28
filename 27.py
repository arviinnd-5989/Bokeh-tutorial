from bokeh.models import ColumnDataSource, CDSView, CustomJSFilter
from bokeh.plotting import figure, show
from bokeh.sampledata.unemployment1948 import data
source = ColumnDataSource(data)
custom_filter = CustomJSFilter(code = '''
   var indices = [];

   for (var i = 0; i < source.get_length(); i++){
      if (parseInt(source.data['Year'][i]) > = 1980){
         indices.push(true);
      } else {
         indices.push(false);
      }
   }
   return indices;
''')
view1 = CDSView(source = source, filters = [custom_filter])
p = figure(title = "Unemployment data", x_range = (1980,2020), x_axis_label = 'Year', y_axis_label = 'Percentage')
p.line(x = 'Year', y = 'Annual', source = source, view = view1, color = 'red', line_width = 2)
show(p)