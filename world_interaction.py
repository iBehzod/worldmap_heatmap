# -*- coding: utf-8 -*-
"""world_interaction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19DHwD7Gk9VFtfCzkGVrSbzV7MkCQkxkE
"""

!pip install plotly

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'colab'

from google.colab import drive
drive.mount('/content/drive')

df_raw = pd.read_csv("/content/API_SP.POP.TOTL_DS2_en_csv_v2_87.csv", skiprows=4)


df = df_raw[["Country Name", "Country Code", "2023"]].copy()
df.columns = ["country", "iso_alpha3", "population"]
df.dropna(subset=["population"], inplace=True)

# Filter out non-countries or aggregator codes (like "WLD" for world)
df = df[df["iso_alpha3"].str.len() == 3]

df.head()

df["population_str"] = df["population"].apply(lambda x: f"{x:,}")
df["pop_log"] = np.log10(df["population"])

fig = px.choropleth(
    data_frame=df,
    locations="iso_alpha3",
    color="pop_log",
    hover_name="country",
    hover_data={"population": ":,"},             # <<— format with commas
    color_continuous_scale="Plasma",
    range_color=(5, 9),  # from 10^5 (100k) to 10^9 (1B)
    title="World Population (Log-Scale) with Custom Color Range"
)

fig.update_layout(
    margin={"r":0, "t":50, "l":0, "b":0},
    geo=dict(showframe=False, showcoastlines=False)
)

fig.show()