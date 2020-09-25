from db.run_sql import run_sql
from models.trainer import Trainer

def save(trainer):
    sql = 'INSERT INTO trainers (name, active) VALUES (%s,%s) RETURNING *'
    values = [trainer.name,trainer.active]
    results = run_sql(sql,values)
    id = results[0]['id']
    trainer.id = id
    return trainer

def select_all():
    trainers = []
    sql = 'SELECT * FROM trainers'
    results = run_sql(sql)
    for row in results:
        trainer = Trainer(row['name'],row['active'],row['id'])
        trainers.append(trainer)
    return trainers

def select(id):
    sql = 'SELECT * FROM trainers WHERE id = %s'
    values = [id]
    results = run_sql(sql,values)[0]
    trainer = Trainer(results['name'],results['active'],results['id'])
    return trainer

def delete_all():
    sql = 'DELETE FROM trainers'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM trainers WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def update(trainer):
    sql = 'UPDATE trainers SET (name, active) = (%s,%s) WHERE id = %s'
    values = [trainer.name,trainer.active,trainer.id]
    run_sql(sql,values)