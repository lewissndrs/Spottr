from db.run_sql import run_sql
from models.booking import Booking
from models.activity import Activity
from models.member import Member

def save(booking):
    sql = 'INSERT INTO bookings (member_id,activity_id,note) VALUES (%s,%s,%s) RETURNING *'
    values = [booking.member.id,booking.activity.id,booking.note]
    results = run_sql(sql,values)
    id = results[0]['id']
    booking.id = id
    return booking

def select_all():
    bookings = []
    sql = 'SELECT * FROM bookings'
    results = run_sql(sql)
    for row in results:
        booking = Booking(row['member_id'],row['activity_id'],row['note'])
        bookings.append(booking)
    return bookings

def select(id):
    sql = 'SELECT * FROM bookings WHERE id = %s'
    values = [id]
    results = run_sql(sql,values)[0]
    booking = Booking(results['member_id'],results['activity_id'],results['note'],results['id'])
    return booking

def delete_all():
    sql = 'DELETE FROM bookings'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM bookings WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def update(booking):
    sql = 'UPDATE bookings SET (member_id,activity_id,note) = (%s,%s,%s) WHERE id = %s'
    values = [booking.member.id, booking.activity.id, booking.note, booking.id]
    run_sql(sql,values)