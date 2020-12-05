from InputDataReader import InputDataReader 

class SumFinder():

    def findSumInTwo(self, numbers, number_to_be):
       for line in numbers:
            for line2 in numbers:
                number = int(line)
                number2 = int (line2)
                sum =  number + number2
                if sum == number_to_be:
                    return number * number2


    def findSumInThree(self, numbers, number_to_be):
       for line in numbers:
            for line2 in numbers:
                for line3 in numbers:
                    number = int(line)
                    number2 = int (line2)
                    number3 = int (line3)
                    sum = number + number2 + number3
                    if sum == number_to_be:
                        return number * number2 * number3

