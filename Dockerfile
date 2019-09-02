FROM python:3.5-stretch
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD 
