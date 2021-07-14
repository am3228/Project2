FROM python:3.7

ADD . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD [ "python", "-m", "unittest", "discover", "-s", "Tests"]