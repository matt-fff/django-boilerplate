FROM python:3.8-alpine

EXPOSE 8000

RUN apk add --no-cache gcc musl-dev
RUN python3 -m pip install pip --upgrade

ADD ./manage.py manage.py
ADD ./.pylintrc .pylintrc
ADD ./.pycodestyle .pycodestyle
ADD ./pyproject.toml pyproject.toml
ADD ./requirements.txt requirements.txt
ADD ./app /app
RUN python3 -m pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]