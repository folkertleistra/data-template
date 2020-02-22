# Index.py is the main file of the dashboard and the file that should be run. It takes care of displaying the header
# and navigation for the dashboard.
# When running the dashboard index.py should be called, also when using a flask server.

import dash
from app import dash_app, app
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input #import State if needed , State
from layouts import example # add your layouts here

server = dash_app.server


dash_app.layout = \
        html.Div(children=[
            html.Div(className="mainContainer",
                     children=[
                         html.Div(className='dashboard-header',
                                  children=[
                                      html.Div(className='title-box',
                                               children=[
                                                   html.Div(id="title", children=[
                                                   html.P('Data Template')
                                                            ]
                                                   ),
                                                   html.Div(id="subtitle", children=[
                                                   html.P('by Storm Digital')
                                                            ]
                                                   )
                                               ]),
                                      html.Div(className="SD-logo",
                                               children=[
                                                   html.Img(src="assets/logo2.png"),
                                               ])
                                  ]),
                         html.Div(id="dashboard-tabs",
                                  children=[
                                      dcc.Link("Example", href="/example"),
                                      # add more links below
                                  ]),
                         html.Div(className="main-content",
                                  children=[
                                      dcc.Location(id="url", refresh=False),
                                      html.Div(id="tab_content"),
                                  ]
                                  )
                     ]
                     )
        ]
        )

# The main callback that takes care of the dashboard navigation
@dash_app.callback(
    [Output("tab_content", "children"),
     Output("dashboard-tabs", "children")],
    [Input("url", "pathname")],
)
def display_page(pathname):
    """ Callback in charge of the navigation of the dashboard
        Two empty lists will be returned when the page is not found, to prevent a multi-output error
     """
    tabs = [
        dcc.Link("Example", href="/example"),
    ]

    if pathname:
        if pathname == '/example':
            tabs[0] = dcc.Link(
                dcc.Markdown("**&#9632 Example**"),
                href="/example",
            )
            return example.layout, tabs
        # Add more path names below when adding more tabs and make sure to import the layouts
        else:
            return [], []
    else:
        return [], []