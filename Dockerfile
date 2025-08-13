FROM python:3.13.6-slim-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /supports-bot

RUN pip install --upgrade pip wheel poetry

RUN poetry config virtualenvs.create false

COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install

COPY . .

RUN chmod +x prestart.sh

ENTRYPOINT ["./prestart.sh"]
CMD ["python3 ./main.py"]