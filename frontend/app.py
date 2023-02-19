from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/event', methods=['GET'])
def add_event():
    return render_template('add_event.html')

@app.route('/participant', methods=['GET'])
def add_participant():
    return render_template('add_participant.html')

@app.route('/schedule', methods=['GET'])
def schedule_email():
    return render_template('schedule_email.html')

if __name__ == '__main__':
    app.run(debug=True, port=1000)