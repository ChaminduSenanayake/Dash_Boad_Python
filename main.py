import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
import base64
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ---------------------------------------------------------------
# Taken from https://opendata.cityofnewyork.us/
# myfile = open('./assets/winequality-red.csv')
df = pd.read_csv("./assets/winequality-red.csv")
coding = {"quality": {0 : "low", 1:"low", 2: "low", 3:"low", 4:"moderate", 5:"moderate",
                      6:"moderate", 7:"high", 8:"high", 9:"high", 10:"high"}}
df = df.replace(coding)
# ---------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------
# encode images
image_filename1 = './assets/graph-bar.png'# replace with your own image
encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())

image_filename2 = './assets/wine-glass.png'# replace with your own image
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())

image_filename3 = './assets/stats.png'# replace with your own image
encoded_image3 = base64.b64encode(open(image_filename3, 'rb').read())
# ---------------------------------------------------------------------------------------------------------------------------


app.layout = html.Div([
    html.Div([
        html.Div(id="title"),
        html.Label(['DashBoard - Red Wine'], style={"font": "bold 30px sans-serif", "color": "#E9E9E9"})
    ], style={"height": "50px", "text-align": "center", "background-color": "#212529", "padding-top": "17px"}),

    # -----------------------------------------------------------------------------------------------------------------------

    html.Div([
        html.Div([
            html.Label("Total Number Of Data Values", style={"font": "15px sans-serif", "color": "#ABABAB","margin":"40px","margin-right":"0px","float":"left"}),
            html.Label(df['quality'].count(), style={"font": "bold 35px sans-serif", "color": "#ffffff","margin-left":"30px","margin-top":"30px","float":"left"}),
            html.Label(html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()),style={"margin-top":"17px","margin-left":"40px","margin-bottom":"10px","float":"Left"}))
        ], style={"background-color": "#2c3135", "display": " table-cell"}),
        html.Div([
            html.Label("No Of Explantory Variables",style={"font": "15px sans-serif", "color": "#ABABAB", "margin": "40px", "margin-right": "0px","float": "left"}),
            html.Label(" 11 ",style={"font": "bold 35px sans-serif", "color": "#ffffff","margin-left": "50px", "margin-top": "30px", "float": "left"}),
            html.Label(html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()),style={"margin-top": "17px", "margin-right": "40px","margin-bottom": "10px", "float": "right"}))
        ], style={"background-color": "#2c3135", "display": " table-cell"}),
        html.Div([
            html.Label("Categories Of Response",style={"font": "15px sans-serif", "color": "#ABABAB", "margin": "40px", "margin-right": "0px","float": "left"}),
            html.Ul([
                html.Li("Low 0-3", style={"font": "12px sans-serif", "color": "#ABABAB"}),
                html.Li("Moderate 4-6", style={"font": "12px sans-serif", "color": "#ABABAB"}),
                html.Li("High 7-10", style={"font": "12px sans-serif", "color": "#ABABAB"})
            ],style={ "margin": "0px","margin-top":"32px","float": "left","list-style-type":"none"}),
            html.Label(html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),style={"margin-top": "15px", "margin-right": "40px","margin-bottom": "10px", "float": "right"}))
        ], style={"background-color": "#2c3135", "display": " table-cell"}),
    ], style={"display": "table", "width": "100%", "table-layout": "fixed", "border-spacing": "20px","margin-top":"-20px"}),

    # -----------------------------------------------------------------------------------------------------------------------

    html.Div([
        html.Label(["Choose variable:"], style={"font-weight": "bold","font-family": "sans-serif", "margin": "10px", "color": "#E9E9E9"}),
        dcc.Dropdown(id='my_dropdown',
                    options=[
                        {'label': 'fixedacidity ', 'value': 'fixedacidity'},
                        {'label': 'volatile acidity', 'value': 'volatile acidity'},
                        {'label': 'citric acid', 'value': 'citric acid'},
                        {'label': 'residual sugar', 'value': 'residual sugar'},
                        {'label': 'chlorides', 'value': 'chlorides'},
                        {'label': 'free sulfur dioxide', 'value': 'free sulfur dioxide'},
                        {'label': 'total sulfur dioxide', 'value': 'total sulfur dioxide'},
                        {'label': 'density ', 'value': 'density'},
                        {'label': 'pH ', 'value': 'pH'},
                        {'label': 'sulphates ', 'value': 'sulphates'},
                        {'label': 'alcohol ', 'value': 'alcohol'}],

                    value='fixedacidity',  # dropdown value selected automatically when page loads
                    disabled=False,  # disable dropdown value selection
                    searchable=True,  # allow user-searching of dropdown values
                    placeholder='Please select...',  # gray, default text shown when no option is selected
                    clearable=True , # allow user to removes the selected value
                    #style={"background-color": "#2c3135","margin-top":"10px","margin-bottom":"-20px"},
        ),

        html.Div([
            html.Div([
                html.H2(id="graph_1_title", style={"color": "#E9E9E9", "text-align": "center","font-family": "sans-serif"}),
                dcc.Graph(id="our_graph1")
            ], style={"display": " table-cell"}),
            html.Div([
                html.H2(id="graph_2_title", style={"color": "#E9E9E9", "text-align": "center", "font-family": "sans-serif"}),
                dcc.Graph(id="our_graph2")
            ], style={"display": " table-cell"})
        ], style={"display": "table", "width": "100%", "table-layout": "fixed", "border-spacing": "20px","margin-bottom":"-20px"}),
    ], style={"background-color": "#2c3135", "padding": "15px","margin":"20px","margin-top":"0px"}),


    # ------------------------------------------------------------------------------------------------------------------
    html.Div([
        html.Div([
            html.H2("Response Variable", style={"color": "#E9E9E9", "text-align":"center","font-family": "sans-serif"}),
            dcc.RadioItems(id="radioButton",
                           options=[
                                {'label': 'Bar Chart', 'value': 'BarChart'},
                                {'label': 'Pie Chart', 'value': 'PieChart'},
                            ],
                           value="PieChart",
                           style={"color": "#E9E9E9", "text-align":"center","font-family": "sans-serif","margin":"20px"}
                           ),
            dcc.Graph(id='responseVariableChart')
        ], style={"height": "400px","background-color": "#2c3135", "display": " table-cell"}),

        html.Div([
            html.Label(["Select Variable:"],  style={"font-weight": "bold","font-family": "sans-serif", "margin": "10px", "color": "#E9E9E9"}),
            dcc.Dropdown(id="my_dropdown2",
                         options=[
                             {'label': 'Scatterplot of citric acid vs pH', 'value': 'citric acid'},
                             {'label': 'Scatterplot of volatile acid vs pH', 'value': 'volatile acidity'},
                             {'label': 'Scatterplot of fixedacidity vs pH', 'value': 'fixedacidity'},
                             {'label': 'Scatterplot of alcohol vs residual sugar', 'value': 'alcohol'}],
                         value='citric acid',
                         searchable=True,
                         placeholder='Please select...',
                         clearable=True,
                         #style={"background-color": "#2c3135","margin-top":"10px"},
                         ),
            html.H2(id="graph_4_title", style={"color": "#E9E9E9", "text-align":"center", "font-family": "sans-serif"}),
            html.Div([
                dcc.Graph(id="our_graph4")
            ])
        ], style={"background-color": "#2c3135", "display": " table-cell","padding": "15px"})
    ], style={"display": "table", "width": "100%", "table-layout": "fixed", "border-spacing": "20px","margin-bottom": "-20px", "margin-top": "-20px"}),
], style={"margin": "-8px", "background-color": "#212529"})


# ---------------------------------------------------------------
# set Titles for graphs
@app.callback(
    Output(component_id='graph_1_title', component_property='children'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def build_graph(data_chosen):
    tit = ('Histogram of {} '.format(data_chosen))
    return tit


@app.callback(
    Output(component_id='graph_2_title', component_property='children'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def build_graph(data_chosen):
    tit = ('Boxplot of {} Vs quality'.format(data_chosen))
    return tit

# ---------------------------------------------------------------
# Connecting the Dropdown values to the graph
# Creating univariate histograms

@app.callback(
    Output(component_id='our_graph1', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def build_graph(column_chosen):
    dff = df
    col2 = column_chosen
    if col2 == "fixedacidity":
        bar_color = "#006382"
    elif col2 == "volatile acidity":
        bar_color = "#009A73"
    elif col2 == "citric acid":
        bar_color = "#7C5592"
    elif col2 == "residual sugar":
        bar_color = "#D4AC0D"
    elif col2 == "chlorides":
        bar_color = "#C0392B"
    elif col2 == "free sulfur dioxide":
        bar_color = "#07758A"
    elif col2 == "total sulfur dioxide":
        bar_color = "#925AAC"
    elif col2 == "density":
        bar_color = "#AEAEAE"
    elif col2 == "pH":
        bar_color = "#EA9358"
    elif col2 == "sulphates":
        bar_color = "#627DCF"
    elif col2 == "alcohol":
        bar_color = "#D7399D"
    else:
        bar_color = "#EA9358"
    fig = px.histogram(dff, x=col2, nbins=30, height=380, opacity=0.8, color_discrete_sequence=[bar_color])
    fig.layout.plot_bgcolor = "#2c3135"
    fig.layout.paper_bgcolor = "#2c3135"
    fig.update_layout(
        bargap=0.01,
        font_family="sans-serif",
        font_color="#C3C3C3",
        #margin=dict(t=0, b=0)
    )
    return fig


# Creating bivariate boxplots
@app.callback(
    Output(component_id='our_graph2', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def build_graph(column_chosen):
    dff = df
    fig = px.box(dff, x="quality", y=column_chosen, color="quality", height=380)
    fig.update_xaxes(type='category')
    fig.layout.plot_bgcolor = "#2c3135"
    fig.layout.paper_bgcolor = "#2c3135"
    fig.update_layout(
        font_family="sans-serif",
        font_color="#C3C3C3",
        legend_title_font_color="#3E8E68",
        #margin = dict(t=15, b=0),
    )
    return fig

# ---------------------------------------------------------------
# Creating response variable barchart
@app.callback(
    Output(component_id='responseVariableChart', component_property='figure'),
    [Input(component_id='radioButton', component_property='value')]
)
def build_graph(chart_chosen):
    if chart_chosen == "PieChart":
        fig = px.pie(df, names=df["quality"], height=550,opacity=0.8)
    if chart_chosen == "BarChart":
        fig = px.bar(df["quality"], x="quality", height=580,opacity=0.8)
    fig.layout.plot_bgcolor = "#2c3135"
    fig.layout.paper_bgcolor = "#2c3135"
    fig.update_layout(
        font_family="sans-serif",
        font_color="#C3C3C3",
        legend_title_font_color="#3E8E68",
        #margin=dict(t=30, b=0),
    )
    return fig

# ---------------------------------------------------------------
# Connecting the Dropdown values to the graph
# Set Graph title
@app.callback(
    Output(component_id='graph_4_title', component_property='children'),
    [Input(component_id='my_dropdown2', component_property='value')]
)
def build_graph(data_chosen):
    if data_chosen == "alcohol":
        tit = ('ScatterPlot of {} Vs residual sugar'.format(data_chosen))
    else:
        tit = ('ScatterPlot of {} Vs pH'.format(data_chosen))
    return tit

# Creating bivariate scatterplot
@app.callback(
    Output(component_id='our_graph4', component_property='figure'),
    [Input(component_id='my_dropdown2', component_property='value')]
)

def build_graph(column_chosen):
    dff = df
    col = column_chosen
    if col == "alcohol":
        xx = dff["residual sugar"]
    else:
        xx = dff["pH"]

    fig = px.scatter(dff, x=xx, y=df[column_chosen], color="quality", height=550)
    fig.layout.plot_bgcolor = "#2c3135"
    fig.layout.paper_bgcolor = "#2c3135"
    fig.update_layout(
        font_family="sans-serif",
        font_color="#C3C3C3",
        legend_title_font_color="#3E8E68",
        #margin=dict(t=15, b=0),

    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
