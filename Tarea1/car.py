import pandas as pd
import plotly.express as px
import numpy as np
import random

file_name = "car_dataset.csv"
df = pd.read_csv(file_name)
for i in range(len(df)):
    marca = df['name'][i].split()[0]
    last = df['name'][i]
    df['name'] = df['name'].replace(last,marca)
# name   selling_price
fig = px.violin(df,y = 'selling_price', color = 'name',title = 'Distribution of cars by company')

fig.show()