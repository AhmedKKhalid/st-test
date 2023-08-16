import plotly.graph_objects as go

import pandas as pd
import streamlit as st


class Vis:
    df = pd.DataFrame()

    def __init__(self, df):
        self.df = df

    # load dataset
    def visualize1(df):
        # create figure

        x0 = df[df['Order_Priority'] == "High"]['Sales']
        y0 = df[df['Order_Priority'] == "High"]['Order_Quantity']
        x1 = df[df['Order_Priority'] == "Not Specified"]['Sales']
        y1 = df[df['Order_Priority'] == "Not Specified"]['Order_Quantity']
        x2 = df[df['Order_Priority'] == "Critical"]['Sales']
        y2 = df[df['Order_Priority'] == "Critical"]['Order_Quantity']
        # Create figure
        fig = go.Figure()

        # Add traces
        fig.add_trace(
            go.Scatter(
                x=x0,
                y=y0,
                mode="markers",
                marker=dict(color="DarkOrange")
            )
        )

        fig.add_trace(
            go.Scatter(
                x=x1,
                y=y1,
                mode="markers",
                marker=dict(color="Crimson"),

            )
        )

        fig.add_trace(
            go.Scatter(
                x=x2,
                y=y2,
                mode="markers",
                marker=dict(color="RebeccaPurple"),

            )
        )

        # Add buttons that add shapes
        cluster0 = [dict(type="circle",
                         xref="x", yref="y",
                         x0=min(x0), y0=min(y0),
                         x1=max(x0), y1=max(y0),
                         line=dict(color="DarkOrange"))]
        cluster1 = [dict(type="circle",
                         xref="x", yref="y",
                         x0=min(x1), y0=min(y1),
                         x1=max(x1), y1=max(y1),
                         line=dict(color="Crimson"))]
        cluster2 = [dict(type="circle",
                         xref="x", yref="y",
                         x0=min(x2), y0=min(y2),
                         x1=max(x2), y1=max(y2),
                         line=dict(color="RebeccaPurple"))]

        fig.update_layout(

            updatemenus=[
                dict(buttons=list([
                    dict(label="None",
                         method="relayout",
                         args=["shapes", []]),
                    dict(label="Cluster 0",
                         method="relayout",
                         args=["shapes", cluster0]),
                    dict(label="Cluster 1",
                         method="relayout",
                         args=["shapes", cluster1]),
                    dict(label="Cluster 2",
                         method="relayout",
                         args=["shapes", cluster2]),
                    dict(label="All",
                         method="relayout",
                         args=["shapes", cluster0 + cluster1 + cluster2])

                ]),

                )
            ]
        )

        # Update remaining layout properties
        fig.update_layout(
            title_text="Highlight Clusters",
            showlegend=False,
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False)
        )

        st.plotly_chart(fig)