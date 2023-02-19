from flask import Flask
from decouple import config
from celery import Celery
from flask_mail import Mail,Message

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

mail = Mail(app)

celery_app = Celery('tasks', broker=config('CELERY_BROKER_URL'), backend=config('CELERY_BACKEND_URL'))

@celery_app.task
def send_email(emails, subject, body):
    with app.app_context():
        msg = Message(recipients=emails, subject=subject, body=body)
        mail.send(msg)