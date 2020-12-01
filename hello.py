from InputDataReader import InputDataReader 
from SumFinder import SumFinder


msg = "hello world"
print(msg)


numbers = InputDataReader().readFile()

sumFinder = SumFinder()
productOf2 = sumFinder.findSumInTwo(numbers, 2020)
productOf3 = sumFinder.findSumInThree(numbers, 2020)

print(productOf2)
print(productOf3)