FROM python:3.9


WORKDIR /app

COPY . /app

# COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y libgl1 --fix-missing
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY ./start /start
RUN chmod +x /start
EXPOSE 8000

# Add the command to start your app
CMD ["../start"]