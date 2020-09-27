from flask import Flask, Blueprint, redirect,request, render_template
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def index():
    members = member_repository.select_all()
    return render_template("/members/index.html",members=members)

# SHOW
@members_blueprint.route("/members/<id>")
def show_member(id):
    member = member_repository.select(id)
    activities = member_repository.activities(id)
    return render_template("/members/show.html",member=member,activities=activities)

# NEW
@members_blueprint.route("/members/new")
def new_member():
    return render_template("/members/new.html")

# CREATE
@members_blueprint.route("/members", methods=["POST"])
def create_member():
    name=request.form['name']
    member = Member(name)
    member_repository.save(member)
    return redirect("/members")

# EDIT
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("/members/edit.html",member=member)

# UPDATE
@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    name = request.form['name']
    active = request.form['active']
    member = Member(name,active,id)
    member_repository.update(member)
    return redirect("/members")

# DELETE
@members_blueprint.route("/members/<id>/delete",methods=['POST'])
def delete_artist(id):
    member_repository.delete(id)
    return redirect("/members")