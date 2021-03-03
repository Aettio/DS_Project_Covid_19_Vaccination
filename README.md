# Data science | Project: "COVID-19 World Vaccination Progress"

## Гайд по проекту

Перед началом:
- "README.txt" - Содержит сам проект с визуализациями. Предпологаеться что читатель и будет смотреть его как основной файл на входе.
- "DataFrames" - Содержит в себе все дата сеты.
- "Images" - Содержит в себе все картинки "README.txt".
- "Code_Visual" - Содержит в себе код для всего визуала.

p.s. Во всём коде дополнительно были сделаны заметки для удобства чтения и понимания.

## Разделы

- Введение
- Задача
- Exploratory Data Analysis (Анализ данных, более подробно можно просмотреть в Code_Visuals.py)
  - Самые используемые вакцины
  - Какие вакцины используются в разных странах
  - В какой стране программа вакцинации более развита
  - Где вакцинируются больше людей в день
- Итог
- Источники

## Введение

Данные по Covid-19 собираются ежедневно в репозитории «Our World» на GitHub, объединяются и выгружаются.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Vaccine.jpg)

## Задача

Отследить вакцинацию COVID-19 в мире и ответить на следующие вопросы:

- Какие вакцины используются в разных странах?
- В какой стране программа вакцинации более развита?
- Где вакцинируются больше людей в день?

## EDA (Exploratory Data Analysis)

Так как данные были довольно хорошо сделаны хватило небольшой чистки, а точнее убирания NA значений. Так что можно было сразу приступать к самому анализу.

# Самые используемые вакцины

Тут как и следовало ожидать мы имеем самые эффективные вакцины в топе листа Pfizer/BioNTech и Moderna, но всё же стоило проверить, так как была вероятность того что самые эффективные вакцины могли быть менее распространёнными из-за меньшего объема производства.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Top_vaccines.png)

# Какие вакцины используются в разных странах

А вот и собственно ответ на первый вопрос. Также судя по этим данным можно отметить что Pfizer/BioNTech не во всех странах является основной и видимо массовость в основном создаётся из-за таких стран как Китай и Индия. Так как в Китае вообще используют только её.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Vaccines_bycountry.jpeg)
(Картинка в очень высоком качестве, так что её можно увеличить чтобы рассмотреть подробнее)

# В какой стране программа вакцинации более развита

На этом графике мы видим топ 20 стран по общему количеству вакцинаций, но не стоит забывать о том что это не процент, так что данная статистика может быть обманчива. Осталось только привести эти данные к соотношению к населению этих стран и выделить наш процент.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Vaccinations_by_country.png)

# Где вакцинируются больше людей в день

А вот и количество вакцинированных на сотню населения, что в принципе интерпретируется как процент. Тут можно сразу же отметить явного лидера Израиль и ОАЭ.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Total_vaccinations_per_hundred.jpeg)
(Картинка в очень высоком качестве, так что её можно увеличить чтобы рассмотреть подробнее)

## Итог

Количество вакцинаций стремительно растёт вверх. Особенно в США, но из-за большого количества населения по сравнению со странами лидерами, США всё еще не входит в топ по проценту вакцинированных. Так же мы отметили что Pfizer/BioNTech является на данный момент самой распространённой вакциной в мире.

p.s. С момента завершения мною данного проекта данные поменялись, соответственно лидеры могли измениться.

## Источники

- Датасет : https://www.kaggle.com/gpreda/covid-world-vaccination-progress
- plotly.express.choropleth документация : https://plotly.github.io/plotly.py-docs/generated/plotly.express.choropleth.html
- Seaborn документация : https://seaborn.pydata.org/introduction.html
