from flask import Flask, Blueprint, redirect,request, render_template
from models.trainer import Trainer
import repositories.trainer_repository as trainer_repository

trainers_blueprint = Blueprint("trainers", __name__)

# INDEX
@trainers_blueprint.route("/trainers")
def trainers():
    trainers = trainer_repository.select_all()
    return render_template("trainers/index.html",trainers=trainers)

# NEW
@trainers_blueprint.route("/trainers/new")
def new_trainer():
    return render_template("trainers/new.html")

# CREATE
@trainers_blueprint.route("/trainers", methods=["POST"])
def create_trainer():
    name = request.form['name']
    new_trainer = Trainer(name)
    trainer_repository.save(new_trainer)
    return redirect("/trainers")

# EDIT
@trainers_blueprint.route("/trainers/<id>/edit")
def edit_trainer(id):
    trainer = trainer_repository.select(id)
    return render_template("/trainers/edit.html",trainer=trainer)

# UPDATE
@trainers_blueprint.route("/trainers/<id>",methods=["POST"])
def update_trainer(id):
    name = request.form['name']
    active = request.form['active']
    trainer = Trainer(name,active,id)
    trainer_repository.update(trainer)
    return redirect("/trainers")

# DELETE
@trainers_blueprint.route("/trainers/<id>/delete",methods=["POST"])
def delete_trainer(id):
    trainer_repository.delete(id)
    return redirect("/trainers")