
import plotly.graph_objects as go

x = [
    ["BB+", "BB+", "BB+", "BB", "BB", "BB"],
    [16, 17, 18, 16, 17, 18,]
]
fig = go.Figure()
fig.add_bar(x=x,y=[1,2,3,4,5,6])
fig.add_bar(x=x,y=[6,5,4,3,2,1])
fig.update_layout(barmode="relative")
fig.show()