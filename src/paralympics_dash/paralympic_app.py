# Imports for Dash and Dash.html
from dash import Dash, html
import dash_bootstrap_components as dbc
external_stylesheets = [dbc.themes.BOOTSTRAP]
# Create an instance of the Dash app
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags, use_pages=True)

# Add an HTML layout to the Dash app
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Event Details", href=dash.page_registry['pages.events']['path'])),
        dbc.NavItem(dbc.NavLink("Charts", href=dash.page_registry['pages.charts']['path'])),
    ],
    brand="Paralympics Dashboard",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    # Nav bar
    navbar,
    # Area where the page content is displayed
    dash.page_container
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)