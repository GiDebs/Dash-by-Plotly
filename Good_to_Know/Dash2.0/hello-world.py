# If you prefer to run the code online instead of on your computer click:
# https://github.com/Coding-with-Adam/Dash-by-Plotly#execute-code-in-browser

from dash import Dash, dcc               # dcc = dash core components
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]) #BOOTSTRAP is the theme of the dashboard created:colors, fonts, ecc... can chose many different themes


mytext = dcc.Markdown(children="# Hello World - let's build web apps in Python!") # The # in the string indicata a Header

# Customize your own Layout
app.layout = dbc.Container([mytext])

# Run app
if __name__=='__main__':
    app.run_server(port=8051)
