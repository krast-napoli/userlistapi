# userlist
#### Проект предлагает бэкенд на Django Rest Framework с базой данных и API. Фронтенд на VueJS: при помощи модальных окон можно редактировать базу. В данном приложении был сделан выбор в пользу DRF, т.к. данный фреймворк позволяет создавать REST API встроенными средствами (serializers, работа с json и проч.)

### Запуск приложения
- pip install -r requirements.txt для установки зависимостей
+ python manage.py makemigrations - для инициализации модели (эта команда также необходима после обновления модели)
+ python manage.py migrate - для фиксации изменений в модели (эта команда также необходима после обновления модели)
+ python manage.py runserver - для запуска на localhost:8000. 
+ localhost:8000/users - при помощи VueJS
+ localhost:8000/api/users - через встроенный интерфейс Django Rest Framework
+ python manage.py dumpdata userlist.users --indent 2 > database.json - команда для дампа базы данных в файл формата json.