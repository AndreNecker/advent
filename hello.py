from Days.DayEight import DayEight 
from Days.InputDataReader import InputDataReader

 


msg = "hello world"
print(msg)

instructions = InputDataReader().read_day_eight()

dayEight = DayEight()
xx = dayEight.repair_instructions(instructions)
print(xx)
if (xx):
    print(dayEight.accumulator)

