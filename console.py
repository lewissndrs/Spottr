import pdb
from models.member import Member
from models.trainer import Trainer
from models.booking import Booking
from models.activity import Activity

import repositories.activity_repository as activity_repository
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.trainer_repository as trainer_repository

activity_repository.delete_all()
member_repository.delete_all()
trainer_repository.delete_all()

trainer1 = Trainer('Tron')
trainer_repository.save(trainer1)

swimclass = Activity('Swim class','2020-01-01','18:00',trainer1)
activity_repository.save(swimclass)

weightsclass = Activity('Weights class','2020-04-16','12:00',trainer1)
activity_repository.save(weightsclass)

activity_repository.delete(weightsclass.id)

activities = activity_repository.select_all()

for activity in activities:
    print(activity.__dict__)

# trainer1 = Trainer('Tom')
# trainer2 = Trainer('Grace')

# trainer_repository.save(trainer1)
# trainer_repository.save(trainer2)

# member_repository.delete(member1.id)
# trainer_repository.delete(trainer1.id)

# trainer2.active = False
# trainer_repository.update(trainer2)

# trainers = trainer_repository.select_all()

# for everyone in trainers:
#     print(everyone.__dict__)

pdb.set_trace()