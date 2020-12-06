from Days.DaySix import DaySix 
from Days.InputDataReader import InputDataReader

 


msg = "hello world"
print(msg)

votes = InputDataReader().read_day_six_per_person_per_group()

xx = DaySix().get_number_of_votes_per_group(votes)
print(xx)
