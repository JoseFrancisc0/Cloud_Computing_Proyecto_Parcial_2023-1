FROM python:3-slim
WORKDIR /project/cars
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "./cars.py"]
