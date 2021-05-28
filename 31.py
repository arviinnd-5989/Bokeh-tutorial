# from bokeh.layouts import column
# from bokeh.models import CustomJS, ColumnDataSource
# from bokeh.plotting import Figure, output_file, show
# from bokeh.models import Button

# x = [x*0.05 for x in range(0, 200)]
# y = x

# source = ColumnDataSource(data=dict(x=x, y=y))
# plot = Figure(plot_width=400, plot_height=400)
# plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

# callback = CustomJS(args=dict(source=source), code="""
#    var data = source.data;
#    x = data['x']
#    y = data['y']
#    for (i = 0; i < x.length; i++) {
#       y[i] = Math.pow(x[i], 4)
#    }
#    source.change.emit();
# """)

# btn = Button(label="click here", name="1")
# btn.js_on_click(CustomJS(code="console.log(arvind)"))

# layout = column(btn , plot)
# show(layout)

from bokeh.io import show
from bokeh.models import Button, CustomJS

button = Button(label="Foo", button_type="success")
button.js_on_click(CustomJS(code="console.log('button: click!', this.toString())"))

show(button)