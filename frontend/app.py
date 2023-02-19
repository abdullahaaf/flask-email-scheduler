from flask import Flask, render_template, url_for, redirect
from decouple import config

app = Flask(__name__)

@app.route('/event', methods=['GET'])
def add_event():
    return render_template('add_event.html',api_base_url=config('API_BASE_URL'))

@app.route('/participant', methods=['GET'])
def add_participant():
    return render_template('add_participant.html',api_base_url=config('API_BASE_URL'))

@app.route('/schedule', methods=['GET'])
def schedule_email():
    return render_template('schedule_email.html',api_base_url=config('API_BASE_URL'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5500)