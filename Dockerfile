FROM python:slim-buster
WORKDIR /opt
RUN apt-get update && apt-get install -y chromium
COPY . ./
RUN pip3 install -r requirements.txt
CMD ["python", "500.py"]
