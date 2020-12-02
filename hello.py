from DayOne import DayOne 
from DayTwo import DayTwo 
from InputDataReader import InputDataReader




msg = "hello world"
print(msg)

passwords = InputDataReader().read_day_two()

xx = DayTwo().read_day_two(passwords, 1)
print(xx)


#DayOne().do_day_one()


