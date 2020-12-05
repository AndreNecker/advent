from Days.DayFive import DayFive 
from Days.InputDataReader import InputDataReader

 


msg = "hello world"
print(msg)

seats = InputDataReader().read_day_five()

xx = DayFive().get_seat_number(seats)

print(xx)
