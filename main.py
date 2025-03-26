import seaborn as sns
import dash
from dash import dcc
from dash import html
import plotly.express as px
from dash import Input, Output



df = sns.load_dataset('tips')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Tips Dataset Analysis'),
    dcc.RadioItems(
        id = 'x-axis',
        options = [
            {'label': 'Sex', 'value': 'sex'},
            {'label': 'Smoker', 'value': 'smoker'},
            {'label': 'Day', 'value': 'day'},
            {'label': 'Time', 'value': 'time'},
        ]
    ),
    
    dcc.Graph(id='graph')
])

@app.callback(
    Output('graph', 'figure'),
    [Input('x-axis','value')]
)

def update_graph(x_axis):
    if x_axis == 'sex':
        fig = px.box(df, x = 'sex', y = 'total_bill')
    elif x_axis == 'smoker':
        fig = px.box(df, x = 'smoker', y = 'total_bill')
    elif x_axis == 'day':
        fig = px.box(df, x = 'day', y = 'total_bill')
    else:
        fig = px.box(df, x = 'time', y = 'total_bill')

    return fig




if __name__ == '__main__':
    app.run(debug=True, port = 8050)