FROM python:3.12-slim-bookworm
COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/
RUN pip install --no-cache-dir --upgrade pip
COPY pyproject.toml ./pyproject.toml
RUN uv sync
COPY . .
CMD ["python3", "./main.py"]