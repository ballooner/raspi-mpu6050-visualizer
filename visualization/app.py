from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from util.constants import DATA_DIR
import os

app = Dash()

app.layout = [
    html.H1(children='Gyrometer data', style={'textAlign':'center'}),
    dcc.Dropdown(os.listdir(DATA_DIR), "", id="data-folders"),
    dcc.RadioItems(["Filtered", "Raw"], "Filtered", id="data-type"),
    dcc.Graph(id="gyro-x"),
    dcc.Graph(id="gyro-y"),
    dcc.Graph(id="gyro-z"),
]

@callback(
    Output("gyro-x", "figure"),
    Output("gyro-y", "figure"),
    Output("gyro-z", "figure"),
    Input("data-folders", "value"),
    Input("data-type", "value"),
)
def updateGraphs(dataFolder, dataType):
    if (dataFolder == ""):
        return [px.line(), px.line(), px.line()]

    dataFile = DATA_DIR / dataFolder
    if (dataType == "Filtered"):
        dataFile /= "filteredData.csv"
    else:
        dataFile /= "rawData.csv"

    data = pd.read_csv(dataFile)

    xFig = createFigure(data, "t", "x", "Gyro X Measurements")
    yFig = createFigure(data, "t", "y", "Gyro Y Measurements")
    zFig = createFigure(data, "t", "z", "Gyro Z Measurements")

    return xFig, yFig, zFig
    
def createFigure(dataFrame, xHeader, yHeader, graphTitle):
    fig = px.line(dataFrame, x=xHeader,y=yHeader, title=graphTitle)
    fig.update_layout(
        xaxis_title="Time (s)",
        yaxis_title=yHeader + "Deg/s"
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)
