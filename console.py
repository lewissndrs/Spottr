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
booking_repository.delete_all()

trainer1 = Trainer('Tron')
trainer_repository.save(trainer1)

swimclass = Activity('Swim class','2020-01-01','18:00',trainer1)
activity_repository.save(swimclass)

weightclass = Activity('Weights class','2020-04-16','12:00',trainer1)
activity_repository.save(weightclass)

member1 = Member('Thom')
member_repository.save(member1)

booking1 = Booking(member1,swimclass)
booking_repository.save(booking1)

booking2 = Booking(member1, weightclass,'I might be late. Sorry!')
booking_repository.save(booking2)

bookings = booking_repository.select_all()

for booking in bookings:
    print(booking.__dict__)

booking_repository.delete(booking1.id)

booking2.note = 'Actually no, nevermind. It cool'
booking_repository.update(booking2)

bookings = booking_repository.select_all()

for booking in bookings:
    print(booking.member.name)

pdb.set_trace()