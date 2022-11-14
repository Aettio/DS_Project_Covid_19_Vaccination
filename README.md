# Data science | Project : "COVID-19 World Vaccination Progress"

## Project guide

Before the beginning:
- "README.txt" - Contains the project itself with visualizations. It is assumed that the reader will view it as the main input file.
- "DataFrames" - Contains all data sets.
- "Images" - Contains all the pictures "README.txt".
- "Code_Visual" - Contains the code for the entire visual.

p.s. Additional notes have been made throughout the code for ease of reading and understanding.

## Sections

- Introduction
- A task
- Exploratory Data Analysis (Data analysis, more details can be viewed in Code_Visuals.py)
  - Most used vaccines
  - What vaccines are used in different countries
  Which country has the most developed vaccination program?
  - Where more people are vaccinated per day
- Total
- Sources

## Introduction

Covid-19 data is collected daily in the Our World GitHub repository, merged and uploaded.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Vaccine.jpg)

## A task

Track COVID-19 vaccinations around the world and answer the following questions:

- What vaccines are used in different countries?
- In which country is the vaccination program more developed?
- Where are more people vaccinated per day?

## EDA (Exploratory Data Analysis)

Since the data was quite well done, a little cleaning was enough, or rather, removing NA values. So it was possible to start the analysis itself right away.

# Most used vaccines

Here, as you might expect, we have the most effective vaccines at the top of the Pfizer/BioNTech and Moderna list, but it was still worth checking, as there was a possibility that the most effective vaccines could be less common due to lower production volume.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Top_vaccines.png)

# What vaccines are used in different countries

And here is the answer to the first question. Also, judging by these data, it can be noted that Pfizer / BioNTech is not the main one in all countries and apparently the mass character is mainly created due to countries such as China and India. Since in China they generally use only it.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Vaccines_bycountry.jpeg)
(The picture is in very high quality, so you can enlarge it for a closer look)

# Which country has the most developed vaccination program

On this graph we see the top 20 countries by total number of vaccinations, but don't forget that this is not a percentage, so this statistic can be misleading. It remains only to bring these data to the ratio of the population of these countries and highlight our percentage.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Vaccinations_by_country.png)

# Where more people are vaccinated per day

And here is the number of people vaccinated per hundred of the population, which, in principle, is interpreted as a percentage. Here you can immediately note the clear leader of Israel and the United Arab Emirates.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Total_vaccinations_per_hundred.jpeg)
(The picture is in very high quality, so you can enlarge it for a closer look)

## Total

The number of vaccinations is skyrocketing. Especially in the USA, but due to the large population compared to the leading countries, the USA is still not in the top in terms of the percentage of vaccinated. We also noted that Pfizer/BioNTech is currently the most widely used vaccine in the world.

p.s. Since the completion of this project by me, the data has changed, respectively, the leaders could change.

## Sources

- Dataset : https://www.kaggle.com/gpreda/covid-world-vaccination-progress
- plotly.express.choropleth documentation : https://plotly.github.io/plotly.py-docs/generated/plotly.express.choropleth.html
- Seaborn documentation : https://seaborn.pydata.org/introduction.html
