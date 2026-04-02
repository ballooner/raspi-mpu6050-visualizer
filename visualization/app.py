from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv(r"../data/Moving/filteredData.csv")

app = Dash()

fig = figure=px.line(df, x="t",y="x", title="Gyroscope x")
fig.update_layout(
    xaxis_title="Time (s)",
    yaxis_title="Deg/s"
)

# Requires Dash 2.17.0 or later
app.layout = [
    html.H1(children='Gyrometer data', style={'textAlign':'center'}),
    dcc.Graph(figure=fig)
]

if __name__ == '__main__':
    app.run(debug=True)
