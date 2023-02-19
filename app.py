from flask import Flask
from database import database

from event_management.views import event_management

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    database.init_app(app)

    with app.app_context():
        database.db.create_all()

    app.register_blueprint(event_management)
    
    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=5000, debug=True)