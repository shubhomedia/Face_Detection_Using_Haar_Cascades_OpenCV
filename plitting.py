from Motion_Object_Detection import df
import pandas
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnarDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:$S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:$S")

cds = ColumnarDataSource(df)

p = figure(x_axis_type = 'datetime', height = 100, width = 500, responsive = True, title ="Motion Graph")
p.yaxis.minor_tick_line_color= None
p.grid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start","@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q=p.quad(left="Start", right="End", bottom=0, top=1, color="red", source=cds)
output_file("Graph"+datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")+".html")
show(p)
