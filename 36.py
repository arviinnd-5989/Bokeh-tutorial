from bokeh.plotting import figure
from bokeh.embed import json_item
import json
fig = figure()
fig.line([1,2,3,4,5], [3,4,5,2,3])
item_text = json.dumps(json_item(fig, "myplot"))
print(item_text)