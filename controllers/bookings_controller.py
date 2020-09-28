from flask import Flask, Blueprint, redirect,request, render_template
from models.booking import Booking
from models.activity import Activity
from models.trainer import Trainer
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
# import repositories.trainer_repository as trainer_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

# NEW

@bookings_blueprint.route("/bookings/new")
def new_booking():
    activities = activity_repository.select_all()
    members = member_repository.select_all()
    return render_template("/bookings/new.html",activities=activities,members=members)

# CREATE

@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    activity_id = request.form['activity_id']
    activity = activity_repository.select(activity_id)
    member_id = request.form['member_id']
    member = member_repository.select(member_id)
    note = request.form['note']
    booking = Booking(member,activity,note)
    booking_repository.save(booking)
    return redirect("/")

# DELETE

@bookings_blueprint.route("/bookings/<id>/delete",methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/")