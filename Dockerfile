FROM python:3.11-slim-bullseye

WORKDIR /blog_app 

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /blog_app/

CMD ["python", "manage.py","runserver","0.0.0.0:8000"]






