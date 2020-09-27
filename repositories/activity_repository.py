from db.run_sql import run_sql
from models.activity import Activity
from models.member import Member
from models.booking import Booking
import repositories.trainer_repository as trainer_repository
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository

def save(activity):
    sql = 'INSERT INTO activities (name,date,time,trainer_id) VALUES (%s,%s,%s,%s) RETURNING *'
    values = [activity.name, activity.date, activity.time, activity.trainer.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    activity.id = id
    return activity

def select_all():
    activities = []
    sql = 'SELECT * FROM activities'
    results = run_sql(sql)
    for row in results:
        trainer = trainer_repository.select(row['trainer_id'])
        activity = Activity(row['name'],row['date'],row['time'],trainer,row['id'])
        activities.append(activity)
    return activities

def select(id):
    sql = 'SELECT * FROM activities WHERE id = %s'
    values = [id]
    results = run_sql(sql,values)[0]
    trainer = trainer_repository.select(results['trainer_id'])
    activity = Activity(results['name'],results['date'],results['time'],trainer,results['id'])
    return activity

def delete_all():
    sql = 'DELETE FROM activities'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM activities WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def update(activity):
    sql = 'UPDATE activities SET (name, date, time, trainer_id) = (%s,%s,%s,%s) WHERE id = %s'
    values = [activity.name, activity.date, activity.time, activity.trainer.id, activity.id]
    run_sql(sql,values)

def bookings(id):
    bookings = []
    sql = 'SELECT bookings.* FROM bookings INNER JOIN activities ON bookings.activity_id = activities.id WHERE bookings.activity_id = %s'
    values = [id]
    results = run_sql(sql,values)
    for row in results:
        member = member_repository.select(row['member_id'])
        activity = activity_repository.select(row['activity_id'])
        booking = Booking(member,activity,row['note'],row['id'])
        bookings.append(booking)
    return bookings