[![main](https://github.com/swankyalex/rocshers_test_assignment/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/swankyalex/rocshers_test_assignment/actions)
[![Lines of code](https://img.shields.io/tokei/lines/github/swankyalex/rocshers_test_assignment)](https://github.com/swankyalex/rocshers_test_assignment/tree/master)

# Тестовое задание

Вакансия: Python developer в команду https://www.linkedin.com/in/rocshers/

#### Заданию было уделено 3 часа. Покрытие кода тестами 100%

## Стек

Python, poetry, pytest, coverage.

## Использование
1. Склонируйте данный репозиторий на свою локальную машину
2. Убедитесь, что у вас установлен пакет [Poetry](https://python-poetry.org/docs/)
3. Установите зависимости командой:
```sh
poetry install
```
4. Для запуска скрипта используйте команду:
```sh
poetry run main
```
либо
```sh
poetry run python src/runner.py 
```
5. Откроется поле для ввода ссылок, вводите ссылки по одной через Enter. По окончанию 
ввода всех ссылок нажмите Enter. При вводе неверной ссылки появится уведомление.
6. Результатом работы программы будет вывод вида: 

![Results](https://i.ibb.co/prybNn0/Screenshot-from-2022-11-15-21-29-15.png)

7. Для запуска тестов используйте:
```sh
pytest
```
8. Для проверки покрытия кода тестами:
```sh
pytest --cov
```
![coverage](https://i.ibb.co/4JFqc87/Screenshot-from-2022-11-15-21-35-04.png)
