#### 1. Запусти только один тест
pytest tests/test_handlers/test_start.py::test_start_handler -v

#### 2. Запусти все handler тесты параллельно
pytest tests/test_handlers/ -n 2 -v

#### 3. Сгенерируй HTML отчет о покрытии
pytest --cov=bot --cov-report=html

#### 4. 
pytest tests/test_handlers/test_start.py -v

#### Tree
```
any-project/
├── src/                    # Исходный код
├── tests/                  # ТЕСТЫ (единая структура!)
│   ├── unit/              # Модульные тесты
│   │   ├── services/      # Тесты сервисов
│   │   ├── handlers/      # Тесты обработчиков
│   │   └── utils/         # Тесты утилит
│   ├── integration/       # Интеграционные тесты
│   │   ├── api/          # Тесты API
│   │   └── database/     # Тесты БД
│   └── e2e/              # End-to-end тесты
├── ci-cd/                 # CI/CD конфиги
└── docker/               # Docker файлы
```


#### ==================Pipeline================
```
name: CI Pipeline

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Environment
        run: # Установка Python/Node.js/Go
      
      - name: Run Unit Tests
        run: # Запуск unit тестов
      
      - name: Run Integration Tests
        run: # Запуск integration тестов
        if: success()
      
      - name: Run E2E Tests
        run: # Запуск e2e тестов
       if: always()  #  Выполнится в любом случае
      
      - name: Generate Reports
        run: # Генерация отчетов


```
