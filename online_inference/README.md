Homework 2
==============================

Homework estimation
----------
0 points

Criterion
------------
№ | Description | Points | Estimation
--- | --- | --- | ---
0 | ~~ветку назовите homework2, положите код в папку online_inference~~ | 0 | 0 |
1 | ~~Оберните inference вашей модели в rest сервис(вы можете использовать как FastAPI, так и flask, другие желательно не использовать, дабы не плодить излишнего разнообразия для проверяющих), должен быть endpoint /predict~~ | 3 | 3 
2 | Напишите тест для /predict (https://fastapi.tiangolo.com/tutorial/testing/, https://flask.palletsprojects.com/en/1.1.x/testing/) | 3 | 0
3 | Напишите скрипт, который будет делать запросы к вашему сервису | 2
4 | Сделайте валидацию входных данных (например, порядок колонок не совпадает с трейном, типы не те и пр, в рамках вашей фантазии)  (вы можете сохранить вместе с моделью доп информацию, о структуре входных данных, если это нужно) https://fastapi.tiangolo.com/tutorial/handling-errors/ -- возращайте 400, в случае, если валидация не пройдена  | 3 | 0
5 | Напишите dockerfile, соберите на его основе образ и запустите локально контейнер(docker build, docker run), внутри контейнера должен запускать сервис, написанный в предущем пункте, закоммитьте его, напишите в readme корректную команду сборки | 4 | 0
6 | Оптимизируйте размер docker image (3 доп балла) (опишите в readme.md что вы предприняли для сокращения размера и каких результатов удалось добиться)  -- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/ | 3 | 0
7 | опубликуйте образ в https://hub.docker.com/, используя docker push (вам потребуется зарегистрироваться) | 2 | 0
8 | напишите в readme корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель. Убедитесь, что вы можете протыкать его скриптом из | 1 | 0
9 | проведите самооценку | 1 | 0
10 | создайте пулл-реквест и поставьте label --hw2 | 0 | 0
+ | Total | 22 | 3