###### Личный блог и портфолио

**Сервис позволяет:**
- регистрироваться, восстанавливать пароль по почте;
- создавать страницу для размещения портфолио;
- создавать и редактировать свои записи в блоге c помощью WYSIWYG-редактора;
- комментировать записи;
- присваивать записи к определенным категориям и тегам;
- редактировать меню в админке через drag&drop.

**Cтек**:
- Python 3
- Django 2
   
**Установка**:

1. Клонируем репозиторий на локальную машину:
`$ git clone https://github.com/Techinek/kuskovan.git`

2. Создаем виртуальное окружение(Linux):
`$ python -m venv venv`

3. Устанавливаем зависимости:
`$ pip install -r reqs.txt`

4. Создаем и применяем миграции:
`$ python manage.py makemigrations и $ python manage.py migrate`

5. Запускаем локальный django-сервер:
`$ python manage.py runserver`