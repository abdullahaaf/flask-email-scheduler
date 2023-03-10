import pytz
from datetime import datetime
from flask import Blueprint,request,jsonify
from flask_cors import cross_origin
from .models import EmailScheduler,EventParticipants,Events
from database.database import db
from celery_queue.tasks import send_email
from decouple import config
from unidecode import unidecode

event_management = Blueprint('event_management', __name__)

@event_management.route("/api/save_emails", methods=["POST"])
@cross_origin()
def save_emails():
    data = request.get_json()

    if data.get('event_id') == None or data.get('email_subject') == None or data.get('email_content') == None or data.get('timestamp') == None:
        return {
            'message' : 'Error, one of field is empty. Check your data'
        }, 400

    email_scheduler = EmailScheduler(
        event_id = data['event_id'],
        email_subject = data['email_subject'],
        email_content = data['email_content'],
        timestamp = data['timestamp']
    )
    db.session.add(email_scheduler)
    db.session.commit()

    send_time_str = data['timestamp']
    timezone = config('TIMEZONE')
    send_time = datetime.strptime(send_time_str, "%Y-%m-%d %H:%M")
    local_tz = pytz.timezone(timezone)
    local_dt = local_tz.localize(send_time)
    utc_dt = local_dt.astimezone(pytz.utc)

    emails = []
    participants = EventParticipants.query.filter(EventParticipants.event_id == data['event_id'])
    for email in participants:
        emails.append(email.email)

    send_email.apply_async(args=[emails, data['email_subject'], data['email_content'],], eta=utc_dt)

    return {
        'message' : 'success schedule email',
        'data' : data
    }, 201

@event_management.route('/api/event', methods=['POST'])
@cross_origin()
def save_event():
    data = request.json

    if data.get('event_name') == None:
        return {
            'message' : 'Error, event name is required'
        }, 400

    new_event = Events(
        event_name=data['event_name']
    )
    db.session.add(new_event)
    db.session.commit()

    return {
        'message' : 'success add event',
        'data' : data
    }, 201

@event_management.route('/api/events', methods=['GET'])
@cross_origin()
def list_event():
    events = Events.query.all()
    response = []
    for event in events:
        event_data = {}
        event_data['event_id'] = event.id
        event_data['event_name'] = event.event_name
        response.append(event_data)

    return {
        'message' : 'success get events',
        'data' : response
    }, 200

@event_management.route('/api/participant', methods=['POST'])
@cross_origin()
def save_participant():
    data = request.json

    if data.get('event_id') == None or data.get('full_name') == None or data.get('email') == None:
        return {
            'message' : 'Error, one of field is empty. Check your data'
        }, 400

    new_participant =  EventParticipants(
        event_id=data['event_id'],
        full_name=unidecode(data['full_name']), #handling full_name that have unicode character
        email=unidecode(data['email']) #handling email that have unicode character
    )

    db.session.add(new_participant)
    db.session.commit()

    return {
        'message' : 'success add participant',
        'data' : data
    }, 201