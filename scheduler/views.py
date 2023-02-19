import pytz
from datetime import datetime
from flask import Blueprint,request,Response
from .models import EmailScheduler,EventParticipants,Events
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

@scheduler.route('/api/event',methods=['POST'])
def save_event():
    data = request.json
    new_event = Events(
        event_name=data['event_name']
    )
    db.session.add(new_event)
    db.session.commit()

    return Response("success add event", status=201, mimetype='application/json')

@scheduler.route('/api/participant', methods=['POST'])
def save_participant():
    data = request.json
    new_participant =  EventParticipants(
        event_id=data['event_id'],
        full_name=data['full_name'],
        email=data['email']
    )

    db.session.add(new_participant)
    db.session.commit()

    return Response("success add participant", status=201, mimetype='application/json')