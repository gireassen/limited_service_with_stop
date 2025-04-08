FROM python:3.9-alpine as builder

WORKDIR /app

COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --user --no-cache-dir -r requirements.txt \
    && apk del .build-deps

FROM python:3.9-alpine

WORKDIR /app

# Копируем только необходимые файлы
COPY --from=builder /root/.local /root/.local
COPY limited_service_with_stop.py .

# Убедимся, что скрипты в PATH
ENV PATH=/root/.local/bin:$PATH

CMD ["python", "limited_service_with_stop.py"]

# Использование Alpine вместо slim (образ в 5x меньше)
# Многоэтапная сборка уменьшает итоговый размер
# Удаление ненужных зависимостей после установки
# Копируются только необходимые файлы