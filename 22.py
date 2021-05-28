import pandas as pd 
df = pd.read_csv('test.csv')

from bokeh.plotting import figure, output_file, show
p = figure()
x = df['x']
y = df['pow']

p.line(x,y,line_width=2)
p.circle(x,y,size=20)
show(p)