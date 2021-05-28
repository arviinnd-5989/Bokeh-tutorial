from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
fig = figure()
fig.line([1,2,3,4,5], [3,4,5,2,3])
string = file_html(fig, CDN, "my plot")
print(string)