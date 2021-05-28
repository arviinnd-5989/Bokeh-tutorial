from bokeh.plotting import figure, output_file, show
from bokeh.transform import dodge
products = ['computer','mobile','printer']
months=['Jan','Feb','Mar']
sales = {'products':products,
'Jan':[10,40,5],
'Feb':[8,45,10],
'Mar':[25,60,22]}
cols = ['red','green','blue']#,'navy','cyan']
fig = figure(x_range=products,plot_width=300, plot_height=300)
fig.vbar(x=dodge('products',-0.25,range=fig.x_range), top = 'Jan', width=0.2, source=sales, color="red")
fig.vbar(x=dodge('products',0,range=fig.x_range), top = 'Feb', width=0.2, source=sales, color="green")
fig.vbar(x=dodge('products',0.25,range=fig.x_range), top = 'Mar', width=0.2, source=sales, color="blue")
show(fig)