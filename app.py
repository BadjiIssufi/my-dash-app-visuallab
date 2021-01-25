import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

from dash.dependencies import Input, Output

df = pd.read_csv('dmr.csv')
# print(df.columns)
df_faixaEtaria = df.groupby(['idade']).sum()
df_visita = df.groupby(['data_vista']).sum()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

colors = {
    'background': '#111111',
    'text': '#c83349'
}

colors2 = {
    'background': '#FFFFFF',
    'text': '#36486b'
}

app.layout = dbc.Container(children=[
    html.Br(),
    html.H1(
        children='Visualização de Dados do Visual Lab',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'backgroundColor': colors['background']
        }
    ),

    dbc.Container(
        [
            dcc.Store(id="store"),
            html.H1("Banco de dados de imagens mastológicas",
                    style={
                        'textAlign': 'center',
                    }),
            html.Hr(),
            html.Div(
                dbc.Row([
                    dbc.Card(
                        [
                            dbc.CardHeader("TOTAL DE IMAGEM NO BANCO"),
                            dbc.CardBody(
                                [
                                    html.H4("Total de 5939", className="card-title"),
                                    html.P("Pacientes no banco", className="card-text"),
                                    dbc.Button(
                                        [dbc.Spinner(size="sm"), " Loading..."],
                                        color="primary",
                                        disabled=True,
                                    ),

                                ]
                            ),
                        ],
                        style={"width": "17rem"},
                    ),

                    dbc.Card(
                        [
                            dbc.CardHeader("TOTAL DE PACIENTE NO BANCO"),
                            dbc.CardBody(
                                [
                                    html.H4("Total de 244", className="card-title"),
                                    html.P("Pacientes no banco", className="card-text"),
                                    dbc.Button(
                                                [dbc.Spinner(size="sm"), " Loading..."],
                                                color="primary",
                                                disabled=True,
                                            ),
                                ]
                            ),
                        ],
                        style={"width": "17rem"},
                    ),
                        dbc.Card(
                        [
                            dbc.CardHeader("PACIENTES COM CANCER"),
                            dbc.CardBody(
                                [
                                    html.H4("Total de 47", className="card-title"),
                                    html.P("Pacientes com cancer no banco", className="card-text"),
                                    dbc.Button(
                                                [dbc.Spinner(size="sm"), " Loading..."],
                                                color="primary",
                                                disabled=True,
                                            ),
                                ]
                            ),
                        ],
                        style={"width": "17rem"},
                    ),

                    dbc.Card(
                        [

                            dbc.CardHeader("PACIENTES SEM CANCER"),

                            dbc.CardBody(
                                [
                                    html.H4("Total de 184" , className="card-title"),
                                    html.P("Pacientes sem cancer no banco", className="card-text"),
                                    dbc.Button(
                                                [dbc.Spinner(size="sm"), " Loading..."],
                                                color="primary",
                                                disabled=True,
                                            ),
                                ]
                            ),
                        ],
                        style={"width": "17rem"},
                    )
                ]
                )
            ),
            html.Br(),
            html.Div(id='tabs-content-inline'),
            dcc.Dropdown(
                id='dd_diagnostico',
                options=[
                    {'label': 'Diognóstico Saudável', 'value': 'diagnostico_Saudavel'},
                    {'label': 'Diognóstico Doente', 'value': 'diagnostico_doente'},
                    {'label': 'Mamografia', 'value': 'mamografia'}
                ],
                value=[ 'diagnostico_doente','diagnostico_Saudavel','mamografia'],
                multi=False,
                clearable=False,
                searchable=True,

            ),
            html.Br(),
            html.Div(children='Diagonstigo em relação a Faixa Etária', style={
                'textAlign': 'center',
                'color': colors['text']
            }),
            dcc.Graph(
                id='fig_diagnostico',
            ),
            html.Hr(),
            html.Br(),
            html.Br(),

            dcc.Dropdown(
                id='dd_bar',
                options=[
                    {'label': 'Radioterapia', 'value': 'radioterapia'},
                    {'label': 'Diognostico Saudavel', 'value': 'diagnostico_Saudavel'},
                    {'label': 'Diognostico Doente', 'value': 'diagnostico_doente'},
                    {'label': 'Mamografia', 'value': 'mamografia'}

                ],
                value=['radioterapia','mamografia'],
                multi=True,
                clearable=False,
                searchable=True
            ),
            dcc.Graph(
                id='fig_bar'
            ),
            html.Hr(),
            html.Br(),
            html.Br(),



            dcc.Dropdown(
                id='dd_violino',
                options=[
                    {'label': 'Mamografia', 'value': 'mamografia'},
                    {'label': 'Diognostico saudavel', 'value': 'diagnostico_Saudavel'},
                    {'label': 'Radioterapia', 'value': 'radioterapia'},
                    {'label': 'Protese', 'value': 'Protese'},
                    {'label': 'Cirugia Duas Mama', 'value': 'cirugiaPlastico_DuasMama'},
                    {'label': 'Biopisia duas Mamas', 'value': 'biopisia_duasMamas'},
                ],
               value='mamografia',
                multi=False,
                clearable=False,
                searchable=True,

            ),
            html.Br(),
            html.Div(children='Diagonstigo em relação a faixa etária', style={
                'textAlign': 'center',
                'color': colors['text']
            }),
            dcc.Graph(
                id='fig_violino',
            ),
            html.Hr(),
            html.Br(),
            html.Br(),
            dcc.Dropdown(
                id='dd_situacao',
                options=[
                    {'label': 'Diognóstico saudável', 'value': 'diagnostico_Saudavel'},
                    {'label': 'Diognóstico doente', 'value': 'diagnostico_doente'},

                ],
                value=['diagnostico_Saudavel'],
                multi=True,
                clearable=False,
                searchable=True
            ),
            html.Br(),
            html.Div(children='Diagnostigo de multiplo entrada em relação a faixa etária', style={
                'textAlign': 'center',
                'color': colors['text']
            }),
            dcc.Graph(
                id='fig_dd_situacao'
            ),
            html.Hr(),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                id='dd_situacao1',
                options=[
                    {'label': 'Diognostico saudavel', 'value': 'diagnostico_Saudavel'},
                    {'label': 'Diognostico doente',  'value': 'diagnostico_doente'},
                    {'label': 'Mamografia', 'value': 'mamografia'},
                    {'label': 'Dieta gordura', 'value': 'habitosAlimentar_dietaGordura'},
                     {'label': 'Sem gordura', 'value': 'habitosAlimentar_semGordura'}
                ],
                value='diagnostico_Saudavel',
                labelStyle={'display': 'inline-block'}
            ),
            html.Br(),
            html.Div(children='Diagnostigo de multiplo entrada em relação a Faixa Etária', style={
                'textAlign': 'center',
                'color': colors['text']
            }),
            dcc.Graph(
                id='fig_dd_situacao1'
            ),
            html.Hr(),
            html.Br(),
            html.Br(),
            html.P("Situação dignóstico:"),
            dcc.Dropdown(
                id='names',
                value='diagnostico_Saudavel',
                options=[
                    {'label': 'Diognostico saudavel', 'value':'diagnostico_Saudavel'},
                    {'label': 'Diognostico doente', 'value': 'diagnostico_doente'},
                    {'label':'Mamografia', 'value': 'mamografia'},
                    {'label':'Radioterapia', 'value': 'radioterapia'},
                    {'label':'Protese', 'value': 'Protese'}

                ],
                clearable=False
            ),

            html.Br(),
            html.P("Procedimentos realizados na mama:"),
            dcc.Dropdown(
                id='values',
                value='mamografia',
                options= [
                    {'label':'Mamografia', 'value': 'mamografia'},
                    {'label':'Radioterapia', 'value': 'radioterapia'},
                    {'label':'Protese', 'value': 'Protese'},
                    {'label':'Sem Gordura', 'value': 'habitosAlimentar_semGordura'},
                    {'label':'Dieta gordura', 'value': 'habitosAlimentar_dietaGordura'},
                    {'label':'Cirugia em  mama esquerda','value': 'cirugiaPlastico_MamaEsquerda'},
                    {'label':'Cirugia em  mama direita','value':'cirugiaPlastico_MamaDireita'},
                    {'label':'Cirugia em duas mama', 'value':'cirugiaPlastico_DuasMama'},
                    {'label':'Exercicio', 'value':'exercicio'},
                    {'label':'Fuma', 'value':'smoked'}

                ],
                clearable=False
            ),
            html.Br(),
            html.Div(children='Situação dignóstico', style={
                'textAlign': 'center',
                'color': colors['text']
            }),
            dcc.Graph(id="pie-chart"),
            html.Div(id="tab-content", className="p-4"),
        ]
        ),

]
)


@app.callback(
    Output(component_id='fig_diagnostico', component_property='figure'),
    [Input(component_id='dd_diagnostico', component_property='value')]
)
def graf_diagnostico(dd_scatter_situacao):
    fig = px.histogram(df, x='idade', y=dd_scatter_situacao)
    fig.update_layout(
        plot_bgcolor=colors2['background'],
        paper_bgcolor=colors2['background'],
        font_color=colors2['text']

    )
    return fig


#########
@app.callback(
    Output(component_id='fig_bar', component_property='figure'),
    [Input(component_id='dd_bar', component_property='value')]
)
def graf_diagnostico(dd_bar):
    fig = px.line(df_visita, x=df_visita.index, y=dd_bar, title='Data da visita')
    fig.update_layout(
        plot_bgcolor=colors2['background'],
        paper_bgcolor=colors2['background'],
        font_color=colors2['text']
    )
    return fig

#########



@app.callback(
    Output(component_id='fig_violino', component_property='figure'),
    [Input(component_id='dd_violino', component_property='value')]
)
def graf_diagnostico(dd_violino):
    fig = px.violin(df, y='idade', x=dd_violino, color=dd_violino, violinmode='overlay',box=True, hover_data=df.columns)
    fig.update_layout(
        plot_bgcolor=colors2['background'],
        paper_bgcolor=colors2['background'],
        font_color=colors2['text']

    )

    return fig


@app.callback(
    Output(component_id='fig_dd_situacao', component_property='figure'),
    [Input(component_id='dd_situacao', component_property='value')]
)
def graf_diagnostico(dd_situacao):
    fig = px.line(df_faixaEtaria, x=df_faixaEtaria.index, y=dd_situacao, title='Visual Lab')
    fig.update_layout(
        plot_bgcolor=colors2['background'],
        paper_bgcolor=colors2['background'],
        font_color=colors2['text']

    )
    return fig


#########
@app.callback(
    Output(component_id='fig_dd_situacao1', component_property='figure'),
    [Input(component_id='dd_situacao1', component_property='value')]
)
def graf_diagnostico(dd_situacao1):
    fig = px.histogram(df, x='idade', y=dd_situacao1, nbins=20, title='Visual Lab')
    fig.update_layout(
        plot_bgcolor=colors2['background'],
        paper_bgcolor=colors2['background'],
        font_color=colors2['text']
    )
    return fig


#####

@app.callback(
    Output("pie-chart", "figure"),
    [Input("names", "value"),
     Input("values", "value")]
)
def generate_chart(names, values):
    fig = px.pie(df, values=values, names=names, color_discrete_sequence=px.colors.sequential.RdBu, title='Visual Lab')
    fig.update_layout(
        plot_bgcolor=colors2['background'],
        paper_bgcolor=colors2['background'],
        font_color=colors2['text']
    )
    return fig

#########

if __name__ == '__main__':
    app.run_server(debug=False)
