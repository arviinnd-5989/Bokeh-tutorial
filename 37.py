from bokeh.embed import server_document
script = server_document("http://localhost:5006/sliders")
print(script)