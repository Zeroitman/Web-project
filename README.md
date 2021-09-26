#### Инструкция по поднятию проекта локально

1) Установите python на ваш пк [Python](https://www.python.org/downloads/)
2) Установите пакет менеджер [pip](https://pip.pypa.io/en/stable/)

Ссылка на репозиторий проекта [Gitlab](https://github.com/Zeroitman/Web-project)

Установка:
- Склонировать проект из репозитория
- Зайдите в папку проекта и создайте виртуальное окружение c помощью команды 
```bash
sudo pip install virtualenv
```
- В папке проекта пропишите в консоли команду для установки виртуального окружения:
```bash
virtualenv -p python3.7 venv
```

- После установки можно будет активировать виртуальное окружение:
```bash
source venv/bin/activate
```

- Установите все зависимости проекта:
```bash
pip install -r requirements.txt
```

- Проведите миграции:
```bash
./manage.py migrate
```

- Загрузите дамп содержащий 25 отделов:
```bash
 ./manage.py loaddata fixtures/dump_departments.json
```

- Загрузите дамп содержащий 50 тыс. сотрудников (придётся подождать минуты 2) или выполните функцию generate_employes, 
которая сгенирирует 50 тыс. сотрудников:
```bash
 ./manage.py loaddata fixtures/dump_employes.json
```

- Создайте суперпользователя(необязательно):
```bash
./manage.py createsuperuser
```

- Запустите проект:

```bash
./manage.py runserver
```
- Для останоки проекта:
```bash
CTRL + C
```
