from flask import Flask
from database import database
from emailconfig import emailconfig

from scheduler.views import scheduler

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    database.init_app(app)
    with app.app_context():
        database.db.create_all()
        
    emailconfig.init_app(app)

    app.register_blueprint(scheduler)
    
    return app

if __name__ == "__main__":
    create_app().run()