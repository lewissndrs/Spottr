from flask import Flask, Blueprint, redirect,request, render_template
from models.activity import Activity
from models.trainer import Trainer
import repositories.activity_repository as activity_repository
import repositories.trainer_repository as trainer_repository

activities_blueprint = Blueprint("activities", __name__)

# INDEX
@activities_blueprint.route("/activities")
def activities():
    activities = activity_repository.select_all()
    return render_template("/activities/index.html",activities=activities)

# SHOW
@activities_blueprint.route("/activities/<id>")
def show_activity(id):
    activity = activity_repository.select(id)
    bookings = activity_repository.bookings(id)
    return render_template("/activities/show.html",activity=activity,bookings=bookings)

# NEW
@activities_blueprint.route("/activities/new")
def new_activity():
    trainers = trainer_repository.select_all()
    return render_template("/activities/new.html",trainers=trainers)

# CREATE
@activities_blueprint.route("/activities",methods=['POST'])
def create_activity():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    trainer = trainer_repository.select(request.form['trainer'])
    activity = Activity(name,date,time,trainer)
    activity_repository.save(activity)
    return redirect("/activities")