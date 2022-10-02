FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY app.py /app

ENTRYPOINT ["python"]
CMD ["app.py"]
