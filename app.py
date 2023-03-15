import dash
import dash_bootstrap_components as dbc
import dash_table
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import os
variable1 = os.environ['THIS_IS_A_KEY_1']
variable2 = os.environ[' NOOB KEY']

from dash import html
from helper_functions import get_player_image_url
from helper_functions import draw_plotly_court
from helper_functions import get_shot_plot
from helper_functions import get_shot_frequency_plot
from helper_functions import get_shot_pcts_plot
from helper_functions import get_pos_number
from helper_functions import get_season_stats

import pandas as pd
import numpy as np

app = dash.Dash(external_stylesheets=[dbc.themes.COSMO])

shot_df = pd.read_csv("./shot_tracker_data.csv")

players = np.unique(shot_df.player_name)
seasons = np.unique(shot_df.season)
shot_types = np.unique(shot_df.shot_types)


app.layout = html.Div([    
    dbc.Navbar([html.A(dbc.Row([dbc.Col(dbc.NavbarBrand("NBA Advanced Shooting Stats", className="ml-2"))], align="center"))],color="secondary", dark=True),
       
    html.Div([
        dbc.Row([
                # Column 1
                dbc.Col([
                    dbc.Container([
                        html.Img(id = 'player-image',
                                src = 'https://nba-players.herokuapp.com/players/curry/stephen', 
                                style={'height':'150px', 'width':'100%'}),
                        html.H5(id = 'position_number', style={'textAlign': 'center', 'fontWeight':'bold'}),
                        dcc.Dropdown(id="player-name", 
                                    value="Stephen Curry",  
                                    options=[{'label': x, 'value': x} for x in np.unique(players)],
                                    style={'width': '100%', 'display':'inline-block'}),
                        dcc.Dropdown(id="year", 
                                    value='2018-2019',
                                    options=[{'label': x, 'value': x} for x in np.unique(seasons)],
                                    style={'width': '100%', 'display':'inline-block', 'textAlign':'center'}),
                        dash_table.DataTable(id = 'season-stats', 
                                             columns=[{'id': c, 'name': c} for c in ['GP', 'MPG', 'FT%', '2P%', '3P%']],
                                             style_as_list_view=True,
                                             style_header={'textAlign': 'center', 'backgroundColor': '#F2F2F2', 'fontWeight': 'bold'},
                                             style_cell={'textAlign': 'center', 
                                                         'fontSize': 12, 
                                                         'backgroundColor': '#F2F2F2',
                                                         'height': 0, 'padding': 1},
                                             style_table ={'width': '100%',
                                                            'marginTop': '10%'}),            
                        ],style={'textAlign': 'center'})
                ], width = 3),
                # Column 2                    
                dbc.Col([
                    dcc.Graph(id='shot-chart', style = {'height': '250px'}),
                    dbc.Row([html.H6(variable1, style = {'fontWeight':'bold'}),
                    dbc.Col([dcc.RangeSlider(id='distance-slider', 
                               min=0, 
                               max=50, 
                               step=1, 
                               value=[0,50],    
                               marks={
                                0: {'label': '0'},
                                10: {'label': '10'},
                                20: {'label': '20'},
                                30: {'label': '30'},
                                40: {'label': '40'},
                                50: {'label': '50'}},
                               ),])], style = {'width':'100%', 'marginLeft': '5%', 'marginTop': '4%', 'color': 'black'}),
                    dbc.Row([html.H6(variable2, style = {'fontWeight':'bold'}),
                    dbc.Col([dcc.Dropdown(
                                id = 'shot_types',
                                options=[ {'label': x, 'value': x} for x in shot_types],
                                value=shot_types,
                                multi=True,
                                style = {}
                               ),])], style = {'width':'100%', 'marginLeft': '5%', 'marginTop': '4%', 'color': 'black'}),
                    ], width = 4),
            # Column 3
            dbc.Col([dcc.Graph(id='frequency-plot', style = {'height': '250px', 'width': '100%' }),
                     dcc.Graph(id='fieldgoal-pct-plot', style = {'height': '250px', 'width': '100%' })], width = 4)
        ], style = {'backgroundColor':'#F2F2F2', 'border':'2px black solid'}),
    ])
])

@app.callback([Output('shot-chart', 'figure'),
            Output('frequency-plot', 'figure'),
            Output('fieldgoal-pct-plot', 'figure'),
            Output('player-image', 'src'),
            Output('position_number', 'children'),
            Output('season-stats', 'data')],
            [Input('player-name', 'value'),
            Input('shot_types', 'value'),
            Input('distance-slider', 'value'),
            Input('frequency-plot', 'hoverData')])
def update_plot(player_name, shot_types, distance_range, hover_data):
    shot_fig = get_shot_plot(shot_df, player_name, shot_types, distance_range)
    url = get_player_image_url(player_name)
    freq_fig = get_shot_frequency_plot(shot_df, player_name)
    pct_fig = get_shot_pcts_plot(shot_df, player_name)
    pos_num = get_pos_number(shot_df, player_name)
    season_stats = get_season_stats(shot_df, player_name)

    return shot_fig, freq_fig, pct_fig, url, pos_num, season_stats

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8050)
