FROM python:3.8.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /app/
CMD python manage.py migrate && python manage.py loaddata /app/customers/fixtures/fixtures.json && python manage.py runserver 0.0.0.0:8000