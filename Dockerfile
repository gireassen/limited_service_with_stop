# Этап сборки
FROM python:3.9-alpine AS builder

WORKDIR /app

COPY requirements.txt .

# Устанавливаем зависимости для сборки и устанавливаем пакеты
RUN apk add --no-cache --virtual .build-deps gcc musl-dev && \
    pip install --user --no-cache-dir --no-compile -r requirements.txt && \
    apk del .build-deps && \
    rm -rf /root/.cache/pip

# Финальный этап
FROM python:3.9-alpine

WORKDIR /app

# Копируем только необходимые файлы
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/requirements.txt .
COPY server.py .

# Оптимизации:
# 1. Объединяем команды RUN для уменьшения слоев
# 2. Удаляем кэш pip и ненужные файлы
# 3. Используем более легковесные альтернативы где возможно
RUN find /usr/local -type d -name '__pycache__' -exec rm -rf {} + && \
    find /usr/local -type f -name '*.pyc' -delete && \
    rm -rf /var/cache/apk/* /tmp/*

# Убедимся, что скрипты в PATH
ENV PATH=/root/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Используем более легковесный способ запуска
CMD ["python", "-OO", "server.py"]

# Использование Alpine вместо slim (образ в 5x меньше)
# Многоэтапная сборка уменьшает итоговый размер
# Удаление ненужных зависимостей после установки
# Копируются только необходимые файлы