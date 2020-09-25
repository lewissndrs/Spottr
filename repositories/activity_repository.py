from db.run_sql import run_sql
from models.activity import Activity

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
        activity = Activity(row['name'],row['date'],row['time'],row['trainer_id'],row['id'])
        activities.append(activity)
    return activities

def select(id):
    sql = 'SELECT * FROM activities WHERE id = %s'
    values = [id]
    results = run_sql(sql,values)[0]
    activity = Activity(results['name'],results['date'],results['time'],results['trainer_id'],results['id'])
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