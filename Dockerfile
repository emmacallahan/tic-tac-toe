FROM python:3.7-stretch
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD sleep infinity
