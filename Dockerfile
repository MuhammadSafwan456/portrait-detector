FROM python:3.9


WORKDIR /app


COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y libgl1
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY ./app /app
COPY ./start /start
RUN chmod +x /start
