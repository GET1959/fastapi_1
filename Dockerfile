FROM python:3.12
COPY . .
COPY pyproject.toml .
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]