# GitHub-API

Тест для проверки работовспособности Github-API.
Я использовал python библиотеку requests.
Для скрытых данных используется библиотека dotenv.

### Как работает тест?
очень просто...

1. Создаётся репозиторий на Github
2. Проверка создался ли репозиторий
3. Удаления репозитория с Github
4. Проверка удалился ли репозиторий

вся информация выводится в консоль.

## Запуск теста

1. Копируем репозиторий
```
git clone git@github.com:Buzhak/GitHub-API.git
```

2. Переходим в папку
```
cd GitHub-API
```

3. Создаём виртуальное окружение
```
python3 -m venv env
```

4. Запускаем виртуальное окружение
win
```
env\Scripts\activate
```
linux\mac
```
source env/bin/activate
```

5. устанавливаем зависимости
```
pip install -r requirements.txt
```

6. Создаем файлик .env и заполняем его по примеру .env.example (это важный пункт, без этого ничего работать не будет)
```
git_token="ваш токен без кавычек"
user_name="имя пользователя без кавычек"
```
7. Запускаем тест:
```
python test_api.py
```

## Пример корректоного прохождения теста

```
Repository "my_test_repo" created successfully!
Repository "my_test_repo" exists.
Repository "my_test_repo" deleted successfully!
Repository "my_test_repo" does not exist.
```

## Технологии

* python
* requests
* python-dotenv
* GitHub-API
