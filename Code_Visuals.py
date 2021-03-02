import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
%matplotlib inline

sns.set(rc={"figure.figsize":(10,8)})
sns.set(style="darkgrid", context="talk")
plt.rc('font', size=12)

df = pd.read_csv("country_vaccinations.csv")

df.head()

# Самые используемые вакцины

df = df.fillna(0)
pd.DataFrame(df['vaccines'].value_counts())


# Какие вакцины используются в разных странах?

fig = px.choropleth(df, locations='iso_code',color=df['vaccines'], hover_name="country", # column to add to hover information
                    color_continuous_scale="Viridis", width=1700,height=500)
fig.show()


# В какой стране программа вакцинации более развита?

top_20 = df.groupby(['country'])["total_vaccinations"].sum().reset_index()
top_20 = top_20.nlargest(20, ['total_vaccinations']).reset_index()

del top_20['index']
top20_countries = top_20['country']
top_20

graph_top20 = sns.barplot(data=top_20, x="total_vaccinations", y="country", palette="viridis")
graph_top20.set(xlabel='Country',ylabel='Total vaccinations')


# Где вакцинируются больше людей в день? Но в процентах от всего населения?

top_country = df.groupby(['country'])["total_vaccinations_per_hundred"].sum().reset_index()
top_country = top_country.nlargest(20, ['total_vaccinations_per_hundred']).reset_index()
del top_country['index']
top_country

graph_twph = sns.barplot(x=top_country['total_vaccinations_per_hundred'], y=top_country['country'], palette="viridis")
graph_twph.set(xlabel='Country',ylabel='Total vaccinations per hundred')

