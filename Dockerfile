FROM python:3.13-slim-bookworm
WORKDIR /supports_bot
RUN pip install --upgrade pip wheel poetry
RUN poetry config virtualenvs.create false
COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml
RUN poetry install --no-interaction
COPY . .
RUN chmod +x ./prestart.sh
ENTRYPOINT ["./prestart.sh"]
CMD ["python3", "./main.py"]