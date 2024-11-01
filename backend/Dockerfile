FROM python:3.9


WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install -y libgl1 --fix-missing
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

COPY ./start ./start
RUN chmod +x ./start

# Add the command to start your app
CMD ["./start"]