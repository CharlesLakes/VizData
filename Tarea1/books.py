import pandas as pd
import plotly.express as px
import numpy as np
import random

file_name = "books.csv"
df = pd.read_csv(file_name)
counts_rew = {}
for i in range(len(df)):
    autores = df['authors'][i].split("/")
    for autor in autores:
        if autor not in counts_rew:
            counts_rew[autor] = 0
        counts_rew[autor] += df['average_rating'][i]
top = []
for autor in counts_rew:
    top.append([counts_rew[autor],autor])
top.sort(reverse=True)
df1 = pd.DataFrame(top[:17])
df1 = df1.rename(columns={0:'average_rating',1:'authors'})
# name   selling_price
fig = px.funnel(df1,x = 'average_rating', y = 'authors', text = 'authors',title = 'Top 15 average rating')

fig.show()