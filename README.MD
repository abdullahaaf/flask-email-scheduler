
# Simple flask microservice to manage an Event

A simple microservice built using flask, a framework from python. The case study of this project is to be able to manage an event, such as:
- Create new events
- Adding participants to certain events
- Schedule email delivery to all participants of a particular event.
This project is also equipped with a simple GUI to be able to perform some of the tasks above.

The celery task queue is used to manage email delivery scheduling, based on a certain timestamp.

## Project structure description
- ```celery_queue``` the directory where all the celery tasks script are located
- ```database``` the directory to initialize database with SQLAlchemy
- ```event_management``` the directory where script for main feature located, including script for database models and script for http routing
- ```frontend``` directory where frontend/gui script are located, this directory is not mandatory to be exist.
- ```tests``` directory where all testcase script located.
- ```app.py``` entry point for microservice.
- ```docker-compose.yml``` docker script for configuring container
- ```Dockerfile``` Dockerfile script for run command on container
- ```.env``` Environment variable, content of this file can refer to ```env.example```
- ``` requirements.txt``` contains python package that need to installed to run this project


## Environment Variables

To run this project, you will need to configure the following environment variables to your .env file

`SQLALCHEMY_DATABASE_URI` SQLAlchemy connection string. Format: *driver://<username>:<password>@<hostname or ip_address>/<db_name>*. **Change hostname with container name if run with docker**.

`MAIL_SERVER` smptp mail to send email.

`MAIL_PORT` smptp port

`MAIL_DEFAULT_SENDER` default email address sender

`MAIL_ISERNAME` username to login to smtp server

`MAIL_PASSWORD` password to login in smtp server

`MAIL_USE_TLS` set default to True

`CELERY_BROKER_URL` Broker connection string for celery. Format: *<driver>://<hostname or ip_address>:<port>/0*. **Change hostname with container name if run with docker**.

`CELERY_BACKEND_URL` Result backend connection string for celery. Format: *<driver>://<hostname or ip_address>:<port>/0*. **Change hostname with container name if run with docker**.

`API_BASE_URL` Api base url that consumed by frontend.

`DB_NAME` database name for container db

`DB_USER` database username for container db

`DB_PASS` database password for container db

`TIMEZONE` set timezone for celery worker scheduling email delivery. Ex: Asia/Singapore


## Run Locally
make sure below port already opened :
- 5000 ```backend port```
- 5500 ```frontend port```
- 6379 ```redis port <not mandatory>```

Environment variable already configured

### Run with docker

```bash
  git clone https://github.com/abdullahaaf/flask-email-scheduler.git
  cd flask-email-scheduler
  docker compose up
```
or
```bash
  git clone https://github.com/abdullahaaf/flask-email-scheduler.git
  cd flask-email-scheduler
  docker compose up -d
```
### Run without docker
- make sure python virtualenvironment already created and activated
- make sure redis already installed
```bash
  git clone https://github.com/abdullahaaf/flask-email-scheduler.git
  cd flask-email-scheduler
  pip install -r requirements.txt
  export PYTHONPATH=<directory of project>
```
Run each of this command on separate terminal on project root folder
```bash
python app.py
python frontend/app.py
celery -A celery_queue.tasks.celery_app worker --loglevel=info
```

## GUI Routing
- `{base_url}/event` route to add event page
- `{base_url}/participant` route to add participant page
- `{base_url}/schedule` route to add email delivery schedule page


## API Reference
[API documentation on postman](https://documenter.getpostman.com/view/2479819/2s93CHvFep)
### Event
#### Get all event

```http
  GET /api/events
```
This will return all events

#### Add event

```http
  POST /api/event
```

| Parameter | Type     | Description                       | Location |
| :-------- | :------- | :-------------------------------- | :---------
| `event_name`      | `string` | **Required**. Name of the event | Raw body

This will store new event into database

### Participant
#### Add Participant

```http
  POST /api/participant
```

| Parameter | Type     | Description                       | Location |
| :-------- | :------- | :-------------------------------- | :---------
| `event_id`      | `integer` | **Required**. ID of event | Raw body
| `full_name`      | `string` | **Required**. Participant full_name | Raw body
| `email`      | `string` | **Required**. Participant email | Raw body

This will store new participant on particular event

### Schedule
#### Schedule email delivery

```http
  POST /api/save_emails
```

| Parameter | Type     | Description                       | Location |
| :-------- | :------- | :-------------------------------- | :---------
| `event_id`      | `integer` | **Required**. ID of event | Raw body
| `email_subject`      | `string` | **Required**. Subject of email | Raw body
| `email_content`      | `string` | **Required**. Email body message | Raw body
| `timestamp`      | `string` | **Required**. Timestamp to schedule email delivery. **Format : YYYY-MM-DD HH:MM**  | Raw body

This will schedule email delivery on all emails of particular event and timestamp

## Running Tests
Run this project locally
To run tests, run the following command

```bash
  py.test tests/<script>.py
```
ex :
```bash
py.test tests/test_email.py
```
## Authors
Abdullah Amin Firdaus