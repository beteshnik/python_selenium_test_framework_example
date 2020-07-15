# ui-tests

Автоматизированные тесты UI

Python 3

Тестовый фреймворк unittest: https://docs.python.org/3/library/unittest.html

Запуск тестов с параметрами окружения: python $SUITE $GRID_URL $TARGET_URL $BROWSER

Параметры задаются в расписании: pipeline_schedules в git

GRID_URL - адрес Selenium-сервера.

TARGET_URL - адрес площадки для тестирования.

BROWSER - название браузера для тестов, варианты: CHROME, FIREFOX

SUITE - тестсьют, который включает в себя нужные тесты: например, testsuite_full_tests или testsuite_smoke_tests

Тест-сьюты расположены в корне директории, тесты размещены по папкам.

Результаты тестов записываются в файл results.xml
