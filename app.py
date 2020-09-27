from flask import Flask,render_template

import repositories.activity_repository as activity_repository

# from controllers.bookings_controller import bookings_blueprint
from controllers.members_controller import members_blueprint
from controllers.trainers_controller import trainers_blueprint
from controllers.activities_controller import activities_blueprint

app = Flask(__name__)


# app.register_blueprint(bookings_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(trainers_blueprint)
app.register_blueprint(activities_blueprint)

@app.route("/")
def login():
    activities = activity_repository.select_all()
    return render_template('index.html',activities=activities)

if __name__ == '__main__':
    app.run