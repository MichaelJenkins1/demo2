import numpy as np
from PIL import Image
import requests
from io import BytesIO
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
from scipy.interpolate import UnivariateSpline

def draw_plotly_court(fig, fig_width=400, margins=10):

    def ellipse_arc(x_center=0.0, y_center=0.0, a=10.5, b=10.5, start_angle=0.0, end_angle=2 * np.pi, N=200, closed=False):
        t = np.linspace(start_angle, end_angle, N)
        x = x_center + a * np.cos(t)
        y = y_center + b * np.sin(t)
        path = f'M {x[0]}, {y[0]}'
        for k in range(1, len(t)):
            path += f'L{x[k]}, {y[k]}'
        if closed:
            path += ' Z'
        return path

    # Set axes ranges
    fig.update_xaxes(range=[-250 - margins, 250 + margins])
    fig.update_yaxes(range=[-52.5 - margins, 417.5 + margins])

    threept_break_y = 89.47765084
    three_line_col = "#777777"
    main_line_col = "#777777"

    fig.update_layout(
        # Line Horizontal
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white",
        yaxis=dict(
            scaleanchor="x",
            scaleratio=1,
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False,
            fixedrange=True,
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False,
            fixedrange=True,
        ),
        shapes=[
            dict(
                type="rect", x0=-250, y0=-52.5, x1=250, y1=417.5,
                line=dict(color=main_line_col, width=1),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(
                type="rect", x0=-80, y0=-52.5, x1=80, y1=137.5,
                line=dict(color=main_line_col, width=1),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(
                type="rect", x0=-60, y0=-52.5, x1=60, y1=137.5,
                line=dict(color=main_line_col, width=1),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(
                type="circle", x0=-60, y0=77.5, x1=60, y1=197.5, xref="x", yref="y",
                line=dict(color=main_line_col, width=1),
                # fillcolor='#dddddd',
                layer='below'
            ),
            dict(
                type="line", x0=-60, y0=137.5, x1=60, y1=137.5,
                line=dict(color=main_line_col, width=1),
                layer='below'
            ),

            dict(
                type="rect", x0=-2, y0=-7.25, x1=2, y1=-12.5,
                line=dict(color="#ec7607", width=1),
                fillcolor='#ec7607',
            ),
            dict(
                type="circle", x0=-7.5, y0=-7.5, x1=7.5, y1=7.5, xref="x", yref="y",
                line=dict(color="#ec7607", width=1),
            ),
            dict(
                type="line", x0=-30, y0=-12.5, x1=30, y1=-12.5,
                line=dict(color="#ec7607", width=1),
            ),

            dict(type="path",
                 path=ellipse_arc(a=40, b=40, start_angle=0, end_angle=np.pi),
                 line=dict(color=main_line_col, width=1), layer='below'),
            dict(type="path",
                 path=ellipse_arc(a=237.5, b=237.5, start_angle=0.386283101, end_angle=np.pi - 0.386283101),
                 line=dict(color=main_line_col, width=1), layer='below'),
            dict(
                type="line", x0=-220, y0=-52.5, x1=-220, y1=threept_break_y,
                line=dict(color=three_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=-220, y0=-52.5, x1=-220, y1=threept_break_y,
                line=dict(color=three_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=220, y0=-52.5, x1=220, y1=threept_break_y,
                line=dict(color=three_line_col, width=1), layer='below'
            ),

            dict(
                type="line", x0=-250, y0=227.5, x1=-220, y1=227.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=250, y0=227.5, x1=220, y1=227.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=17.5, x1=-80, y1=17.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=27.5, x1=-80, y1=27.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=57.5, x1=-80, y1=57.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=-90, y0=87.5, x1=-80, y1=87.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=90, y0=17.5, x1=80, y1=17.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=90, y0=27.5, x1=80, y1=27.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=90, y0=57.5, x1=80, y1=57.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),
            dict(
                type="line", x0=90, y0=87.5, x1=80, y1=87.5,
                line=dict(color=main_line_col, width=1), layer='below'
            ),

            dict(type="path",
                 path=ellipse_arc(y_center=417.5, a=60, b=60, start_angle=-0, end_angle=-np.pi),
                 line=dict(color=main_line_col, width=1), layer='below'),
        ]
    )
    return True


def get_shot_plot(shot_df, player_name, shot_types, distance_range):
    plot_data = shot_df[(shot_df.player_name==player_name) & 
                        (shot_df.shot_types.isin(shot_types)) &
                        (shot_df.shot_distance >= distance_range[0])&
                        (shot_df.shot_distance <= distance_range[1])]
    xlocs = list((plot_data['y']-300)/1.2)
    ylocs = list(plot_data['converted_x']/1.2-52.5)
    hover_text = [str(a) + ' ' + 'Q' + str(b) + ' ' + c + ' ' + str(d)  for a,b,c,d in zip(plot_data['player_name'], plot_data['period'], plot_data['clock'], plot_data['shot_types'])]
    symbols = ['circle' if x == True else 'x' for x in plot_data.results]
    colors = ['#A369EC' if x == True else 'black' for x in plot_data.results]

    fig = go.Figure()
    draw_plotly_court(fig)

    fig.add_trace(go.Scatter(
        x=xlocs, y=ylocs, mode='markers',
        marker=dict(
            sizemode='area', sizemin=3.5,
            line=dict(width=1), symbol=symbols, color = colors
        ), hovertext = hover_text, hoverinfo = 'text'
    ))
    return fig

def get_player_image_url(player_name):
    first_last = player_name.split(' ')
    first_name = first_last[0].lower()
    last_name = first_last[1].lower()
    url = 'https://nba-players.herokuapp.com/players/{0}/{1}'.format(last_name, first_name)
    return url

def get_shot_frequency_plot(shot_df, player_name):
    x = shot_df[shot_df.player_name == player_name]['shot_distance'].tolist()
    hist_data = [x]
    group_labels = ['Shot Distance'] # name of the dataset

    fig = ff.create_distplot(hist_data, group_labels, show_hist=False, colors = ['#A369EC'], show_rug=False)
    fig.update_layout(showlegend=False, 
                  title={'text': "<b>Shot Frequency by Distance</b>",'y':.95, 'x':0.55},
                  titlefont=dict(size =14, color='black', family='Arial, sans-serif'),
                  xaxis_title="<b>Shot Distance</b>", 
                  #yaxis_title="Frequency",
                  font=dict(size=11, color= 'black'),
                  xaxis=dict(linecolor = 'black', title_standoff = 1),
                  yaxis=dict(linecolor = 'black', title_standoff = 1),
                  paper_bgcolor='rgba(0,0,0,0)',
                  margin=dict(l=10, r=10, t=30, b=20),
                  )
    return fig


def get_pos_number(shot_df, player_name):
    return str(shot_df[shot_df.player_name == player_name]['POS'].iloc[0]) + ' #' + str(shot_df[shot_df.player_name == player_name]['jersey_number'].iloc[0])


def get_shot_pcts_plot(shot_df, player_name):
    pct_by_dist = shot_df[shot_df.player_name == player_name].copy()
    pct_by_dist['results'] = pct_by_dist['results'].astype(int)
    pct_by_dist['shot_distance'] = [2 * round(float(x/2)) for x in pct_by_dist.shot_distance]
    pct_by_dist = pct_by_dist.groupby(by ='shot_distance')['results'].mean()
    
    x = pct_by_dist.index
    y = np.array(pct_by_dist)
    s = UnivariateSpline(x, y, s=9)
    xs = np.linspace(0, max(x), 100)
    ys = s(xs)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=xs, y=ys,
                    mode='lines',
                    name='lines', line=dict(color='black')))
    fig.update_layout(showlegend=False, 
                  title={'text': "<b>FG% by Distance</b>",'y':.95, 'x':0.55},
                  titlefont=dict(size =14, color='black', family='Arial, sans-serif'),
                  xaxis_title="<b>Shot Distance</b>", 
                  #yaxis_title="Frequency",
                  font=dict(size=11, color= 'black'),
                  xaxis=dict(linecolor = 'black', title_standoff = 1),
                  yaxis=dict(linecolor = 'black', title_standoff = 1),
                  paper_bgcolor='rgba(0,0,0,0)',
                  margin=dict(l=10, r=10, t=30, b=20),
                  )
    return fig

def get_season_stats(shot_df, player_name):

    season_stats = shot_df[shot_df.player_name == player_name].copy()
    season_stats = season_stats[['GP', 'MPG', 'FT%', '2P%', '3P%']]
    season_stats = season_stats.head(1)
    season_stats = season_stats.round(2)
    return season_stats.to_dict('records')