from flask import Blueprint,request
from flask_mail import Message
from emailconfig.emailconfig import mail

from .models import EmailScheduler, EventParticipants
from database.database import db

scheduler = Blueprint('scheduler', __name__)

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

    send_email(data['event_id'], data['email_content'], data['email_subject'])
    return {"data" : data}