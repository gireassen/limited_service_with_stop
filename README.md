# Limited Request Webhook Service


[![CI/CD Pipeline](https://github.com/gireassen/limited_service_with_stop/actions/workflows/docker-build-test.yml/badge.svg)](https://github.com/gireassen/limited_service_with_stop/actions/workflows/docker-build-test.yml)
[![Last Commit](https://img.shields.io/github/last-commit/gireassen/limited_service_with_stop)](https://github.com/gireassen/limited_service_with_stop/commits/main)
[![Docker Pulls](https://img.shields.io/docker/pulls/gias123/limited_service)](https://hub.docker.com/r/gias123/limited_service)
[![Docker Image Size](https://img.shields.io/docker/image-size/gias123/limited_service/latest)](https://hub.docker.com/r/gias123/limited_service)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)](https://www.python.org/)
[![GitHub License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/gireassen/limited_service_with_stop/blob/main/LICENSE)

Микросервис на Python, который автоматически останавливается после обработки 10 POST-запросов. Разработан для тестирования сценариев обработки отказов (failure scenarios) и проверки механизмов перезапуска сервисов в отказоустойчивых кластерах.

## Особенности

- Ограничение на 10 успешных запросов (HTTP 200);
- Автоматическое завершение работы с кодом 503 после лимита;
- Ультра-легковесный Docker образ 🐳(~19) на Alpine Linux;
- Встроенные тесты для проверки лимита запросов;

## Использование

### Запуск локально

```bash
# запуск сервиса
python3 server.py

# запуск теста
python3 test_service.py

# или curl post по 10 раз
curl -X POST http://localhost:8008
```

