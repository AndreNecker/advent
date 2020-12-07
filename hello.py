from Days.DaySeven import DaySeven 
from Days.InputDataReader import InputDataReader

 


msg = "hello world"
print(msg)

bags = InputDataReader().read_day_seven()

xx = DaySeven().count_bags_in_gold(bags)
print(xx)
