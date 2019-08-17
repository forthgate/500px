FROM python:3.5.7-slim-stretch 
WORKDIR /opt
RUN apt-get update && apt-get install -y chromium
COPY . ./
RUN chmod +x ./webdriver/chromedriver
RUN pip3 install -r requirements.txt
CMD ["python", "500.py"]
