FROM python:3.5.7-slim-stretch 
WORKDIR /opt
RUN apt-get update && apt-get install -y chromium
COPY requirements.txt ./
COPY webdriver/chromedriver ./
RUN chmod +x ./chromedriver
COPY 500.py ./
RUN pip3 install -r requirements.txt
CMD ["python", "500.py"]
