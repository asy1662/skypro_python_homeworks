# skypro_python_homeworks
# Selenium Calculator Testing

Этот проект автоматизирует тестирование онлайн-калькулятора, используя Selenium WebDriver и Allure для отчетности.
 Тест для проверки работы калькулятора.

    Шаги:
    -----
    1. Установить задержку в 45 секунд.
    2. Нажать кнопки для вычисления: 7 + 8 =.
    3. Получить и проверить результат.
## Требования

- Python 3.6+
- Selenium
- Allure-pytest
- WebDriver Manager

## Установка зависимостей

Убедитесь, что у вас установлен Python, а затем установите необходимые зависимости с помощью pip:

bash
pip install -r requirements.txt


## Запуск тестов

### Pytest

Для запуска тестов выполните команду:

bash
pytest


### Генерация Allure-отчетов

1. Запустите тесты и сохраните результаты в папку `allure-results`:

    ```bash
    pytest --alluredir=allure-results
    ```

2. Сформируйте отчет из результатов:

    ```bash
    allure generate allure-results -o allure-report
    ```

3. Для просмотра отчета в браузере:

    ```bash
    allure open allure-report
    ```
# Selenium Form Testing with Allure Report

Этот проект автоматизирует тестирование формы с различными типами данных, используя Selenium WebDriver и Allure для отчетности.
 Тест для проверки успешной отправки формы с правильными данными.

    Шаги:
    -----
    1. Открыть страницу формы.
    2. Заполнить форму данными.
    3. Отправить форму.
    4. Проверить, что все поля формы подсвечены зелёным.
    5. Проверить подсветку поля Zip code.
## Требования

- Python 3.6+
- Selenium
- Allure-pytest
- WebDriver Manager

## Установка зависимостей

Убедитесь, что у вас установлен Python, а затем установите необходимые зависимости с помощью pip:

bash
pip install -r requirements.txt


## Запуск тестов

### Pytest

Для запуска тестов выполните команду:

bash
pytest


### Генерация Allure-отчетов

1. Запустите тесты и сохраните результаты в папку `allure-results`:

    ```bash
    pytest --alluredir=allure-results
    ```

2. Сформируйте отчет из результатов:

    ```bash
    allure generate allure-results -o allure-report
    ```

3. Для просмотра отчета в браузере:

    ```bash
    allure open allure-report
    ```

### Установка Allure Commandline Tool

1. Скачайте и установите Allure Commandline Tool, следуя инструкциям [здесь](https://docs.qameta.io/allure/#_get_started).

2. Добавьте путь к Allure в переменную окружения PATH.


  Тест для проверки успешной покупки продуктов и правильности итоговой суммы.

    Шаги:
    -----
    1. Открыть сайт Saucedemo.
    2. Войти под стандартным пользователем.
    3. Добавить выбранные продукты в корзину.
    4. Перейти к оформлению заказа.
    5. Заполнить информацию о заказе.
    6. Проверить общую сумму заказа
    # Selenium Product Purchase Testing with Allure Report

Этот проект автоматизирует тестирование покупки продуктов на сайте Saucedemo, используя Selenium WebDriver и Allure для отчетности.

## Требования

- Python 3.6+
- Selenium
- Allure-pytest
- WebDriver Manager

## Установка зависимостей

Убедитесь, что у вас установлен Python, а затем установите необходимые зависимости с помощью pip:

bash
pip install -r requirements.txt


## Запуск тестов

### Pytest

Для запуска тестов выполните команду:

bash
pytest


### Генерация Allure-отчетов

1. Запустите тесты и сохраните результаты в папку `allure-results`:

    ```bash
    pytest --alluredir=allure-results
    ```

2. Сформируйте отчет из результатов:

    ```bash
    allure generate allure-results -o allure-report
    ```

3. Для просмотра отчета в браузере:

    ```bash
    allure open allure-report
    ```

### Установка Allure Commandline Tool

1. Скачайте и установите Allure Commandline Tool, следуя инструкциям [здесь](https://docs.qameta.io/allure/#_get_started).

2. Добавьте путь к Allure в переменную окружения PATH.
