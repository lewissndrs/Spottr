from db.run_sql import run_sql
from models.member import Member

import repositories.activity_repository as activity_repository

def save(member):
    sql = 'INSERT INTO members (name, active) VALUES (%s,%s) RETURNING *'
    values = [member.name,member.active]
    results = run_sql(sql,values)
    id = results[0]['id']
    member.id = id
    return member

def select_all():
    members = []
    sql = 'SELECT * FROM members'
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'],row['active'],row['id'])
        members.append(member)
    return members

def select(id):
    sql = 'SELECT * FROM members WHERE id = %s'
    values = [id]
    result = run_sql(sql,values)[0]
    member = Member(result['name'],result['active'],result['id'])
    return member

def delete_all():
    sql = 'DELETE FROM members'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM members WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def update(member):
    sql = 'UPDATE members SET (name, active) = (%s,%s) WHERE id = %s'
    values = [member.name,member.active,member.id]
    run_sql(sql,values)

def activities(id):
    activities = []
    sql = 'SELECT activity_id FROM bookings WHERE member_id = %s'
    values = [id]
    results = run_sql(sql,values)
    for row in results:
        activity = activity_repository.select(row['activity_id'])
        activities.append(activity)
    return activities