# Книга рецептов

Веб-приложение на базе Django, где можно хранить рецепты.

## Развёртывание проекта с использованием Docker

### Настройка проекта

Создайте копию файла `.env.dist` с названием `.env` файл в корне репозитория:

```bash
cp .env.dist .env
```

Откройте файл `.env` и внесите нужные вам изменения в переменные окружения.

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

### Первичная настройка проекта

Не забудьте выполнить первичную настройку приложения перед использованием. Перед выполнением команд ниже убедитесь, что вы зашли в терминал внутри контейнера. Для этого выполните команду:

```bash
docker-compose exec app bash
```

#### Применение миграций
Создает схему базы данных
```bash
python manage.py migrate
```

#### Создание суперпользователя
Необходима для доступа к админке
```bash
python manage.py createsuperuser
```

#### Добавление фикстур
```bash
python manage.py loaddata ingredients measures receipts receipt_ingredients
```

Развёрнутое приложение будет доступно в браузере по адресу http://127.0.0.1:8000
