from DayOne import DayOne 
from DayTwo import DayTwo 
from DayThree import DayThree 
from InputDataReader import InputDataReader




msg = "hello world"
print(msg)

trees = InputDataReader().read_day_three()
counted_trees_11 = DayThree().count_trees(trees, 1, 1)
counted_trees_13 = DayThree().count_trees(trees, 1, 3)
counted_trees_15 = DayThree().count_trees(trees, 1, 5)
counted_trees_17 = DayThree().count_trees(trees, 1, 7)
counted_trees_21 = DayThree().count_trees(trees, 2, 1)

print(counted_trees_11 * counted_trees_13 * counted_trees_15 * counted_trees_17 * counted_trees_21)
#DayOne().do_day_one()


