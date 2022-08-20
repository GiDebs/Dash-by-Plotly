
from dash import Dash, dcc, Output, Input  # Input and Output are classes of Callback dash core component
import dash_bootstrap_components as dbc    

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytext = dcc.Markdown(children='') #It is an empty string
myinput = dbc.Input(value="# Hello World - write something here!")

# Customize your own Layout
app.layout = dbc.Container([mytext, myinput])

# Callback allows components to interact
#Callback is composed by a decorator (@app.callback()) and a function (def) always

@app.callback(
    Output(mytext, component_property='children'),
    Input(myinput, component_property='value')
)
def update_title(user_input):  # function arguments (user_input) come from the component_property of the Input defined in the decorator (->'value' -> whatever I write in the Input bar of the dashboard)
    return user_input  # returned objects (user_input) are assigned to the component_property of the Output defined in the decorator (->'children' -> which is an empty string filled by whatever I will write in the Input bar of the dashboard)
#I can write also different words instead of user_input and the instruction do not change

# Run app
if __name__=='__main__':
    app.run_server(port=8052)
