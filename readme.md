# Книга рецептов

Веб-приложение на базе Django, где можно хранить рецепты.

## Развёртывание проекта с использованием Docker

### Настройка проекта

Создайте копию файла `.env.dist` с названием `.env` файл в корне репозитория:

```bash
cp .env.dist .env
```

Откройте файл `.env` и внесите необходимые изменения в переменные окружения.

### Сборка и запуск контейнеров

Выполните следующую команду в корне репозитория:

```bash
docker-compose up --build
```

При первом запуске процесс сборки может занять несколько минут.

### Остановка контейнеров

Откройте новое окно терминала и выполните команду

```bash
docker-compose stop
```

### Инициализация приложения

Перед началом использования приложения не забудьте выполнить инициализацию приложения.

Запустите терминал внутри контейнера следующей командой:

```bash
docker-compose exec app bash
```

#### Применение миграций
Создает схему базы данных
```bash
python manage.py migrate
```

#### Создание суперпользователя
Необходимо для доступа к панели администратора
```bash
python manage.py createsuperuser
```

#### Добавление фикстур
```bash
python manage.py loaddata ingredients measures receipts receipt_ingredients
```

Развёрнутое приложение будет доступно в браузере по адресу http://127.0.0.1:8000
