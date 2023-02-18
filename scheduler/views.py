import pytz
from datetime import datetime
from flask import Blueprint,request
from flask_mail import Message
from emailconfig.emailconfig import mail
from celery import Celery
from decouple import config

from .models import EmailScheduler, EventParticipants
from database.database import db

celery_app = Celery('views', broker=config('CELERY_BROKER_URL'), backend=config('CELERY_BACKEND_URL'))
scheduler = Blueprint('scheduler', __name__)


@celery_app.task
def send_email(event_id, body, subject):
    emails = EventParticipants.query.filter(EventParticipants.event_id == event_id).all()
    list_email = []
    for email in emails:
        list_email.append(email.email)

    msg = Message(recipients=list_email, body=body, subject=subject)
    mail.send(msg)

@scheduler.route("/save_emails", methods=["POST"])
def save_emails():
    data = request.json

    email_scheduler = EmailScheduler(
        event_id = data['event_id'],
        email_subject = data['email_subject'],
        email_content = data['email_content'],
        timestamp = data['timestamp']
    )
    db.session.add(email_scheduler)
    db.session.commit()

    send_time_str = data['timestamp']
    send_time = datetime.strptime(send_time_str, "%Y-%m-%d %H:%M:%S")
    local_tz = pytz.timezone('Asia/Jakarta')
    local_dt = local_tz.localize(send_time)
    utc_dt = local_dt.astimezone(pytz.utc)
    send_email.apply_async(args=[data['event_id'], data['email_content'], data['email_subject']], eta=utc_dt)

    return {"data" : data}