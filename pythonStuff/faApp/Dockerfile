FROM --platform=linux/arm64 python:3.12.2-slim-bullseye

WORKDIR /code

COPY ./requirements.txt ./models.py /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

#CMD ["uvicorn", "app.main:app", "--app-dir", "/code/app", "--host", "0.0.0.0", "--port", "80"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
