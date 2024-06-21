#Данные регионов России
Проект по визуализации статистических данных регионов РФ, а также муниципальных районов РФ.
<!--Описание-->
## О чем проект?
Проект о визуализации статистических данных, таких как: миграционный прирост муниципальных районов РФ, динамика фонда заработной платы регионов РФ, доход и сумма социальных выплат муниципальных районов РФ, состав дохода региона РФ от муниципальных районов РФ, численность населения муниципальных районов РФ, доход региона РФ, а также тепловая карта миграции регионов РФ. Все эти данные будут полезны исследователям, политическим деятелям, а также некоторые данные будут полезны людям, которые планируют переехать в другой регион. Проект представлен в виде дашборда с разными диаграммами, которые отображают информацию по определенным показателям.
## Ссылка на датасет
https://github.com/ZhigalovArtem/Dashboard/blob/main/merged_data.xlsx

<!--Установка-->
1. Клонирование репозитория 

```git clone https://github.com/ZhigalovArtem/Dashboard.git```

2. Создание виртуального окружения

```python3 -m venv venv```

3. Активация виртуального окружения

```source venv/bin/activate```

4. Установка библиотек

```pip3 install dash```

```pip install dash-bootstrap-components```

```pip install pandas```

```pip install plotly-express```


5. Запуск дашборда для его использования

```python3 app.py --help```

<!--Зависимости-->
## Зависимости
Эта программа зависит от интепретатора Python версии 3.7 или выше, PIP 23.2.1 или выше.