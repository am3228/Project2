FROM python:3.7

ADD . .

Run pip install --upgrade pip

CMD [ "python", "-m", "unitest", "discover", "-s", "Tests"]