import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(layout='wide')

df = pd.read_csv('India-dataset.csv')
list_of_state = list(df['State'].unique())
list_of_state.insert(0,'Overall Analysis')

st.sidebar.title('India population analysis')

selected_state = st.sidebar.selectbox("select state",list_of_state)
primary = st.sidebar.selectbox('select primary parameter',sorted(list(df.columns[5:])))
secondary = st.sidebar.selectbox('select secondary parameter',sorted(list(df.columns[5:])))

plot = st.sidebar.button('plot')

if plot:
    if selected_state == 'Overall Analysis':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary,
                                color_discrete_sequence=["fuchsia"], width=1200, height=600,zoom=4, size_max=35)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        st.plotly_chart(fig,use_container_width=True)
    else:
        select_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(select_df, lat="Latitude", lon="Longitude", size=primary, color=secondary,
                                color_discrete_sequence=["fuchsia"], width=1200, height=600, zoom=6, size_max=35)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        st.plotly_chart(fig, use_container_width=True)
