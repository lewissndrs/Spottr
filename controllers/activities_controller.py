from flask import Flask, Blueprint, redirect,request, render_template
from models.activity import Activity
from models.trainer import Trainer
import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("activities", __name__)

# INDEX
@activities_blueprint.route("/activities")
def activities():
    activities = activity_repository.select_all()
    return render_template("activities/index.html",activities=activities)

# SHOW
@activities_blueprint.route("/activities/<id>")
def show_activity(id):
    activity = activity_repository.select(id)
    bookings = activity_repository.bookings(id)
    return render_template("activities/show.html",activity=activity,bookings=bookings)