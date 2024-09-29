# Контрольные вопросы
## 1 практическая работа:
### В каком файле обрабатываются HTTP-запросы?
* В файле `views.py` обрабатываются HTTP-запросы.

### Какой файл отвечает за маршрутизацию?
* За маршрутизацию отвечает файл `urls.py`

### Какая команда используется для создания проекта на Django?
* Команда: `django-admin startproject имя_проекта`

### Какая команда используется для создания приложения в проекте на Django?
* Команда: `python manage.py startapp имя_приложения`


## 2 Практическая работа
### В каком файле подключаем приложение в Django?
* Приложение подключается в файле `settings.py` в разделе `INSTALLED_APPS`.

### Для чего нужна функция render?
* Функция `render` используется для рендеринга HTML-шаблонов с передачей данных контекста.

### В какой папке сохраняем HTML-шаблоны?
* Шаблоны сохраняются в папке `templates` внутри приложения или в основной директории проекта.


## 3 Практическая работа
### Для чего нужен файл `models.py`?
* Там мы создаём структуру данных, как таблицы в базе данных.

### Какая команда создаёт скрипт для миграции?
* `python manage.py makemigrations`

### Где хранятся скрипты для миграции?
* В папке `migrations` внутри приложения.

### Какая команда выполняет миграции?
* ``python manage.py migrate``
