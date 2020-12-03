from DayOne import DayOne 
from DayTwo import DayTwo 
from DayThree import DayThree 
from InputDataReader import InputDataReader




msg = "hello world"
print(msg)

trees = InputDataReader().read_day_three()
counted_trees = DayThree().count_trees(trees)

print(counted_trees)
#DayOne().do_day_one()


