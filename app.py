import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input, Output

df = pd.read_csv('dataset_Visuallab.csv')
df_faixaEtaria = df.groupby(['idade']).sum()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server=app.server

colors = {
    'background': '#111111',
    'text': '#c83349'
}
colors1 = {
    'background': '#111111',
    'text':'#7FDBFF'
}

colors2 = {
    'background':'#96ceb4',
    'text':'#36486b'
}
colors3 = {
    'background':'#b2b2b2',
    'text':'#36486b'
}
colors4 = {
    'background':'#c0ded9',
    'text':'#36486b'
}

app.layout = html.Div(children=[
    html.H1(
        children='Visualização de Dados do Visual Lab',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'backgroundColor': colors['background']
        }
    ),
        dcc.Dropdown(
            id='dd_diagnostico',
            options=[
                {'label': 'Diognostico Saudavel', 'value': 'diagnostico_Saudavel'},
                {'label': 'Diognostico Doente', 'value': 'diagnostico_doente'},
            ],
            value='diagnostico_Saudavel',
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
        html.Br(),

        dcc.Dropdown(
            id='dd_situacao',
            options=[
                {'label': 'Diognostico Saudavel', 'value': 'diagnostico_Saudavel'},
                {'label': 'Diognostico Doente', 'value': 'diagnostico_doente'},
            ],
            value=['diagnostico_Saudavel'],
            multi=True,
            clearable=False,
            searchable=True
        ),
         html.Br(),
           html.Div(children='Diagnostigo de multiplo entrada em relação a Faixa Etária', style={
           'textAlign': 'center',
           'color': colors['text']
           }),
        dcc.Graph(
            id='fig_dd_situacao'
        ),
        html.Br(),

        dcc.Checklist(
            id='dd_situacao1',
            options=[
                {'label': 'Diognostico Saudavel', 'value': 'diagnostico_Saudavel'},
                {'label': 'Diognostico Doente', 'value': 'diagnostico_doente'},
            ],
            value=['diagnostico_Saudavel','diagnostico_doente'],
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

       html.P("Opção 01:"),
       dcc.Dropdown(
         id='names',
         value='diagnostico_Saudavel',
         options=[{'value': x, 'label': x}
                 for x in ['diagnostico_Saudavel', 'diagnostico_doente', 'idade', 'data_exame']],
         clearable=False
      ),
      html.P("Opção 02:"),
      dcc.Dropdown(
        id='values',
        value='cirugiaPlastico_DuasMama',
        options=[{'value': x, 'label': x}
                 for x in ['cirugiaPlastico_DuasMama','cirugiaPlastico_MamaDireita','cirugiaPlastico_MamaEsquerda', 'diagnostico_Saudavel']],
        clearable=False
     ),
     html.Br(),
     html.Div(children='Opção01 versos Opção02', style={
        'textAlign': 'center',
        'color': colors['text']
     }),
     dcc.Graph(id="pie-chart"),

    ],
)

@app.callback(
    Output(component_id='fig_diagnostico', component_property='figure'),
    [Input(component_id='dd_diagnostico', component_property='value')]
)
def graf_diagnostico(dd_scatter_situacao):
    fig = px.bar(df, x='idade', y=dd_scatter_situacao, color='idade', title='Visual Lab')
    fig.update_layout(
        plot_bgcolor=colors1['background'],
        paper_bgcolor=colors1['background'],
        font_color=colors1['text']

    )
    return fig
#########
@app.callback(
    Output(component_id='fig_dd_situacao', component_property='figure'),
    [Input(component_id='dd_situacao', component_property='value')]
)
def graf_diagnostico(dd_situacao):
    #fig = px.scatter(df, x='idade', y=dd_scatter_situacao, title='Visual Lab')
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
    #fig = px.scatter(df, x='idade', y=dd_scatter_situacao, title='Visual Lab')
    fig = px.scatter(df_faixaEtaria, x=df_faixaEtaria.index, y=dd_situacao1, title='Visual Lab')
    fig.update_layout(
        plot_bgcolor=colors3['background'],
        paper_bgcolor=colors3['background'],
        font_color=colors3['text']

    )
    return fig

####
@app.callback(
    Output("pie-chart", "figure"),
    [Input("names", "value"),
     Input("values", "value")])
def generate_chart(names, values):
    fig = px.pie(df, values=values, names=names, color_discrete_sequence=px.colors.sequential.RdBu, title='Visual Lab')
    fig.update_layout(
        plot_bgcolor=colors4['background'],
        paper_bgcolor=colors4['background'],
        font_color=colors4['text']

    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=False)
    