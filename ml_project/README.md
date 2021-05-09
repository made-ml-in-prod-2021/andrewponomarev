Homework 1
==============================

Ml project for prediction Heart Disease

https://www.kaggle.com/ronitf/heart-disease-uci

Installation: 
~~~
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
~~~
Usage:
~~~
python src/train_pipeline.py configs/train_config.yaml
~~~

Test:
~~~
pytest tests/
~~~

Homework estimation
----------
9 points

Criterion
------------
№ | Description | Points
--- | --- | ---
-2 | ~~Назовите ветку homework1~~ | 1
-1 | ~~Положите код в папку ml_project~~ | -
0 | В описании к пулл реквесту описаны основные &quot;архитектурные&quot; и тактические решения, которые сделаны в вашей работе. | 2
1 | ~~Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками~~ | 2
2 | ~~Проект имеет модульную структуру(не все в одном файле =) )~~ | 2
3 | Использованы логгеры | 2
4 | Написаны тесты на отдельные модули и на прогон всего пайплайна | 3
5 | Для тестов генерируются синтетические данные, приближенные к реальным | 3
6 | Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing) | 3
7 | ~~Используются датаклассы для сущностей из конфига, а не голые dict~~ | 3
8 | Используйте кастомный трансформер(написанный своими руками) и протестируйте его | 3
9 | Обучите модель, запишите в readme как это предлагается | 3
10 | Напишите функцию predict, которая примет на вход артефакт/ы от обучения, тестовую выборку(без меток) и запишет предикт, напишите в readme как это сделать | 3
11 | Используется hydra  (https://hydra.cc/docs/intro/) | 3 (доп баллы)
12 | Настроен CI(прогон тестов, линтера) на основе github actions  | 3 балла (доп баллы)
13 | ~~Проведите самооценку, опишите, в какое колво баллов по вашему мнению стоит оценить вашу работу и почему~~ | 1 (доп баллы)


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- code to download or generate data
        │
        ├── features       <- code to turn raw data into features for modeling
        │
        └── models         <- code to train models and then use trained models to make



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
