import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.pie(df, values = "cases", names =  "country")

fig.show()