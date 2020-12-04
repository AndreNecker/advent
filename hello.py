from DayOne import DayOne 
from DayTwo import DayTwo 
from DayThree import DayThree 
from DayFour import DayFour 
from InputDataReader import InputDataReader

 


msg = "hello world"
print(msg)

passports = InputDataReader().read_day_four()

xx = DayFour().count_passports(passports)

print(xx)
