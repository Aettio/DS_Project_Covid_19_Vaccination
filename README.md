# Data science | Project: "COVID-19 World Vaccination Progress"

## Гайд по проекту

Перед началом:
- "README.txt" - Содержит сам проект с визуализациями. Предпологаеться что читатель и будет смотреть его как основной файл на входе.
- "DataFrames" - Содержит в себе все дата сеты.
- "Images" - Содержит в себе все картинки "README.txt".
- "Code_Visual" - Содержит в себе код для всего визуала (Графиков и 3D).

p.s. Во всём коде дополнительно были сделаны заметки для удобства чтения и понимания.

## Разделы

- Введение
- Задача
- Exploratory Data Analysis (Анализ данных, более подробно можно просмотреть в Code_Visuals.py)
  - Чистка данных 
  - Визуализация
- Итог
- Источники

## Введение

Данные по Covid-19 собираются ежедневно в репозитории «Our World» на GitHub, объединяются и выгружаются.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Vaccine.jpg)

## Задача

Отследить вакцинацию COVID-19 в мире и ответить на следующие вопросы:

- Какие вакцины используются в разных странах?
- В какой стране программа вакцинации более развита?
- Где вакцинируются больше людей в день? (В процентах от населения)

## EDA (Exploratory Data Analysis)

# Самые используемые вакцины

Тут как и следовало ожидать мы имеем самые эффективные вакцины в топе листа, но всё же стоило проверить так как была вероятность того что самые эффективные вакцины могли быть менее распространёнными изза меньшего объема производства.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/top_vaccines.png)

# Какие вакцины используются в разных странах?

А вот и собтвенно ответ на первый вопрос.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Vaccines_by_country.jpeg)

# Топ 20 стран по общему количеству вакцинаций

На этом графике мы видим топ 20 стран по общему количеству вакцинаций но не стоит забывать о том что это не процент, так что данная статисика может быть обманчева. Осталось только привести эти данные к соотношению к населению этих стран и выделить наш процент.

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Vaccinations_by_country.png)

# Где вакцинируются больше людей в день? Но в процентах от всего населения?

![alt text](https://github.com/Aettio/DS_Project_Covid_19_Vaccination/blob/main/Images/Total_vaccinations_per_hundred.png)

## Итог

## Источники

- Датасет : https://www.kaggle.com/gpreda/covid-world-vaccination-progress
