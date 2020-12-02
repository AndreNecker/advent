from SumFinder import SumFinder
from InputDataReader import InputDataReader 

class DayOne:
    def do_day_one(self):
        numbers = InputDataReader().read_day_one()
        sumFinder = SumFinder()
    
        productOf2 = sumFinder.findSumInTwo(numbers, 2020)
        productOf3 = sumFinder.findSumInThree(numbers, 2020)
    
        print(productOf2)
        print(productOf3)
