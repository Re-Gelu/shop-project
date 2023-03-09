FROM python:3.10.5-alpine

# set work directory
ENV BACKEND_APP_HOME=/usr/src/app/backend
WORKDIR $BACKEND_APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./entrypoint.sh .

COPY . $BACKEND_APP_HOME

# install dependencies and update pip
RUN apk update 
RUN apk add postgresql-dev gcc python3-dev musl-dev libpq
RUN rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# staticfiles folder
RUN mkdir $BACKEND_APP_HOME/staticfiles

# entrypoint
RUN sed -i 's/\r$//g'  $BACKEND_APP_HOME/entrypoint.sh
RUN chmod +x  $BACKEND_APP_HOME/entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000

RUN chmod +x $BACKEND_APP_HOME/start.sh
CMD ["./start.sh"]