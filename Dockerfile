FROM python:3.7

ADD . .

RUN pip install numpy

CMD ["python3", "-m", "unittest", "discover", "-s", "Tests"]