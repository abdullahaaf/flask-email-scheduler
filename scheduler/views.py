import pytz
from datetime import datetime
from flask import Blueprint,request
from .models import EmailScheduler,EventParticipants
from database.database import db
from tasks import send_email

scheduler = Blueprint('scheduler', __name__)

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

    emails = []
    participants = EventParticipants.query.filter(EventParticipants.event_id == data['event_id'])
    for email in participants:
        emails.append(email.email)

    send_email.apply_async(args=[emails, data['email_subject'], data['email_content'],], eta=utc_dt)
    # send_email.apply_async(eta=utc_dt)

    return {"data" : data}