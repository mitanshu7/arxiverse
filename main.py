import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# Initialize the app
app = Dash()
server = app.server

parque_file = 'https://media.githubusercontent.com/media/mitanshu7/PaperMatch_Analysis/refs/heads/main/bluuebunny/arxiv_abstract_embedding_mxbai_large_v1_milvus_binary/umap/hamming/all_years.parquet'
df = pd.read_parquet(parque_file)

# Sample a subset of the data for visualization
df_sampled = df.sample(100000)

# Plot the 3D scatter plot using Plotly Express
fig = px.scatter_3d(df_sampled, x='x', y='y', z='z', hover_name='title', hover_data='year', color='categories',  opacity=0.5)#, size='year', text='id', symbol='categories')

# Customize the marker size and layout
fig.update_traces(marker_size = 3)
fig.update_layout(
    title='UMAP Projection of Arxiv Abstracts',
    scene=dict(
        xaxis_title='UMAP X',
        yaxis_title='UMAP Y',
        zaxis_title='UMAP Z'
    ),
    legend_title='Categories',
    height=800,
    scene_camera=dict(
        eye=dict(x=1.25, y=0, z=0.125)
    )
)

# App layout
app.layout = [
    html.Div(children='Interactive 3D Scatter Plot of Arxiv Abstracts.'),
    html.Div(children='This visualization shows the UMAP projection of Arxiv abstracts, colored by categories.'),
    html.Div(children='Hover over points to see titles and years. You can zoom, pan, and rotate the plot for better exploration.'),
    dcc.Graph(figure=fig),
    html.Div(children='Note: The data is sampled for performance reasons.'),
]

# Run the app
if __name__ == '__main__':
    app.run(port=8050)