from bokeh.plotting import figure, output_file, show
products = ['computer','mobile','printer']
months=['Jan','Feb','Mar']
sales = {'products':products,
'Jan':[10,40,5],
'Feb':[8,45,10],
'Mar':[25,60,22]}
cols = ['red','green','blue']#,'navy','cyan']
fig = figure(x_range=products,plot_width=300, plot_height=300)
fig.vbar_stack(months, x='products',source=sales,color=cols, width=0.5)
show(fig)