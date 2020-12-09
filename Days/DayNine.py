class DayNine:

    def get_number_not_sum_of_previous_two(self, numbers, length_preamble):

        index = length_preamble
        for number in numbers[index:]:
            previous_numbers = numbers[:index] #alle zahlen bis length
            previous_numbers = previous_numbers[(index - length_preamble):]
            if (not self.is_number_matching_sum(number, previous_numbers)):
                return number
            index = index + 1
        return 0




    def is_number_matching_sum(self, number, previous_numbers):
        return_value = False
        cnt = 0
        for n1 in previous_numbers:
            cnt = cnt + 1
            for n2 in previous_numbers[cnt:]:
                if ((n1 + n2) == number):
                    return True
        return return_value

    def get_highest_and_smallest_numbers_to_sum(self, numbers, number_to_be):
   
        added_numbers = []
        found = False
        outer_counter = 0
        while(outer_counter < len(numbers)):
            counter1 = outer_counter
            while(counter1 < len(numbers)):
                added_numbers.append(numbers[counter1])
                sum1 = sum(added_numbers)        
                if (sum1 == number_to_be):
                    found = True
                    print('FOUND')
                    break
                if (sum1 > number_to_be):
                    added_numbers = []
                    break
                counter1 = counter1 + 1
            if (sum(added_numbers) == number_to_be):
                found = True
                print('FOUND2')
            if (found == True):
                break
            outer_counter = outer_counter +1
        
        return max(added_numbers) + min (added_numbers)



