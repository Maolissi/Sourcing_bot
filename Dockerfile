FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY sourcer_bot ./sourcer_bot

RUN pip install --no-cache-dir .

CMD ["python", "-m", "sourcer_bot"]
