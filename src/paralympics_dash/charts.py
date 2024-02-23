# This version is after the final activity in week 7
from dash import Dash, html
from dash import register_page, get_asset_url
import dash_bootstrap_components as dbc

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap
# components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Pass the stylesheet variable to the Dash app constructor
app =register_page(__name__, name='Charts', title='Charts')

# Variables that define the three rows of the layout
row_one = html.Div(
    dbc.Row([
        dbc.Col([html.H1("Paralympics Dashboard"), html.P(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida. Fusce "
            "efficitur posuere metus posuere malesuada. ")
                 ], width=12),
    ]),
)

row_two = html.Div(
    dbc.Row([
        dbc.Col(children=[dbc.Select(id="type-dropdown",
                                     # id uniquely identifies the element, will be needed later
                                     options=[
                                         {"label": "Events", "value": "events"},
                                         # The value is in the format of the column heading in the data
                                         {"label": "Sports", "value": "sports"},
                                         {"label": "Countries", "value": "countries"},
                                         {"label": "Athletes", "value": "participants"},
                                     ],
                                     value="events"  # The default selection
                                     ),
                          ], width=2),
        dbc.Col(children=[
            html.Img(src=get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=4),
        dbc.Col(children=[
            dbc.Checklist(
                options=[
                    {"label": "Summer", "value": "summer"},
                    {"label": "Winter", "value": "winter"},
                ],
                value=["summer"],  # Values is a list as you can select both winter and summer
                id="checklist-input",
            ),
        ], width=2),
        dbc.Col(children=[
            html.Img(src=get_asset_url('bar-chart-placeholder.png'), className="img-fluid"),
        ], width=4),
    ], align="start")
)



# Add an HTML layout to the Dash app.
# The layout is wrapped in a DBC Container()
layout = dbc.Container([
    row_one,
    row_two,

])

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)
    # Runs on port 8050 by default. If you have a port conflict, add the parameter port=   e.g. port=8051