from Days.DayNine import DayNine 
from Days.InputDataReader import InputDataReader

 


msg = "hello world"
print(msg)

numbers = InputDataReader().read_day_nine()

number_to_search = DayNine().get_number_not_sum_of_previous_two(numbers, 25)
print('number_to_search: ' + str(number_to_search))
xx = DayNine().get_highest_and_smallest_numbers_to_sum(numbers, number_to_search)
print(xx)


